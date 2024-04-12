from django.db import models
from Documents.models import PDFDocument

# Create your models here.
class Note(models.Model):
    idDocumento=models.ForeignKey(PDFDocument,on_delete=models.CASCADE)
    contenido=models.CharField(max_length=255)
    fecha_Creacion=models.DateTimeField(auto_now_add=True)