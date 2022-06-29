from django.db import models

# Create your models here.

class Mascotas(models.Model):
    
    animal = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    nombre = models.CharField(max_length=20)

class Dueños(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    DNI = models.IntegerField()
    mascota = models.CharField(max_length=30)

class Encargados(models.Model):

    nombre = models.CharField(max_length=30)
    DNI = models.IntegerField()
    telefono = models.IntegerField()