from django.shortcuts import render, redirect, HttpResponse
import urllib.request
import json
from geopy.geocoders import Nominatim
from django.contrib import messages
from .models import Trail
from login_app.models import User
import os
from dotenv import load_dotenv 
load_dotenv()

def homepage(request):
    return render(request, 'home.html')

def search_trail(request):
    geolocator = Nominatim(timeout = 100)
    location = geolocator.geocode(request.GET['location'])
    if location is None:
        messages.error(request, "Enter a valid location")
        return redirect('/')
    else:
        latitude = location.latitude
        longitude = location.longitude
        token = os.getenv('TOKEN')
        url = f"https://www.hikingproject.com/data/get-trails?lat={latitude}&lon={longitude}&maxDistance=50&maxResults=15&key={token}"
        req = urllib.request.Request(url)

        ##parsing response
        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))

        context = {
            "cont": cont['trails'],
            "location": request.GET['location']
        }

    return render(request, 'results.html', context)

def trail_profile(request, trail_id):
    token = os.getenv('TOKEN')
    url = f'https://www.hikingproject.com/data/get-trails-by-id?ids={trail_id}&key={token}'
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    context = {
        "cont": cont['trails']
    }
    return render(request, 'profile.html', context)

def favorite_trail(request):
    if not 'user_id' in request.session:
        messages.error(request, "Sign in or register to favorite trails")
        return redirect('/login_registration')
    else:
        this_trail = int(request.POST['trail_id'])
        Trail.objects.create(
            trail_id = this_trail,
            user = User.objects.get(id = request.POST['user'])
        )
        return redirect(f"/search_trail?location={request.POST['location']}")

def user_profile(request, user_id):
    user = User.objects.get(id= user_id)
    user_trails = User.objects.get(id=user_id).favorite_trails.all()
    trail_ids = ""
    for trail in user_trails:
        trail_ids = trail_ids + str(trail.trail_id) + ","
    print(trail_ids)
    token = os.getenv('TOKEN')
    url = f"https://www.hikingproject.com/data/get-trails-by-id?ids={trail_ids}&key={token}"

    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    context = {
        "user": user,
        "trails": cont['trails']
    }
    return render(request, 'user.html', context)

