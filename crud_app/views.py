from django.shortcuts import render, redirect
from .models import Persona
# Create your views here.


def index(request):
    if request.method == 'POST':
        nombre_completo = request.POST['nombre_completo'].upper()
        peso = request.POST['peso']
        talla = request.POST['talla']
        Persona.objects.create(
            nombre_completo = nombre_completo,
            peso = peso,
            talla = talla
        )
        return redirect('/')

    else:
        personas = Persona.objects.all().order_by('id')
        return render(request, 'index.html',{'personas':personas})
    

def ver_persona(request, id):
    persona = Persona.objects.get(id=id)
    return render(request, 'editar.html', {'persona':persona})

def editar_persona(request):
    persona = Persona.objects.filter(id = request.POST['id'])
    peso = request.POST['peso']
    talla = request.POST['talla']
    persona.update(
        peso = peso,
        talla = talla
    )
    return redirect('/')


def eliminar(request, id):
    Persona.objects.filter(id = id).delete()
    return redirect('/')


def inicio_test(request):
    return render(request, 'inicio_test.html')

def acerca_test(request):
    return render(request, 'acerca.html')


