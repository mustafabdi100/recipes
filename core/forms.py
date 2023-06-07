from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image', 'prep_time', 'cook_time', 'total_time', 'servings', 'ingredients', 'directions']
