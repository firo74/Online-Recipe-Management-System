from django.db import models

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
        ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    instructions = models.TextField()
    preparation_time = models.CharField(max_length=50)
    cooking_time = models.CharField()
    difficulty_level = models.CharField(choices=DIFFICULTY_CHOICES)
    category = models.ManyToManyField('Category', related_name= 'recipe_category')
    ingredients = models.ManyToManyField('Ingredients', related_name= 'recipe_ingredients')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField()


    def __str__(self):
        return self.name


    





