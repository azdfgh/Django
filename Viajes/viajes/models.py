from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here

# Un destino es un lugar al que se puede viajar, pero sin incluir los datos respecto al viaje, como precio, etc...
class Destino(models.Model):
	lugar = models.CharField(max_length=100)
	descripcion = models.TextField()
	distancia = models.IntegerField()
	
	def __unicode__(self):
        	return self.lugar

class Viaje (models.Model):
	destino = models.ForeignKey(Destino)
	numero_de_dias = models.IntegerField()
	coste = models.IntegerField()
	modo_desplazamiento = models.CharField(max_length=100)

	def __unicode__(self):
		return (self.destino.lugar)


class Ruta(models.Model):
	Nombre_Ruta = models.CharField(max_length=100)
	Destinos = models.ManyToManyField(Destino)
	Precio_total= models.IntegerField()
	Duracion_Total= models.IntegerField()

	def __unicode__(self):
		return (self.Nombre_Ruta)

