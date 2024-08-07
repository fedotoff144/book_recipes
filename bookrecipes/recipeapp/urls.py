from django.urls import path
from recipeapp.views import index

urlpatterns = [
    path('', index, name='index'),
]
