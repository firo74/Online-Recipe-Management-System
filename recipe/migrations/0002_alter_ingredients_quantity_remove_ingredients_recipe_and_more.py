# Generated by Django 5.2.4 on 2025-07-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='quantity',
            field=models.CharField(),
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='recipe',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ManyToManyField(related_name='ingredients_recipe', to='recipe.recipe'),
        ),
    ]
