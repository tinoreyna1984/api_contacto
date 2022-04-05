from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fono = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    fecha_nac = models.CharField(max_length=200, blank=True, null=True)
