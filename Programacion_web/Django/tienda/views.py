from django.shortcuts import render

from .models import Provedor, Tipo

# Create your views here.


def provedores(request):
    provedors = Provedor.objects.all()   
    context={"provedors":provedors}
    return render(request, 'tienda/provedores.html', context)

def catalogo(request):
    context={}
    return render(request, 'tienda/catalogo.html', context )

def contacto(request):
    context={}
    return render(request, 'tienda/contacto.html', context )

def foro (request):
    context={}
    return render(request, 'tienda/foro.html', context )
def Inicio(request):
    context={}
    return render(request, 'tienda/Inicio.html', context )
def login(request):
    context={}
    return render(request, 'tienda/login.html', context )
def PP(request):
    context={}
    return render(request, 'tienda/PP.html', context )
def TC(request):
    context={}
    return render(request, 'tienda/TC.html', context )
def tiendas(request):
    context={}
    return render(request, 'tienda/tiendas.html', context )


def listadoSQL(request):
    provedors = Provedor.objects.raw('SELECT * FROM provedors_provedor')
    print(provedors)   
    context={"provedors":provedors}
    return render(request, 'tienda/listadoSQL.html', context)

