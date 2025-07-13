from django.urls import path
from .views import RecipeListView, RecipeDetailView


urlpatterns = [
    path('recipe-list/', view=RecipeListView, name= 'recipe_list'),
    path('recipe-details/<int:pk>', view= RecipeDetailView, name= 'recipe_details'),
    

]