from django.shortcuts import render, redirect, HttpResponse
import urllib.request
import json
from geopy.geocoders import Nominatim
from django.contrib import messages

def homepage(request):
    return render(request, 'home.html')

def search_trail(request):
    geolocator = Nominatim()
    location = geolocator.geocode(request.POST['location'])
    if location is None:
        messages.error(request, "Enter a valid location")
        return redirect('/')
    else:
        latitude = location.latitude
        longitude = location.longitude
        token = "200676508-c12a355611c571567c0ce3a8469cbf2d"
        # url = f"https://www.hikingproject.com/data/get-trails?lat=40.0274&lon=-105.2519&maxDistance=10&key={token}"
        url = f"https://www.hikingproject.com/data/get-trails?lat={latitude}&lon={longitude}&maxDistance=20&maxResults=5&key={token}"
        req = urllib.request.Request(url)

        ##parsing response
        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))

        context = {
            "cont": cont['trails']
        }

    return render(request, 'results.html', context)
