from django.urls.conf import path
from . import views


urlpatterns = [
    path('tatinspizza.com',views.index),
    path('tatinspizza.com/registro',views.registro),
    path('tatinspizza.com/inicio_sesion',views.inicio_sesion),
    path('tatinspizza.com/menu',views.menu),
    path('tatinspizza.com/comida',views.comida),
    path('tatinspizza.com/busqueda',views.busqueda),
    #path('tatinspizza.com/resultado_busqueda',views.resultado_busqueda),
   #Cliente
    #path('tatinspizza.com/pedido',views.cuenta),
    path('tatinspizza.com/cuenta',views.cuenta),
    #path('tatinspizza.com/carrito',views.carrito),
    path('tatinspizza.com/boleta',views.boleta),
    path('tatinspizza.com/comentario',views.comentario),
    #Comida
    path('tatinspizza.com/clientes',views.monitoreo_cliente),
    path('tatinspizza.com/comidas',views.monitoreo_comidas),
    #path('tatinspizza.com/editar_cliente/<int:id>',views.editar_cliente),
    #path('tatinspizza.com/editar_comida/<int:id>',views.editar_comida),
   
   

]