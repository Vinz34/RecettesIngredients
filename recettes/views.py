from django.db.models import ProtectedError
from django.http import Http404
from django.shortcuts import render
from .models import Recipe
from django.shortcuts import render, redirect
from .forms import RecipeForm, IngredientForm
from .models import Ingredient
from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'
    context_object_name = 'ingredients'


def index(request):
    return render(request, 'index.html')


def settings(request):
    # Render the settings.html template and return it as an HTTP response
    return render(request, 'recettes/settings.html')


def recipe_list(request):
    # Récupérer tous les ingrédients de la base de données
    ingredients = Ingredient.objects.all()

    # Récupérer toutes les recettes de la base de données
    recettes = Recipe.objects.all()

    selected_ingredients = request.GET.getlist('ingredient')

    if selected_ingredients:
        # Filtrer les recettes en fonction des ingrédients sélectionnés
        recettes = recettes.filter(ingredients__name__in=selected_ingredients)

    ingredients = ingredients.order_by('name')
    recettes = recettes.order_by('name')

    # Calculer le nombre de recettes où chaque ingrédient apparaît
    for ingredient in ingredients:
        for recipe in recettes:
            if recipe.ingredients.__contains__(str(ingredient)):
                ingredient.count += 1
        print(ingredient.count)

    context = {
        'ingredients': ingredients,
        'recettes': recettes,
        'selected_ingredients': selected_ingredients
    }

    return render(request, 'recettes/recipe_list.html', context)


def ingredient_list(request):
    try:
        ingredient = Ingredient.objects.all()
    except Ingredient.DoesNotExist:
        # If no Restaurants are found, raise an HTTP 404 error
        raise Http404("No restaurants available.")
    return render(request, 'recettes/ingredient_list.html', {'ingredients': ingredient})


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page:recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recettes/create_recipe.html', {'form': form})


def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].lower()
            if Ingredient.objects.filter(name=name).exists():
                messages.warning(request, f"L'ingrédient '{name}' existe déjà.")
            else:
                form.save()
            return redirect('home_page:ingredient_list')
    else:
        form = IngredientForm()
    ingredients = Ingredient.objects.all()
    return render(request, 'recettes/add_ingredient.html', {'form': form, 'ingredients': ingredients})


def delete_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    if request.method == 'POST':
        try:
            ingredient.delete()
            return redirect('../../')
        except ProtectedError:
            error_msg = f"L'ingrédient {ingredient.name} est utilisé dans au moins une recette et ne peut pas être supprimé."
            return render(request, 'recettes/error.html', {'error_msg': error_msg})
    return render(request, 'recettes/delete_ingredient.html', {'ingredient': ingredient})


def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home_page:recipe_list')
    return render(request, 'recettes/delete_recipe.html', {'recipe': recipe})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recettes/recipe_detail.html', {'recipe': recipe})


def recipe_edit(request, recipe_id):
    # get the restaurant object from the database using the restaurant_id parameter
    recipe = Recipe.objects.get(pk=recipe_id)

    # check if the request method is POST
    if request.method == 'POST':
        # create a form object and populate it with data from the request
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            # save the updated restaurant object to the database
            form.save()
            # redirect to the updated restaurant's detail page
            return redirect('../../', recipe.id)
    else:
        # create a form object and populate it with the current values from the restaurant object
        form = RecipeForm(instance=recipe)

    # render the update_restaurant template with the form object as context
    return render(request, 'recettes/recipe_edit.html', {'form': form})


def recipe_delete(request, recipe_id):
    # Retrieve the Restaurant object with the given restaurant ID
    recipe = Recipe.objects.get(pk=recipe_id)

    # If the HTTP request method is POST, delete the Restaurant object from the database and redirect to the index
    # view for all restaurants
    if request.method == 'POST':
        recipe.delete()
        return redirect('../../')

    # If the HTTP request method is not POST, render the remove_restaurant.html template with the Restaurant object
    # passed as context
    return render(request, 'recettes/recipe_delete.html', {'recipe': recipe})


def edit_ingredient(request, ingredient_id):
    # Retrieve the Burger object with the given burger ID
    ingredient = Ingredient.objects.get(pk=ingredient_id)

    # If the HTTP request method is POST, update the Burger object with the submitted form data and redirect to the
    # index view for all burgers
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            # Update the existing Burger object in the database with the submitted form data
            form.save()
            # Redirect to the index view for all burgers with the ID of the updated burger as a URL parameter
            return redirect('../../', ingredient.id)
    else:
        # If the HTTP request method is not POST, render the update_burger.html template with the Burger object and
        # form passed as context
        form = IngredientForm(instance=ingredient)

    return render(request, 'recettes/ingredient_edit.html', {'ingredient': ingredient, 'form': form})