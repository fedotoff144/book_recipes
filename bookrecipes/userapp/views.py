from lib2to3.fixes.fix_input import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# from django.urls import reverse

from .models import User
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm


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
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userapp:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'userapp/profile.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            username = email
            user = User(username=username, name=name, email=email, password=password)
            user.save()
            login(request, user)
            return render(request, 'recipeapp/index.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'userapp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('recipeapp:index')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'userapp/login.html', context)


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('recipeapp:index')
