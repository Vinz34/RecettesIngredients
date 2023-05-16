from django.urls import path
from . import views


app_name = "home_page"
urlpatterns = [
    path('', views.index, name='index'),
    path('settings/create/', views.create_recipe, name='create_recipe'),
    path('settings/ingredient/', views.add_ingredient, name='add_ingredient'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('settings/', views.settings, name='settings'),
    path('ingredients/<int:ingredient_id>/edit_ingredient/', views.edit_ingredient, name='edit_ingredient'),
    path('ingredients/<int:ingredient_id>/delete_ingredient/', views.delete_ingredient, name='delete_ingredient'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:recipe_id>/recipe_edit/', views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:recipe_id>/recipe_delete/', views.recipe_delete, name='recipe_delete'),

]