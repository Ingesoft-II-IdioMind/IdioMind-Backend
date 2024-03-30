from django.db import models
from Accounts.models import UserAccount

# Create your models here.
class PDFDocument(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)  # Definir la longitud máxima del título
    autor = models.CharField(max_length=255)   # Definir la longitud máxima del autor
    fecha_subida = models.DateField(auto_now_add=True)          # Puedes especificar el formato de fecha si lo deseas
    ultima_vez_abierto = models.DateField(null=True, blank=True)  
    base64 = models.TextField()