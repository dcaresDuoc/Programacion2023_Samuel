
from django.contrib import admin
from django.urls import path
from Mori.vista import index
from Mori.vista import pagina1
from Mori.vista import pagina2
from Mori.vista import pagina3
from Mori.vista import pagina4
from Mori.vista import pagina5
from Mori.vista import pagina6
from Mori.vista import pagina7


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('index/Inicio.html', index),
    path('index/catalogo.html', pagina1),
    path('index/contacto.html', pagina2),
    path('index/foro.html', pagina3),
    path('index/login.html', pagina4),
    path('index/PP.html', pagina5),
    path('index/tc', pagina6),
    path('index/tiendas.html', pagina7)
    
]
