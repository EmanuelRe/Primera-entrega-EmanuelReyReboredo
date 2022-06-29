from itertools import product
from urllib import request
from django.shortcuts import render, HttpResponse
from App.models import *
from App.forms import *

# Create your views here.

def inicio(request):

    return render(request, "App/inicio.html")

def mascotas(request):

    if request.method == 'POST':

        miFormulario = FormularioMascotas(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            mascota = Mascotas(animal=info['animal'], raza=info['raza'], nombre=info['nombre'])
            mascota.save()

            return render(request, "App/inicio.html")
    else:
        miFormulario = FormularioMascotas()

    return render(request, "App/mascotas.html", {"miFormulario":miFormulario})

def dueños(request):

    if request.method == 'POST':

        miFormulario = FormularioDueños(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            dueño = Mascotas(nombre=info['nombre'], apellido=info['apellido'], DNI=info['DNI'],mascota=info["mascota"])
            dueño.save()

            return render(request, "App/inicio.html")
    else:
        miFormulario = FormularioDueños()

    return render(request, "App/dueños.html", {"miFormulario":miFormulario})

def encargados(request):

    if request.method == 'POST':

        miFormulario = FormularioEncargados(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            encargado = Encargados(nombre=info['nombre'], DNI=info['DNI'], telefono=info['telefono'])
            encargado.save()

            return render(request, "App/inicio.html")
    else:
        miFormulario = FormularioEncargados()

    return render(request, "App/encargados.html", {"miFormulario":miFormulario})

def buscar(request):

    if request.GET['resultado']:

        mascotas = mascotas.objects.filter(productos__icontains=mascotas)
        print(mascotas)
    
        return render(request, "App/inicio.html", {"mascotas":mascotas.values,"prd":mascotas})
    
    else:

        respuesta = "Sin datos"

    return render(request, "App/inicio.html", {"prd":respuesta})

