from django.shortcuts import render, redirect 

def homepage(request):
    return render(request, 'home.html')

def search_trail(request):
    token = "200676508-c12a355611c571567c0ce3a8469cbf2d"
    url = "https://www.hikingproject.com/data/get-trails?lat=40.0274&lon=-105.2519&maxDistance=10&key=200676508-c12a355611c571567c0ce3a8469cbf2d"
    return render(request, 'results.html')
