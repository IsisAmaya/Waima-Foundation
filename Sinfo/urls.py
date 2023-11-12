
from django.contrib import admin
from django.urls import path ,include
from Niños.views import FormularioNiñosView 
from Comidas.views import FormularioComidasView 
from miembros import views
#estas urs son de todo el proyecto en general, asi que vamos a haver un archivo urls.py para cada aplicacion y asi que cada una tenga sus urls
urlpatterns = [
    path('admin/', admin.site.urls),  
    #asi se enlazan las urls del pryecto con las de la app
    path('',include('Comedor.urls')), 
    #ya a la url se le debe agregar ProyectoWebApp/  
    path('Niños/',include('Niños.urls'),name='Niños'), 
    ##path('',include('app2.urls')), 
    ##path('',include('app3.urls')), 
    path('Comidas/',include('Comidas.urls')), 
    path('registrarNiño/',FormularioNiñosView.index, name='registrarNiño'), 
    path('guardarNiño/', FormularioNiñosView.procesar_form, name= 'guardarNiño'), 
    path('listarNiño/', FormularioNiñosView.listar_Niños, name= 'listarNiño '), 
    path('registrarComidas/',FormularioComidasView.index, name='registrarComida'),  
    path('guardarComidas/', FormularioComidasView.procesar_form, name= 'guardarComidas'), 
    path('listarComidas/',FormularioComidasView.listar_Comidas, name='listarComida'),  
    path('miembros/',include('django.contrib.auth.urls')), 
    
    path('miembros/',include('miembros.urls')), 
    path('loginUser/', views.login_user, name="login"),
    path('logoutUser/', views.logout_user, name='logout'),
    path('registerUser/', views.register_user, name='register_user'), 
    path('editarNiño/<int:id_niño>',FormularioNiñosView.editar, name='editarNiño'), 
    path('actualizarNiño/<int:id_niño>',FormularioNiñosView.actualizar_niño, name='actualizarNiño'),
    path('eliminarNiño/<int:id_niño>',FormularioNiñosView.delete, name='eliminarNiño'), 
    path('editarComida/<int:id_comida>',FormularioComidasView.editar, name='editarComida'), 
    path('actualizarComida/<int:id_comida>',FormularioComidasView.actualizar_comida, name='actualizarComida'), 
    path('eliminarComida/<int:id_comida>',FormularioComidasView.delete, name='eliminarComida'), 
    
]


