from django.urls.conf import path
from . import views


urlpatterns = [
    path('tatinspizza.com',views.index,name='index'),
    path('tatinspizza.com/comentarios',views.comentario,name='comentario'),
    path('tatinspizza.com/registro',views.registro,name='registro'),
    
]