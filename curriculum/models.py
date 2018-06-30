from django.db import models
from django.utils import timezone



class Estudio(models.Model):
    carrera= models.CharField(max_length=200)
    lugar= models.CharField(max_length=200)
    comienzo = models.DateTimeField(
            default=timezone.now)
    fin = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return ""

class Experiencia(models.Model):
    trabajo= models.CharField(max_length=200)
    descripcion=models.TextField()
    lugar= models.CharField(max_length=200)
    comienzo = models.DateTimeField(
            default=timezone.now)
    fin = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return ""

class Redes(models.Model):
    inicio= models.CharField(max_length=200)
    icono=models.CharField(max_length=200)

    def __str__(self):
        return ""


class Intereses(models.Model):
    interes= models.CharField(max_length=200)
    icono=models.CharField(max_length=200)

    def __str__(self):
        return ""



