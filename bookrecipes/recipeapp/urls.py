from django.urls import path
from recipeapp.views import index, recipe_categories, recipe_category

app_name = 'recipeapp'

urlpatterns = [
    path('', index, name='index'),
    path('recipe_categories/', recipe_categories, name='recipe_categories'),
    path('recipe_category/<int:category>/', recipe_category, name='recipe_category'),
]
