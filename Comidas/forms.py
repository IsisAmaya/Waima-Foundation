from django import forms 
from .models import comida

class FormularioComidas(forms.ModelForm): 
    class Meta: 
        model= comida 
        fields='__all__' 
        widgets={
                'producto':forms.TextInput(attrs={'class': 'form-control-small'}),
                'peso': forms.TextInput(attrs={'class': 'form-control-small'}),
                'modoIngreso':forms.Select(attrs={'class': 'form-control'}),
                'modoSalida':forms.Select(attrs={'class': 'form-control'}), 
                'FechaIngreso':forms.DateInput(attrs={'type':'date'}), 
                'fechaSalida':forms.DateInput(attrs={'type':'date'})
                }
