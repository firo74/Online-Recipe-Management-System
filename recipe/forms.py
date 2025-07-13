from django.forms import ModelForm
from .models import Recipe, Ingredients, Category

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'