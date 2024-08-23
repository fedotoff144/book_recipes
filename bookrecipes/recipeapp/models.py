from django.db import models
from userapp.models import User


# Create your models here.


class RecipeCategory(models.Model):
    category = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    servings = models.ImageField()
    time = models.ImageField()
    description = models.TextField()
    photo = models.ImageField(upload_to='recipes_photo/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_category_id = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)

    def __str__(self):
        user = User.objects.filter(pk=self.user_id)
        return (f'name of dish: {self.name},'
                f'quantity servings: {self.servings},'
                f'time of cooking: {self.time}'
                f'user: {self.user_id.name}'
                f'category of recipe: {self.recipe_category_id.category}')


class CookingSteps(models.Model):
    step_description = models.TextField()
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return (f'description step of cooking: {self.step_description},'
                f'recipe name: {self.recipe_id.name}')


class Ingredients(models.Model):
    grocery = models.CharField(max_length=100)
    quantity = models.CharField(max_length=20)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return (f'grocery: {self.grocery},'
                f'quantity: {self.quantity},'
                f'for recipe: {self.recipe_id.name}')
