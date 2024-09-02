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
            username = email
            user = User(name=name, email=email, username=username, password=password)
            user.save()
            print(user)
            login(request, user)
            return render(request, 'recipeapp/index.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'userapp/register.html', {'form': form})


# def login_view(request: HttpRequest):
#     if request.method == 'GET':
#         if request.user.is_authenticated:
#             return redirect('/admin/')
#
#         return render(request, 'userapp/login.html')
#
#     username = request.POST['username']
#     password = request.POST['password']
#
#     user = authenticate(request, username=username, password=password)
#     # print(user.pk)
#     # print(username, password)
#     if user:
#         login(request, user)
#         return redirect('recipeapp:index')
#
#     return render(request, 'userapp/login.html', {'error': 'User not found'})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        if form.is_valid():
            # user = User(**form.cleaned_data)
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
        else:
            print(form.errors)
    else:
        # form = UserLoginForm(request)
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'userapp/login.html', context)


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('recipeapp:index')
