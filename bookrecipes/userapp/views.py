from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpRequest
from django.urls import reverse

from .models import User
from .forms import UserRegistration, UserLogin


# Create your views here.


def advertisement(request: HttpRequest):
    # print(request.path)
    # print(request.method)
    # print(request.headers)
    return render(request, 'userapp/advertisement.html')


def help_template(request):
    return render(request, 'userapp/help.html')


def rules(request):
    return render(request, 'userapp/rules.html')


def reg(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            username = email.split('@')[0]
            user = User(name=name, email=email, username=username)
            user.save()
            print(user)
            return render(request, 'recipeapp/index.html', {'form': form})
    else:
        form = UserRegistration()
    return render(request, 'userapp/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            print(email, password)
            print('user' if user else 'not user')
            # print('user.is_active' if user.is_active else 'user is not active')
            if user and user.is_active:
                login(user)
                print('3 STAGE', email, password)
                return HttpResponse(reverse('index'))
    else:
        form = UserLogin()
    return render(request, 'userapp/login.html', {'form': form})
