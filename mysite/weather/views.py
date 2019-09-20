from django.shortcuts import render
import requests
from django.apps import apps
from .models import City
from .forms import CityForm
from django.contrib.auth import get_user_model
from django.contrib.gis.geoip2 import GeoIP2
# Create your views here.

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d5ce99cb6977c026aa0c2b641554b743'
	User = apps.get_model('home', 'User')
	user_dt = User.objects.get(username=request.user.username)
	cities = City.objects.filter(parent_user = user_dt)
	
	g = GeoIP2()
	def get_client_ip(request):
	    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	    if x_forwarded_for:
	        ip = x_forwarded_for.split(',')[0]
	    else:
	        ip = request.META.get('REMOTE_ADDR')
	    return ip
	
	user_ip = '2601:182:c902:5a72:55eb:a4f4:51f2:bd63'
	#user_ip = get_client_ip(request)
	cur_loc = g.city(user_ip)
	
	cur_city = cur_loc['city']
	print(cur_loc)
	cur_weather_dt = requests.get(url.format(cur_city)).json()
	cur_weather = {
				'city' : cur_city,
				'temperature' : cur_weather_dt['main']['temp'],
				'description' : cur_weather_dt['weather'][0]['description'],
				'icon' : cur_weather_dt['weather'][0]['icon']
			      }
	
	invalid_message = ''
	if request.method == 'POST':
		new_city = City(parent_user=user_dt)
		form = CityForm(request.POST, instance=new_city)
		form.save()
		new_city_name = new_city.name
		city_weather = requests.get(url.format(new_city_name)).json()
		
		# if the city name is invalid, do nothing and display an error message. 
		if 'message' in city_weather.keys() and city_weather['message'] == 'city not found':
			invalid_message = 'city not found'
			
	# delete duplicates
	for city in cities.distinct():
		cities.filter(pk__in=cities.filter(name=city.name).values_list('id', flat=True)[1:]).delete()
			
	form = CityForm()

	weather_data = []

	for city in cities:
		city_weather = requests.get(url.format(city)).json()
		if ('message' not in city_weather.keys()) or city_weather['message'] != 'city not found':
			weather = {
				'city' : city,
				'temperature' : city_weather['main']['temp'],
				'description' : city_weather['weather'][0]['description'],
				'icon' : city_weather['weather'][0]['icon']
			}
	
			weather_data.append(weather)

	context = {'cur_weather': cur_weather, 'weather_data' : weather_data, 'form' : form, 'invalid_message': invalid_message}

	return render(request, 'weather/index.html', context)
