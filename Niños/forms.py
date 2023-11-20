from django import forms 
from .models import Niños_tabla2

class FormularioNiños(forms.ModelForm): 
    class Meta: 
        model= Niños_tabla2 
        fields='__all__' 
        widgets={'fechaDeNacimiento': forms.DateInput(attrs={'type':'date'}),'nombre':forms.TextInput(attrs={'class': 'form-control-small'}),'infoTalla':forms.TextInput(attrs={'class': 'form-control-small'}), 'FechaIngreso':forms.DateInput(attrs={'type':'date'})}


class FormularioExportarExcel(forms.Form):
        OPCIONES = [
            ('historico', 'Histórico'),
            ('mes', 'Seleccionar un mes'),
        ]

        option = forms.ChoiceField(choices=OPCIONES, initial='historico')
        mes = forms.DateField(input_formats=['%Y-%m'], required=False)