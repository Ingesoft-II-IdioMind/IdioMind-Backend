from django.db import models

# Create your models here.

class Post(models.Model):
    Titulo = models.CharField(max_length=128,null=True,blank=True)
    Fecha_publicacion = models.DateTimeField(auto_now_add=True)
    Autor = models.CharField(max_length=128,null=True,blank=True)
    Imagen = models.URLField(null=True, blank=True,max_length=1024)
    Contenido = models.CharField(max_length=1024,null=True,blank=True)