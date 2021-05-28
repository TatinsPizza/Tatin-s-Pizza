from app.models import Comentario, Comida, Usuario
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.conf import settings

from datetime import date
from datetime import datetime

#----Usuario actual----
class Usuario_actual:
	id = 0
	logeado = False

usuario_actual = Usuario_actual()

#----Visitante----
#Incompleto
def index(request):
    return render(request,"index.html")

#Casi-Completo (falta verificacion de correo)
def registro(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]

        if Usuario.objects.filter(correo = correo).exist():
            return redirect("tatinspizza.com/registro")

        nuevo_usuario = Usuario()
        nuevo_usuario.nombre = nombre
        nuevo_usuario.correo = correo
        nuevo_usuario.contrasena = contrasena
        nuevo_usuario.save()

        return redirect("tatinspizza.com/inicio_sesion")
    
    return render(request,"registro.html")

#Incompleto (falta redirijir al iniciar sesion)
def inicio_sesion(request):
    if request.method == "POST":
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]

        if Usuario.objects.filter(correo = correo,contrasena = contrasena).exists():
            usuario = Usuario.objects.get(correo = correo)
            usuario_actual.id = usuario.id_usuario
            usuario_actual.logeado = True

            return redirect("")

    return render(request,"inicio_sesion.html")

#Completo
def menu(request):
    comidas = Comida.objects.all()

    contexto = {
        "comidas" : comidas,
    }

    return render(request,"menu.html",contexto)

#Completo
def comida(request,id):
    comida = Comida.objects.get(id_comida = id)

    contexto = {
        "comida" : comida,
    }

    return render(request,"comida.html",contexto)

#completo
def busqueda(request):
    return render(request,"comida.html")

#Completo
def resultado_busqueda(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]

        comidas = Comida.objects.filter(nombre__icontains=nombre)

        contexto = {
            "comidas" : comidas,
        }

        return render(request,"resultado_busqueda.html",contexto)

    return redirect("tatinspizza.com/busqueda")


#----Cliente----

#Incompleto
def pedir(request,id):
    return render(request,"pedir.html")

#Incompleto
def cuenta(request,id):
    return render(request,"cuenta.html")

#Incompleto
def carrito(request,id):
    return render(request,"carrito.html")

#Incompleto
def boleta(request):
    #Provisorio
    comidas = ['Lomito a lo pobre','Chacarero','Lomito','Bebida','Café']
    descripciones = [1233124,123123,123123,12312,123123]

    ahora = datetime.now()
    fecha = ahora.strftime('%d/%m/%Y')
    hora = ahora.strftime('%H:%M')
    
    template = get_template('../templates/boleta.html')
    context = {'title': 'primer titulo','comidas':comidas,'descripcion':'precios','subtotal':12312,'total':13123,'impuesto':1231, 'fecha':fecha,'hora':hora}
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment;filename="report.pdf"'
   
    pisaStatus = pisa.CreatePDF(
        html, dest=response)
   
    if pisaStatus.err:
        return HttpResponse('Error <pre>',html,'</pre>')
    return response
#Casi-Completo
def comentario(request):
    if request.method == "POST":
        usuario = Usuario.objects.get(id_usuario = usuario_actual.id)
        comentario = request.POST["comentario"]
        


        nuevo_comentario = Comentario()
        nuevo_comentario.comentario = comentario
        nuevo_comentario.usuario = usuario
        nuevo_comentario.save()

        return redirect("tatinspizza.com/comentarios")

    comentarios = Comentario.objects.all()

    contexto = {
        "comentarios" : comentarios,
    }

    return render(request,"comentarios.html",contexto)


#----Administrador----

#--Comida--
def monitoreo_comida(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        ingredientes = request.POST["ingredientes"]
        precio = request.POST["precio"]
        

        nueva_comida = Comida()
        nueva_comida.nombre= nombre
        nueva_comida.descripcion = descripcion
        nueva_comida.ingredientes = ingredientes
        nueva_comida.precio = precio
        nueva_comida.save()

        return redirect("tatinspizza.com/monitoreo_comidas")

    comidas = Comida.objects.all()

    contexto = {
        "comidas" : comidas,
    }

    return render(request,"monitoreo_comidas.html",contexto)

def editar_comida(request,id):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        ingredientes = request.POST["ingredientes"]
        precio = request.POST["precio"]


        actualizar_comida = Comida.objects.get(id_comida = id)
        actualizar_comida.nombre= nombre
        actualizar_comida.descripcion = descripcion
        actualizar_comida.ingredientes = ingredientes
        actualizar_comida.precio = precio
        actualizar_comida.save()
        return redirect("tatinspizza.com/monitoreo_comidas")


    comida = Comida.objects.get(id_comida = id)

    contexto = {
        "comida" : comida,
    }

    return render(request,"editar_comida.html",contexto)

#--Cliente--

def monitoreo_cliente(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]

        nuevo_usuario = Usuario()
        nuevo_usuario.nombre = nombre
        nuevo_usuario.correo = correo
        nuevo_usuario.contrasena = contrasena
        nuevo_usuario.save()
        
        return redirect("tatinspizza.com/monitoreo_clientes")

    clientes = Usuario.objects.all()

    contexto = {
        "clientes" : clientes,
    }

    return render(request,"monitoreo_clientes.html",contexto)

def editar_cliente(request,id):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]

        actualizar_usuario = Usuario.objects.get(id_usuario = id)
        actualizar_usuario.nombre = nombre
        actualizar_usuario.correo = correo
        actualizar_usuario.contrasena = contrasena
        actualizar_usuario.save()

        return redirect("tatinspizza.com/monitoreo_clientes")

    cliente = Usuario.objects.get(id_usuario = id)

    contexto = {
        "cliente" : cliente,
    }

    return render(request,"editar_cliente.html",contexto)
