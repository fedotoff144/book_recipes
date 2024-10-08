from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .forms import AddRecipe


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
        form = AddRecipe(request.POST)
        if form.is_valid():
            print(**request)
    else:
        form = AddRecipe()
    # return render(request, 'recipeapp/add_recipe.html', {'form': form})
    return None
