from django.shortcuts import render
from django.http import HttpResponse
import requests, re

# cases = requests.get('https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php',
# headers = {
# "X-RapidAPI-Host":"coronavirus-monitor.p.rapidapi.com",
# "X-RapidAPI-Key":"65b8fe815amshf5a6a02cb1f36c4p19b3e8jsn6ba08bcc824f"
# })
# str = cases.text
# country = re.findall(r"country_name\":\"(\w+)",str)
def statistic(dic):
    d = []
    i = 10
    while(i != 0):
        for k in dic['countries_stat'][10-i]:
            for e in dic['countries_stat'][10-i][k]:
                if e == ',':
                    d.append(e + '<br>')  # print(e)
                else:
                    d.append(e) #print(e, end="")
        i-=1
        return d

def home(request):
    cases = requests.get(
    'https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php',
    headers = {
    "X-RapidAPI-Host":"coronavirus-monitor.p.rapidapi.com",
    "X-RapidAPI-Key":"65b8fe815amshf5a6a02cb1f36c4p19b3e8jsn6ba08bcc824f"
    })
    dic= {}
    dic = cases.json()    #str = cases.text
    #country = re.findall(r"country_name\":\"(\w+)",str)
    # #re.sub(r"\',","\s", country)
    # #for lst in country:
    # #    lst = country
    # n = 0
    # lst = []
    # while(n != len(country)):
    #     lst.append(country[n]+'<br>')
    #     n+=1

    return render(request, 'home.html', dic)
