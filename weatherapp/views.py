from django.shortcuts import render
import requests
from .forms import CityForm
# Create your views here.

API_KEY = '73eeb5bb57df43861abc7c225d459b93'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city):
     url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=fa"
     response = requests.get(url)
     return response.json()


def home(request):
    weather_data = None
    city = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)
    else:
        form = CityForm()

    return render(request, 'weatherapp/home.html', {'form': form, 'weather_data': weather_data, 'city': city})

