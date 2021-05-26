#Librerias
from django.shortcuts import render,HttpResponse,redirect

#Aqui se definen las funcionalidades del proyecto donde el retorno 
#consiste en redirigir a una template que consuma esa funcionalidad

#Definimos index como la pagina principal
def index(request):
    #No hace nada mas que redirigir a nuestra pagina principal
    return render(request,"index.html")


