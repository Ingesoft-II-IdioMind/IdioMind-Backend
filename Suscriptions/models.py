from django.db import models
# Create your models here.
class Suscription(models.Model):
    nombre_suscription = models.CharField(max_length=45)
    estado = models.BooleanField(default=True)
    dias_duracion = models.IntegerField()  # Duration in days
    
    def __str__(self):
        return self.nombre_subscription
