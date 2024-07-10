from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #Mantener id pokemon
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon_id"),
]