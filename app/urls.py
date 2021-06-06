from django.urls.conf import path
from . import views


urlpatterns = [
    #path('tatinspizza.com',views.index),
    #path('tatinspizza.com/registro',views.registro),
    #path('tatinspizza.com/inicio_sesion',views.inicio_sesion),
    #path('tatinspizza.com/menu',views.menu),
    #path('tatinspizza.com/comida',views.comida),
    #path('tatinspizza.com/busqueda',views.busqueda),
    #path('tatinspizza.com/resultado_busqueda',views.resultado_busqueda),
   #Cliente
    #path('tatinspizza.com/pedido',views.cuenta),
    path('tatinspizza.com/mi_perfil',views.mi_perfil),
    #path('tatinspizza.com/carrito',views.carrito),
    path('tatinspizza.com/boleta',views.boleta),
    #path('tatinspizza.com/comentario',views.comentario),
    #Comida
    
    path('tatinspizza.com/monitoreo_usuarios',views.monitoreo_usuarios),
    path('tatinspizza.com/eliminar_usuario/<int:id>',views.eliminar_usuario),
    path('tatinspizza.com/comidas',views.monitoreo_comidas),
    path('tatinspizza.com/editar_usuario/<int:id>',views.editar_usuario),
    path('tatinspizza.com/editar_comida/<int:id>',views.editar_comida),
   
   

]