# Generated by Django 5.2.4 on 2025-07-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_ingredients_quantity_remove_ingredients_recipe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipe_ingredients', to='recipe.ingredients'),
        ),
    ]
