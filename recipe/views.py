from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Category
from .forms import RecipeForm, CategoryForm, IngredientsForm
from django.http import HttpResponse


def RecipeListView(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


def RecipeDetailView(request, pk):
    recipe = Recipe.objects.get(pk = pk)
    return render(request, 'recipe_details.html', {'recipe': recipe})


def RecipeFormView(request):
    if request.method == 'GET':
        form = RecipeForm()
        return render(request, 'recipe_form.html', {'form': form})
    
    elif request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Recipe is added successfully'
            return render(request, 'recipe_form.html', {'form': form, 'msg': msg})
            # return redirect('recipe_form')

def CategoryFormView(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'category_form.html', {'form': form})
    
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Category is added successfully'
            return render(request, 'category_form.html', {'form': form, 'msg': msg})
        

def IngredientsFormView(request):
    if request.method == 'GET':
        form = IngredientsForm()
        return render(request, 'ingredients_form.html', {'form': form})

    elif request.method == 'POST':
        form = IngredientsForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Ingredient is added successfully'
            return render(request, 'ingredients_form.html', {'form': form, 'msg': msg})


def RecipeUpdateView(request, pk):
    recipe = Recipe.objects.get(pk = pk)
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        return render(request, 'recipe_update.html',{'form': form, 'recipe': recipe})

    elif request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
            # return render(request, 'recipe_update.html',{'form': form})



def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})


def recipes_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(categories=category)
    return render(request, 'recipe_list.html', {'recipes': recipes, 'category': category})



def recently_viewed(request):
    ids = request.COOKIES.get('recently_viewed', '')
    ids = ids.split(',') if ids else []
    recipes = Recipe.objects.filter(pk__in=ids)
    return render(request, 'recently_viewed.html', {'recipes': recipes})




