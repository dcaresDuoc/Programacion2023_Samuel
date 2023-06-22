from django.shortcuts import render

def index(request):
    return render(request, 'Inicio.html')

def pagina1(request):
    return render(request, 'catalogo.html')

def pagina2(request):
    return render(request, 'contacto.html')

def pagina3(request):
    return render(request, 'foro.html')

def pagina4(request):
    return render(request, 'login.html')

def pagina5(request):
    return render(request, 'PP.html')

def pagina6(request):
    return render(request, 'TC.html')

def pagina7(request):
    return render(request, 'tiendas.html')
    