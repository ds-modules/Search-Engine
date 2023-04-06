from turtle import home
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django import forms
import subprocess
# Create your views here.
# request -> response
# request handler 
# action 

def search_engine(request):
    if request.method == 'POST':
        # If the form was submitted, process the form data
        query = request.POST.get('query')
        # Use the form data to generate some output
        script_output = subprocess.check_output(['python', 'playground/Search_Repo_Test.py', query])
        decoded = script_output.decode('utf-8')[1:-2]
        repo_list = ast.literal_eval(decoded)
        repo_list = list(repo_list)
        print(repo_list)

        url = 'https://raw.githubusercontent.com/ds-modules/Search-Engine/main/tags/tags.json'
        resp = requests.get(url)
        tags = json.loads(resp.text)
        print(tags['BUDS-su20']['department'])
        departments, names, semesters = [], [], []
        for i in repo_list:
            departments.append(tags[i]['department'])
            names.append(tags[i]['name'])
            semesters.append(tags[i]['semester'])

        zipped_list = zip(repo_list,departments, names, semesters)

        return render(request, 'index-testing.html', {"information":zipped_list})
        # If the form was not submitted, render the form template
        redirect(reverse('search_engine'))
        # return redirect('output_page', query)
    else:
        return render(request, 'index-testing.html')
