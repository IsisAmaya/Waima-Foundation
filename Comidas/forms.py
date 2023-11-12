from django import forms 
from .models import comida

class FormularioComidas(forms.ModelForm): 
    class Meta: 
        model= comida 
        fields='__all__' 
        widgets={'producto':forms.TextInput(attrs={'class': 'form-control-small'}),'descripcion':forms.TextInput(attrs={'class': 'form-control-small'}),'informacion':forms.TextInput(attrs={'class': 'form-control-small'}), 'FechaIngreso':forms.DateInput(attrs={'type':'date'})}
