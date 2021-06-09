from django.urls.conf import path
from . import views


urlpatterns = [
    path('tatinspizza.com', views.index),
    path('tatinspizza.com/registro', views.registro),
    path('tatinspizza.com/inicio_sesion', views.inicio_sesion),
    path('tatinspizza.com/cerrar_sesion', views.cerrar_sesion),
    path('tatinspizza.com/menu',views.menu),
    path('tatinspizza.com/resultado_busqueda',views.resultado_busqueda),
    # Cliente
    path('tatinspizza.com/mi_perfil',views.mi_perfil),
    path('tatinspizza.com/carrito', views.carrito),
    path('tatinspizza.com/gracias', views.realizar_pedido),
    path('tatinspizza.com/comentario',views.comentario),
    # Comida
    path('tatinspizza.com/monitoreo_clientes',views.monitoreo_Usuario),
    path('tatinspizza.com/eliminar_cliente/<int:id>',views.eliminar_usuario),
    path('tatinspizza.com/monitoreo_comidas',views.monitoreo_comida),
    path('tatinspizza.com/editar_cliente/<int:id>',views.editar_usuario),
    path('tatinspizza.com/crear_comida',views.crear_comida),
    path('tatinspizza.com/editar_comida/<int:id>',views.editar_comida),
    path('tatinspizza.com/eliminar_comida/<int:id>',views.eliminar_comida),
    path('tatinspizza.com/agregar_al_carrito/<int:id>',views.agregar_al_carrito),
    path('tatinspizza.com/disminuir_al_carrito/<int:id>',views.disminuir_al_carrito),


]
