
from django.db import models
from django import forms
# Create your models here.
class comida(models.Model):
    
    opciones1 = [
        ('Compra', 'Compra'),
        ('Donacion', 'Donacion'),
    ]
    
    opciones2 = [
        ('Comedor', 'Comedor'),
        ('Donacion', 'Donacion'),
    ]
    
    producto = models.TextField(max_length=50)
    FechaIngreso= models.DateField(null=True)
    modoIngreso = models.CharField(max_length=100, choices=opciones1, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    fechaSalida = models.DateField(null=True)
    modoSalida = models.CharField(max_length=100, choices=opciones2, null=True)
    
    
    
    def _str_(self):
        return self.producto 

