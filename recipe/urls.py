from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeFormView, CategoryFormView, IngredientsFormView, RecipeUpdateView, recipe_delete, recipes_by_category, recently_viewed


urlpatterns = [
    path('recipe-list/', RecipeListView, name= 'recipe_list'),
    path('recipe-details/<int:pk>', RecipeDetailView, name= 'recipe_details'),
    path('recipe-form/', RecipeFormView, name= 'recipe_form'),
    path('category-form/', CategoryFormView, name= 'category_form'),
    path('ingredients-form/', IngredientsFormView, name= 'ingredients_form'),
    path('recipe-update/<int:pk>', RecipeUpdateView, name= 'recipe_update'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
    path('category/<int:category_id>/', recipes_by_category, name='recipes_by_category'),
    path('recent/', recently_viewed, name='recently_viewed'),

]