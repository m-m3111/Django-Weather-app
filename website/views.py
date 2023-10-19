import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=32e4d2a6840e4e530bb3e477aec0c38b'
    city= 'Tehran'

    r= requests.get(url.format(city)).json()
    #print(r)
    return render(request, 'template.html')