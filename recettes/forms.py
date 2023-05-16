from django import forms
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)
    description = forms.CharField(widget=forms.Textarea)

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def clean_ingredients(self):
        selected_values = self.cleaned_data.get('ingredients')
        if not selected_values:
            raise forms.ValidationError("Veuillez sélectionner au moins un ingrédient.")
        return selected_values


    recette = forms.CharField(widget=forms.Textarea, required=False)

    image = forms.ImageField(required=False)

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'recette', 'image']

    '''def clean_new_ingredient_name(self):
        name = self.cleaned_data.get('new_ingredient')
        if name and Ingredient.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('Cet ingrédient existe déjà.')
        return name

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        ingredients = self.cleaned_data.get('ingredients')
        new_ingredient = self.cleaned_data.get('new_ingredient')
        if new_ingredient:
            ingredient, created = Ingredient.objects.get_or_create(name=new_ingredient)
            ingredients.append(ingredient)
        instance.ingredients.set(ingredients)
        return instance'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingredients'].required = False


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Ingredient.objects.filter(name=name).exists():
            raise forms.ValidationError('Cet ingrédient existe déjà')
        return name