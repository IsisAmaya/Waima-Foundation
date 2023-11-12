
from django.urls import path  
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import FormularioComidasView
urlpatterns = [ 
    path('registrarComidas/',FormularioComidasView.index, name='registrarComida'), 
    path('listarComidas/',FormularioComidasView.index, name='listarComida'),
    
]
