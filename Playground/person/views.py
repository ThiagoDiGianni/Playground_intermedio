from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def  list_person(request):

    persons = person.objects.all()
    context = {'person':persons }
    return render(request,'index.html',context)


def papa(self):
    papa= person(name="Miguel",surname="Di Gianni",age=57)
    papa.save()
    texto= f"Nombre: {papa.name} Apellido: {papa.surname} Edad: {papa.age} "
    return HttpResponse(texto)


def inicio(request):
    
    return render(request, "person/inicio.html")