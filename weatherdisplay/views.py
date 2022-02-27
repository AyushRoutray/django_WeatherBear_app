from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=f1400ffdcdd1409698305fd261b54aea&units=metric').read()
        list_of_data = json.loads(source)
        data = {'countryname':str(list_of_data['sys']['country']).lower(), 
                'temperature':str(list_of_data['main']['temp']), 
                'icon':list_of_data['weather'][0]['icon'],
                'desc':list_of_data['weather'][0]['description'].title(),
                'city':city,}
    else:
        data = {}
    return render(request, 'weatherdisplay/weathercard.html', data)