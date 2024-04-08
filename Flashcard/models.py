from django.db import models
from Accounts.models import UserAccount
from Mazos.models import Deck

# Create your models here.
class Flashcard(models.Model):
    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    mazo=models.ForeignKey(Deck,on_delete=models.CASCADE)
    fecha_Creacion=models.DateTimeField(auto_now_add=True)
    contenido=models.CharField(max_length=255)
    ultima_Revision=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    proxima_Revision=models.DateTimeField(null=True,blank=True)
    comentario=models.CharField(max_length=127)