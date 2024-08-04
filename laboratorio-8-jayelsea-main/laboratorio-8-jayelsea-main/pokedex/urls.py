from django.urls import path

from . import views

app_name = "pokedex"
urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon_id"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("edit_pokemon/<int:id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:id>", views.delete_pokemon, name="delete_pokemon"),
    path("add_trainer/", views.add_trainer, name="add_trainer"),
    path("trainer/", views.trainer_list, name="trainer_list"),
    path("trainer/trainer/<int:trainer_id>", views.trainer, name="trainer_id"),
    path('trainer/edit_trainer/<int:id>', views.edit_trainer, name="edit_trainer"),
    path('trainer/delete_trainer/<int:id>', views.delete_trainer, name="delete_trainer")
    
    
]

