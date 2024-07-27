from django.db import models

# Son clases que nos ayudan a gestionar la conexion en la base de datos

#Ponemos el nombre de la tabla, en este caso la tabla se llama 'Pokemon'
#NO necesitamos iniciar con los constructores

#Creacion de la clase Trainer

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


#CReacion de clase Pokemon
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES={
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
        ('L', 'Lagartija'),
    }
    #Choices define las opciones disponibles para el campo type. Cada elemento de esta tupla interna contiene dos partes:
    #La primera parte ('A', 'F', 'T') es el valor real que se almacenará en la base de datos cuando el usuario seleccione esa opción.
    #La segunda parte ('Agua', 'Fuego', 'Tierra') es la etiqueta legible para el usuario que se mostrará en el formulario o en la interfaz de administración de Django.
    type = models.CharField(max_length=30, choices=POKEMON_TYPES,  null=False)
    weight = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    height = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)    
    #on_delete=models.cascade, sirve para borrar el entrenador con todos sus pokemones, ya que normalmente no dejaria eliminar
    #el entrenador, porque tiene pokemones relacionados a su foreign key.
    picture = models.ImageField(upload_to='pokemon_images')
    #Necesitamos una libreria llamada pillow para poder poner imagenes
    def __str__(self) -> str:
        return self.name


