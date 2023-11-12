
from django.db import models

# Create your models here.

class Niños_tabla(models.Model):
    nombre = models.TextField(max_length=100)
    fechaDeNacimiento1 = models.DateField()
    peso= models.IntegerField(max_length=100)
    edad= models.IntegerField(max_length=100)
    infoTalla = models.TextField(max_length=4000)
    
    def _str_(self):
        return self.nombre 
    

class Niños_tabla2(models.Model):
    nombre = models.TextField(max_length=40)
    fechaDeNacimiento = models.DateField()
    peso = models.IntegerField(max_length=100)
    edad = models.IntegerField(max_length=100)
    infoTalla = models.TextField(max_length=40)
    FechaIngreso= models.DateField(null=True)
    
    def _str_(self): 
        return self.nombre

