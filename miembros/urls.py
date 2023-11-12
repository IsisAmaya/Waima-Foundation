
from django.urls import path  
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [ 

    path('loginUser', views.login_user, name="login"),
    path('logoutUser', views.logout_user, name='logout'),
    path('registerUser', views.register_user, name='register_user'),
    
]

