import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=32e4d2a6840e4e530bb3e477aec0c38b'
     if request.method == 'POST':
        CityForm(request.POST).save()

     form = CityForm()
     cities = City.objects.all()
     data = []

     for city in cities:
        r= requests.get(url.format(city)).json()
        city_weather= {
            'city': city.name,
            'temp': r['main']['temp'],
            'desc': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        data.append(city_weather)
        print(data)

     return render(request, 'template.html', {'data': data, 'form': form})