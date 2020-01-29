from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import User
import bcrypt 

def index(request):
    return render(request, 'login.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/login_registration")
    else:
        hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashed_pass)
        request.session['user_id'] = user.id 
        request.session['user_email'] = user.email
        request.session['first_name'] = user.first_name
        messages.info(request, "Successfully registered, please log in.")
        return redirect("/login_registration")

def user_login(request):
    users = User.objects.filter(email = request.POST['email'])

    if len(users) != 1:
        messages.error(request, "Invalid e-mail")
        return redirect('/login_registration')

    user = users[0]

    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "Invalid e-mail")
        return redirect('/login_registration')
    else:
        request.session['user_id'] = user.id 
        request.session['user_email'] = user.email
        request.session['first_name'] = user.first_name
        return redirect('/')

    return redirect('/')

def success(request):
    if not 'user_id' in request.session:
        messages.error(request, 'Please log in')
        return redirect('/')
    return render(request, 'success.html')

def user_logout(request):
    request.session.clear()
    return redirect('/')
