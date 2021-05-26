#Librerias
from django.contrib import admin
from django.urls import path,include 


urlpatterns = [
    #Con esta instruccion utilizaremos las rutas de nuestra /app
    path('',include('app.urls')),
]

