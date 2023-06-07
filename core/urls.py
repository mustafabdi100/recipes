from django.urls import path
from .views import home, recipe_detail, submit_recipe,featured_recipes,profile

urlpatterns = [
    path('', home, name='home'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('submit_recipe/', submit_recipe, name='submit_recipe'),
    path('featured_recipes/', featured_recipes, name='featured_recipes'),
     path('profile/', profile, name='profile'),
]
