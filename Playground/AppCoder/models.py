from django.db import models

class Curso(models.Model):

    nombre= models.CharField(max_length=20)
    comision= models.IntegerField()

class Estudiante(models.Model):

    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    email= models.EmailField()



