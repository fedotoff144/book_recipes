from django.db import models
from userapp.models import User


# Create your models here.


class RecipeCategory(models.Model):
    category = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f'RecipeCategory(pk={self.pk}, {self.category!r})'

    class Meta:
        verbose_name = 'Категории рецептов'


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    servings = models.PositiveSmallIntegerField(blank=False)
    time = models.PositiveSmallIntegerField(blank=False)
    description = models.TextField()
    photo = models.ImageField(upload_to='recipes_photo/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)

    def __str__(self):
        # user = User.objects.filter(pk=self.user)
        return (f'Recipe(pk={self.pk}, '
                f'recipe: {self.recipe_name!r}, '
                f'user: {self.user.name}, '
                f'category: {self.recipe_category.category!r})')

    # @property
    # def short_description(self) -> str:
    #     if len(self.description) > 80:
    #         return self.description[:80] + '...'
    #     return self.description

    class Meta:
        verbose_name = 'Рецепты'


class CookingSteps(models.Model):
    step_description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return (f'CookingSteps(pk={self.pk}, recipe name: {self.recipe.recipe_name!r}, '
                f'description: {self.step_description[:15]}...)')

    # @property
    # def short_step_description(self) -> str:
    #     if len(self.step_description) > 80:
    #         return self.step_description[:80] + '...'
    #     return self.step_description

    class Meta:
        verbose_name = 'Шаги приготовления'


class Ingredients(models.Model):
    grocery = models.CharField(max_length=100)
    quantity = models.CharField(max_length=20)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'Ingredients(pk={self.pk}, grocery: {self.grocery!r})'

    class Meta:
        # ordering = ["quantity"] # ORDER BY quantity ASC
        ordering = ['-quantity']  # ORDER BY quantity DESC
        verbose_name = 'Ингридиенты'
