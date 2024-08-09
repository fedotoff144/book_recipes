from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserRegistration


# Create your views here.


def advertisement(request):
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
            password = form.cleaned_data['password1']
            user = User(name=name, email=email, password=password)
            user.save()
            return render(request, 'recipeapp/main.html', {'form': form})
    else:
        form = UserRegistration()
    return render(request, 'userapp/registration.html', {'form': form})
