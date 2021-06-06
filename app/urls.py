from django.urls.conf import path
from . import views


urlpatterns = [
    path('tatinspizza.com', views.index),
    path('tatinspizza.com/registro', views.registro),
    path('tatinspizza.com/inicio_sesion', views.inicio_sesion),
    path('tatinspizza.com/cerrar_sesion', views.cerrar_sesion),
    path('tatinspizza.com/menu',views.menu),
    # path('tatinspizza.com/comida',views.comida),
    path('tatinspizza.com/resultado_busqueda',views.resultado_busqueda),
    # Cliente
    # path('tatinspizza.com/pedir',views.pedir),
    path('tatinspizza.com/mi_perfil',views.mi_perfil),
    path('tatinspizza.com/carrito', views.carrito),
    # path('tatinspizza.com/boleta',views.boleta),
    path('tatinspizza.com/comentario',views.comentario),
    # Comida
    # path('tatinspizza.com/clientes',views.monitoreo_cliente),
    # path('tatinspizza.com/editar_cliente/<int:id>',views.editar_cliente),
    # path('tatinspizza.com/editar_comida/<int:id>',views.editar_comida),
    path('tatinspizza.com/agregar_al_carrito/<int:id>',views.agregar_al_carrito),
    path('tatinspizza.com/disminuir_al_carrito/<int:id>',views.disminuir_al_carrito),


]
