from django.db import models
from Accounts.models import UserAccount

class Deck(models.Model):
    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=45)
    fecha_Creacion=models.DateTimeField(auto_now_add=True)
    ultima_Practica=models.DateTimeField(null=True,blank=True)