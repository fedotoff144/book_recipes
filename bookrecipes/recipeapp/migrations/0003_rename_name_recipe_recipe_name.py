# Generated by Django 5.0.8 on 2024-08-23 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='recipe_name',
        ),
    ]
