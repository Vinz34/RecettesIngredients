from django.db import models
from django.contrib.postgres.fields import *


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, default='')
    recette = models.TextField(max_length=1000, default='')
    ingredients = models.CharField(default='', max_length=1000)
    #ingredients_array = ArrayField(models.CharField(max_length=100), default = list)
    image = models.ImageField(upload_to='uploads/', default='uploads/unknown.png')

    def save(self, *args, **kwargs):
        # convertir la liste d'ingrédients en chaîne de caractères
        self.ingredients = self.ingredients.replace("<QuerySet [<Ingredient: ",'')
        self.ingredients = self.ingredients.replace(">",'')
        self.ingredients = self.ingredients.replace(" <Ingredient: ",'')
        self.ingredients = self.ingredients.replace("]",'')


        '''self.ingredients_array = self.ingredients.split(",")
        print(self.ingredients_array)'''

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name



    '''def save(self, *args, **kwargs):
        # convertir la liste d'ingrédients en chaîne de caractères
        ingredients_list = [ingredient.name for ingredient in self.ingredients.all()]
        self.ingredients = ','.join(ingredients_list)

        super().save(*args, **kwargs)

    def get_ingredients_list(self):
        # convertir la chaîne de caractères en liste
        return self.ingredients.split(',')'''