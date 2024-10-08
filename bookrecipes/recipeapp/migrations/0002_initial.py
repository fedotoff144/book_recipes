# Generated by Django 5.0.8 on 2024-08-24 09:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipeapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipe'),
        ),
        migrations.AddField(
            model_name='cookingsteps',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipecategory'),
        ),
    ]
