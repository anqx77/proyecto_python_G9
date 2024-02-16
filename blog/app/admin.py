from django.contrib import admin

from .models import Publicacion, Postulante, Detalle_Postulante, Postulados


admin.site.register(Publicacion)

@admin.register(Postulante)
class Postulante(admin.ModelAdmin):
    list_display = ('id', 'nombre_postulante')
    

# @admin.register(Detalle_Postulante)
# class Detalle_Postulante(admin.ModelAdmin):
#     list_display = ('id','')

@admin.register(Postulados)
class Postulados(admin.ModelAdmin):
    list_display = ('id', 'fecha_postulacion')
