from django.db import models
from Documents.models import PDFDocument
from Accounts.models import UserAccount

# Create your models here.
class Note(models.Model):
    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE,null=True)
    documento=models.ForeignKey(PDFDocument,on_delete=models.CASCADE)
    contenido=models.CharField(max_length=511,default="")
    cita = models.CharField(max_length=511,default="")
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    highlight_areas = models.JSONField(default=list)