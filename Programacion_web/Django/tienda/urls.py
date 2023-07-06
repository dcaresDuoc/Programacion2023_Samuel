#from django.conf.urls import url   
from django.urls import path
from . import views


urlpatterns = [
    path ('provedores.html', views.provedores, name='provedores'),
    path('listadoSQL.html', views.listadoSQL, name='listadoSQL'),
    path('catalogo.html', views.catalogo, name='catalogo'),
    path('contacto.html', views.contacto, name='contacto'),
    path('foro.html', views.foro, name='foro'),
    path('Inicio.html', views.Inicio, name='Inicio'),
    path('login.html', views.login, name='login'),
    path('PP.html', views.PP, name='PP'),
    path('TC.html', views.TC, name='TC'),
    path('tiendas.html', views.tiendas, name='tiendas'),
   
    

]