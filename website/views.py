import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=32e4d2a6840e4e530bb3e477aec0c38b'
    city= 'Tehran'

    r= requests.get(url.format(city)).json()
    #print(r.text)
    
    city_weather= {
        'city': city,
        'temp': r['main']['temp'],
        'desc': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    print(city_weather)

    return render(request, 'template.html', {'city_weather': city_weather})