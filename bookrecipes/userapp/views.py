from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest
# from django.urls import reverse

from .models import User
from .forms import UserRegistrationForm, UserLoginForm


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


def profile(request):
    return render(request, 'userapp/profile.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            # username = email
            user = User(name=name, email=email, password=password)
            user.save()
            print(user)
            login(request, user)
            return render(request, 'recipeapp/index.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'userapp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # print(username, password)
            print(email, password)
            # user = authenticate(username=username, password=password)
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('recipeapp:index')
    else:
        form = UserLoginForm()
    return render(request, 'userapp/login.html', {'form': form})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('recipeapp:index')
