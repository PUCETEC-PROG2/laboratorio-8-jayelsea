from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Pokemon
from pokedex.forms import PokemonForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



def index(request):
    pokemons = Pokemon.objects.order_by('type')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))


#Crearemos la vista add pokemon
#EL request obtiene los datos enviados desde el formulario por el metodo "post" 

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
        
    return render(request,'polemos_form.html', 'add_pokemon.html', {'form':form})
#Crearemos la vista del login, heredando el login de nuestro administrador.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
@login_required
def edit_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk = id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
        
    return render(request,'pokemon_form.html', {'form':form})

@login_required
def delete_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk = id)
    pokemon.delete()
    return redirect("pokedex:index")
    