from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest 
from .forms import FormularioComidas 
from .models import comida
from django.contrib import messages
# Create your views here.
class FormularioComidasView(HttpRequest):  
    def index(request):
        Comidas=FormularioComidas() 
        return render (request,"ComidasIndex.html",{"form":Comidas}) 
    
    def procesar_form(request): 
        Comidas=FormularioComidas(request.POST) 
        if Comidas.is_valid(): 
            Comidas.save() 
            Comidas=FormularioComidas() 
        return render(request, "ComidasIndex.html",{"form":Comidas, "mensaje":'OK'}) 
    
    def listar_Comidas(request): 
        Comidas=comida.objects.all() 
        return render(request, "ComLista.html",{"Comidas":Comidas}) 
    
    
    def editar(request, id_comida):  
        Comidas_edit=comida.objects.filter(id=id_comida).first() 
        form=FormularioComidas(instance=Comidas_edit) 
        return render (request,"ComidaEdit.html",{"form":form, 'Comidas':Comidas_edit}) 
    
    def actualizar_comida(request, id_comida):
        Comida= comida.objects.get(pk=id_comida)
        form= FormularioComidas(request.POST, instance=Comida)
        if form.is_valid():
            form.save() 
        messages.success(request,'Comida actualizada correctamente')
        Comidas = comida.objects.all()
        return render(request, "ComLista.html",{"form":form, "Comidas":Comidas}) 

    def delete(request,id_comida): 
        Comida=comida.objects.get(pk=id_comida) 
        Comida.delete()
        messages.success(request,'Comida eliminada correctamente')
        Comidas=comida.objects.all() 
        return render(request,"ComLista.html",{"Comidas":Comidas})