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
        print("working")
        script_output = subprocess.check_output(['python', 'playground/Search_Repo_Test.py', query])
        print('script done')
        decoded = script_output.decode('utf-8')
        print('done')
        return render(request, 'search_output.html', {'result': decoded})
        # If the form was not submitted, render the form template
        redirect(reverse('search_engine'))
    #     return redirect('output_page', query)
    else:
        return render(request, 'form.html')
