from django.contrib import admin
from .models import RecipeCategory, Recipe, CookingSteps, Ingredients


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category', 'category_name']
    ordering = ['pk']
    list_display_links = 'category', 'category_name'



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'recipe_name', 'servings', 'time']
    ordering = ['pk']
    list_display_links = 'recipe_name',
    search_fields = 'recipe_name',
    search_help_text = 'Поиск по полю recipe_name'

    # method for query optimization
    def get_queryset(self, request):
        return Recipe.objects.select_related('user', 'recipe_category')


@admin.register(CookingSteps)
class CookingStepsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'recipe', 'step_description_short']
    ordering = ['pk']
    list_display_links = 'recipe', 'step_description_short'

    def step_description_short(self, obj: CookingSteps) -> str:
        if len(obj.step_description) < 48:
            return obj.step_description
        return obj.step_description[:48] + '...'

    # method for query optimization
    def get_queryset(self, request):
        return CookingSteps.objects.select_related('recipe')


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'recipe', 'grocery']
    ordering = ['pk']
    list_display_links = 'recipe', 'grocery'
    search_fields = 'grocery',
    search_help_text = 'Поиск по полю grocery'

    # method for query optimization
    def get_queryset(self, request):
        return Ingredients.objects.select_related('recipe')
