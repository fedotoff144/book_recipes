from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def advertisement(request):
    return render(request, 'userapp/advertisement.html')


def help_template(request):
    return render(request, 'userapp/help.html')


def rules(request):
    return render(request, 'userapp/rules.html')

