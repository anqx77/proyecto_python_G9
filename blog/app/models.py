from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    titulo      = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    email       = models.EmailField(blank=True, null=True)
    
    def __str__(self): 
        return self.titulo

class Postulante(models.Model):
    nombre_postulante = models.CharField(max_length=144, blank= False, null=False)
    apellido_postulante = models.CharField(max_length=144, blank= False, null=False)
    GENERO_CHOICES = {
        "Hombre": "Masculino",
        "Mujer":  "Femenino", 
    }
    edad_postulante = models.IntegerField(blank=False, null=False)
    direccion_postulante = models.TextField(blank = True, null = True, default='')
    email_postulante = models.EmailField(blank=True, null=True)
    telefono_postulante = models.CharField(max_length=10, blank=False, null=False)
    PROVINCE_CHOICES = (('A', 'Azuay'), ('B', 'Bolívar'), ('F', 'Cañar'), ('C', 'Carchi'), ('H', 'Chimborazo'), ('X', 'Cotopaxi'), ('O', 'El Oro'), ('E', 'Esmeraldas'), ('W', 'Galápagos'), ('G', 'Guayas'), ('I', 'Imbabura'), ('L', 'Loja'), ('R', 'Los Ríos'), ('M', 'Manabí'), ('S', 'Morona Santiago'), ('N', 'Napo'), ('D', 'Orellana'), ('Y', 'Pastaza'), ('P', 'Pichincha'), ('SE', 'Santa Elena'), ('SD', 'Santo Domingo de los Tsáchilas'), ('U', 'Sucumbíos'), ('T', 'Tungurahua'), ('Z', 'Zamora Chinchipe'))
    calificacion_postulante = models.CharField(max_length=3,  blank=True)

    def __str__(self):
        return self.nombre_postulante

class Detalle_Postulante(models.Model):
    
    
    cv_laboral = models.FileField(upload_to="uploads", blank = True )
    NIVEL_LABORAL_CHOICES = {
        "SEGUNDO": "SECUNDARIA",
        "TERCER": "UNIVERSIDAD",
        "CUARTO": "MASTERADO",
        "QUINTO": "PHD",
    }
    descripcion_laborar = models.TextField(blank = True, null = True, default='')
   
    
    def __str__(self):
        return self.experiencia_laboral

class Postulados(models.Model):
    # ESTADO_POSTULADOS_CHOICES = {
    #     "ACTIVO": "ENVIADO",
    #     "DESACTIVADO": "RECHAZADO",
    #     "PROCESS": "EN PROCESO",
    #     "ENTREVISTADO": "ENTREVISTADO",
    #     "CONTRATADO": "CONTRATADO",
    # }
    fecha_postulacion = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.fecha_postulacion

