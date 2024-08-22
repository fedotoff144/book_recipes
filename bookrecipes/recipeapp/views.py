from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Recipe


# Create your views here.

def index(request):
    return render(request, 'recipeapp/index.html')


def recipe_categories(request):
    return render(request, 'recipeapp/recipe_categories.html')


def recipe_category(request, category):
    context = []
    return render(request, 'recipeapp/recipe_category.html', context)


def add_recipe(request):
    if request.method == 'POST':
        pass
    return None