from django.db import models
from django.utils import timezone


class Persona(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    #autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True ) #, blank=True, null=True
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    direccion=models.CharField(max_length=200, null=True)
    ubicacion=models.CharField(max_length=200, null=True)
    telefono=models.CharField(max_length=200, null=True)
    imagen=models.CharField(max_length=200, null=True)
    website = models.URLField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
