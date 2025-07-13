from django.shortcuts import render
from .models import Recipe


def RecipeListView(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


def RecipeDetailView(request, pk):
    recipe = Recipe.objects.get(pk = pk)
    return render(request, 'recipe_details.html', {'recipe': recipe})
