
from django.urls import path  
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import FormularioNiñosView  

urlpatterns = [ 

    path('registrarNiño/',FormularioNiñosView.index, name='registrarNiño'), 
    path('listarNiños/',FormularioNiñosView.listar_Niños, name='listarNiño'),
    path('editarNiño/',FormularioNiñosView.editar, name='editarNiño'), 
    path('actualizarNiño/',FormularioNiñosView.actualizar_niño, name='actualizarNiño'),
    
    
]

