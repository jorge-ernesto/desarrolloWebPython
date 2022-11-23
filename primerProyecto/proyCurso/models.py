from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=64,default='')
    precio = models.CharField(max_length=32,default='')
    nombreImagen = models.CharField(max_length=64,default='')
    descripion = models.CharField(max_length=512,default='')
    estado = models.CharField(max_length=64,default='')
    stock = models.CharField(max_length=32,default='')