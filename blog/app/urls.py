
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('agregar', views.agregar, name = 'agregar'),
    path('eliminar/<publicacion_id>', views.eliminar, name = 'eliminar'),
    path('actualizar/<publicacion_id>', views.actualizar, name ="actualizar"), 
    path('postular', views.postular, name = 'postular'),
    
   
]
