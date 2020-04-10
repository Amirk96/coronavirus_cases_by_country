from django.shortcuts import render
from django.http import HttpResponse
import requests, re

def home(request):
    cases = requests.get(
    'https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php',
    headers = {
    "X-RapidAPI-Host":"coronavirus-monitor.p.rapidapi.com",
    "X-RapidAPI-Key":"65b8fe815amshf5a6a02cb1f36c4p19b3e8jsn6ba08bcc824f"
    })
    dic= {}
    dic = cases.json()   
    return render(request, 'home.html', dic)
