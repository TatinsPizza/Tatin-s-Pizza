from django.urls.conf import path
from . import views


urlpatterns = [
    path('tatinspizza.com',views.index),
    path('tatinspizza.com/registro',views.registro),
    path('tatinspizza.com/inicio_sesion',views.inicio_sesion),
    path('tatinspizza.com/menu',views.menu),
    path('tatinspizza.com/comida',views.comida),
    path('tatinspizza.com/busqueda',views.busqueda),
    path('tatinspizza.com/resultado_busqueda',views.resultado_busqueda),
   #Cliente
    path('tatinspizza.com/pedir',views.pedir),
    path('tatinspizza.com/cuenta',views.cuenta),
    path('tatinspizza.com/carrito',views.carriento),
    path('tatinspizza.com/boleta',views.boleta),
    path('tatinspizza.com/comentario',views.comentario),
    #Comida
    path('tatinspizza.com/clientes',views.monitoreo_cliente),
    path('tatinspizza.com/editar_cliente/<id:int>',views.editar_cliente),
   

]