from turtle import home
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django import forms
import subprocess, ast, json, requests
from django.template import Template, Context
import datetime

def main(request):
    return render(request, 'main_page.html')

def search(request):
    # If the form was submitted, process the form data
    # Use the form data to generate some output
    query = request.GET.get('query')
    script_output = subprocess.check_output(['python3', 'website/Search_Repo_Test.py', query])
    decoded = script_output.decode('utf-8')[1:-2]
    repo_list = ast.literal_eval(decoded)
    repo_list = list(repo_list)
    print(repo_list)

    url = 'https://raw.githubusercontent.com/ds-modules/Search-Engine/main/tags/tags.json'
    resp = requests.get(url)
    tags = json.loads(resp.text)
    info_dict = {}
    departments, names, semesters = [], [], []
    for i in repo_list:
        if i not in tags:
            continue
        else:
            departments.append(tags[i]['department'])
            names.append(tags[i]['name'])
            semesters.append(tags[i]['semester'])
            info_dict[i] = [tags[i]['department'], tags[i]['name'], tags[i]['semester']]
    
    today = datetime.date.today()
    year = today.year
    total_semesters = (year - 2015 + 1) * 3
    year_list = []
    while year >= 2015:
        year_list.append(f'Fall {year}')
        year_list.append(f'Summer {year}')
        year_list.append(f'Spring {year}')
        year -= 1
    repo_information = [[] for _ in range(total_semesters)]

    others = []
    for i in repo_list:
        if i not in tags:
            continue
        else:
            semester = info_dict[i][2]
            if semester in year_list:
                index = year_list.index(info_dict[i][2])
                repo_information[index].append([i, info_dict[i][0], info_dict[i][1], info_dict[i][2]])
            else:
                others.append([i, info_dict[i][0], info_dict[i][1], info_dict[i][2]])
    # repo_information = repo_information[0]
    final_information = []
    for i in repo_information:
        if len(i) == 0:
            continue
        elif type(i[0]) != list:
            final_information.append(i)
        else:
            for j in i:
                final_information.append(j)
    for i in others:  
        final_information.append(i)
    print(final_information)
    print('------')
    # Now repo_information is in the form [[[1, 1, 1, 1], [1, 1, 1, 1]], [...]]
    # call list[0] -> [[1,1,1,1], [1,1,1,1], [...]]
    zipped_list = zip(repo_list,departments, names, semesters)
    print(zipped_list)
    # print(zipped_list)

    # return render(request, 'search_information.html', {"information":final_information})
    return render(request, 'search_information.html', {"information":final_information, 'parent_template':'main_page.html'})
    # return JsonResponse({"information":final_information}, safe=False
