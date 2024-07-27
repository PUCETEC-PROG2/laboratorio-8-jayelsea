from django import forms
from .models import Pokemon
#CReamos la clase para agregar el formulario de agregar pokemon en nuestra web

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        #fields = ['name', 'type', 'weight', 'height', 'trainer', 'picture'] para elegir todo usamos "fields= __all__"
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }