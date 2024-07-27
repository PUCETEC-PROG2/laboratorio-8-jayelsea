from django.urls import path

from . import views

app_name = "pokedex"
urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon_id"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("edit_pokemon/<int:id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:id>/", views.delete_pokemon, name="edit_pokemon")
]

#Con .as_view convertimos una clase en una vista, recuerda que anteriormente usabamos funciones