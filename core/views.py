from django.shortcuts import render, redirect
from .models import Recipe
from django.shortcuts import get_object_or_404
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required



def home(request):
    featured_recipes = Recipe.objects.all()[:6] # this will get the first six recipes, consider using a filter if you have a way of marking a recipe as featured.
    context = {
        'featured_recipes': featured_recipes
    }
    return render(request, 'core/home.html', context)

def featured_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'core/featured_recipes.html', context={
        'recipes': recipes,
    })

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'core/recipe_detail.html', {'recipe': recipe})

@login_required
def submit_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'core/submit_recipe.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
