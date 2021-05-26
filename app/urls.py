#Librerias
from django.urls import path,include
from . import views

#Aqui se encuentran todas la urls de nuestro proyecto,
#su objetivo es dirigir de la ruta hacia views.py 

urlpatterns = [
    #pagina principal
    path('tatinspizza.com',views.index,name='index'),
]


