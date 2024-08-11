from django import forms


class AddRecipe(forms.Form):
    recipe_name = forms.CharField(max_length=50)
    servings = forms.IntegerField()
    time = forms.IntegerField()
    description = forms.CharField(max_length=500)
    photo = forms.ImageField()
    user_id = forms.IntegerField()
    recipe_category_id = forms.IntegerField()

