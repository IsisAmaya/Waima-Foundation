from django.shortcuts import render
from django.http import HttpRequest 
from .forms import FormularioNiños 
from .models import Niños_tabla2
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.contrib import messages
# Create your views here.
"""def app1_vista(request): 
    return render(request,'niños.html') 
""" 
class FormularioNiñosView(HttpRequest): 
    def init(self, args, **kwargs):
        super(FormularioNiños, self).init(args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Field('nombre', css_class='form-control-small'))

    def index(request):
        Niños=FormularioNiños() 
        return render (request,"NiñosIndex.html",{"form":Niños}) 
    
    def procesar_form(request): 
        Niños=FormularioNiños(request.POST) 
        if Niños.is_valid(): 
            Niños.save() 
            Niños=FormularioNiños() 
        return render(request, "NiñosIndex.html",{"form":Niños, "mensaje":'OK'}) 
    
    def listar_Niños(request): 
        Niños=Niños_tabla2.objects.all() 
        return render(request, "NiñosLista.html",{"Niños":Niños})  
    
    def editar(request, id_niño):  
        Niños_edit=Niños_tabla2.objects.filter(id=id_niño).first() 
        form=FormularioNiños(instance=Niños_edit) 
        return render (request,"NiñoEdit.html",{"form":form, 'Niños':Niños_edit}) 
    
    def actualizar_niño(request, id_niño):
        Niño = Niños_tabla2.objects.get(pk=id_niño)
        form= FormularioNiños(request.POST, instance=Niño)
        if form.is_valid():
            form.save() 
        messages.success(request,'Niño actualizado correctamente')
        Niños_actualizar = Niños_tabla2.objects.all() 

        return render(request, "NiñosLista.html",{"form":form, "Niños":Niños_actualizar}) 
    
    def delete(request,id_niño): 
        Niño=Niños_tabla2.objects.get(pk=id_niño) 
        Niño.delete()
        messages.success(request,'Niño eliminado correctamente')
        Niños=Niños_tabla2.objects.all() 
        return render(request,"NiñosLista.html",{"Niños":Niños})