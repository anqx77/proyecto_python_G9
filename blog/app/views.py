from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Publicacion, Empleo
from  .forms import PublicacionForm, EmpleoForm

def actualizar(request, publicacion_id): 
    publicacion = Publicacion.objects.get(pk = publicacion_id)
    form = PublicacionForm(request.POST or None, instance = publicacion)
    if form.is_valid(): 
        form.save()
        messages.success(request, 'Publicación Actualizada')
        return redirect(home)  
    return render(request, 'app/actualizar.html', {'publicacion':publicacion, 'form': form})
    
def eliminar(request, publicacion_id):
    publicacion = Publicacion.objects.get(pk = publicacion_id)
    publicacion.delete()
    messages.success(request, 'Publicación Eliminada')
    return redirect(home)  
    
def agregar(request): 
    if request.POST: 
        form = EmpleoForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Publicacion Añadida')
        return redirect(home)  

    return render(request, 'app/agregar.html', {'form':EmpleoForm})

def home(request): 
    empleos = Empleo.objects.all()
    return render(request, 'app/home.html', {'empleos': empleos})

def index(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'app/index.html', {'publicaciones': publicaciones})

def postular(request): 
    if request.POST: 
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Postulación Exitosa')
        return redirect(index)  
