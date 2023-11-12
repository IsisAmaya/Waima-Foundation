from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import FormularioComidas 
from .models import comida
from django.contrib import messages
import openpyxl
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
    
    def export_excel(request):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="mydata.xlsx"'

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'My Data'

        # Write header row
        header = ['Producto',  'Modo de Ingreso', 'Peso',  'Fecha de Ingreso', 'Modo de Salida', 'Fecha de Salida']
        for col_num, column_title in enumerate(header, 1):
            cell = worksheet.cell(row=1, column=col_num)
            cell.value = column_title

        # Write data rows
        queryset = comida.objects.all().values_list('producto',  'modoIngreso',  'peso', 'FechaIngreso', 'modoSalida', 'fechaSalida')
        for row_num, row in enumerate(queryset, 1):
            for col_num, cell_value in enumerate(row, 1):
                cell = worksheet.cell(row=row_num+1, column=col_num)
                cell.value = cell_value
            

        
        for col_letter in ["D", "F"]:
            worksheet.column_dimensions[col_letter].auto_size = True
        
        workbook.save(response)

        return response