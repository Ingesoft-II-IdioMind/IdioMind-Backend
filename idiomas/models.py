from django.db import models

# Create your models here.
class Idiom(models.Model):
    nombre= models.CharField(max_length=255)  # Definir la longitud máxima del título