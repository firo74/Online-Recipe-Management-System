from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeFormView, CategoryFormView, IngredientsFormView, RecipeUpdateView


urlpatterns = [
    path('recipe-list/', RecipeListView, name= 'recipe_list'),
    path('recipe-details/<int:pk>', RecipeDetailView, name= 'recipe_details'),
    path('recipe-form/', RecipeFormView, name= 'recipe_form'),
    path('category-form/', CategoryFormView, name= 'category_form'),
    path('ingredients-form/', IngredientsFormView, name= 'ingredients_form'),
    path('recipe-update/', RecipeUpdateView, name= 'recipe_update')

]