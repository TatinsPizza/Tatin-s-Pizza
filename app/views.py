from app.models import Comentario, Comida, Usuario
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
#Librerias PDF
from django.template.loader import get_template
from xhtml2pdf import pisa
import smtplib 
import smtplib
from django.conf import settings
from datetime import date
from datetime import datetime
#Librerias Email
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


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
    comidas = ['churrasssco','Chacarero','Lomito','Bebida','Café']
    descripciones = [1233124,123123,123123,12312,123123]

    ahora = datetime.now()
    fecha = ahora.strftime('%d/%m/%Y')
    hora = ahora.strftime('%H:%M')
    
    template = get_template('../templates/boleta.html')
    context = {'title': 'primer titulo','comidas':comidas,'descripcion':'precios','subtotal':12312,'total':13123,'impuesto':1231, 'fecha':fecha,'hora':hora}
    html = template.render(context)

    RUTA = "C:/Users/javie/OneDrive/Python/Tatins_Pizza/app/temp"
    file = open(os.path.join(RUTA, str('boleta') + '.pdf'), "w+b")
  
    pisaStatus = pisa.CreatePDF(
        html,dest=file)

    pisaStatus = pisa.CreatePDF(html, dest=file, link_callback=template)
 
    getCorreo(RUTA)
   
    if pisaStatus.err:
        return HttpResponse('Error <pre>',html,'</pre>')

    
    return render(request,"boleta_impresa.html")
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

def getCorreo(RUTA):
    remitente = 'tatinspizza@gmail.com'
    destinatarios = ['r.millanao02@ufromail.cl',]
    asunto = '[Boleta] Tatin´s Pizza'
    cuerpo = 'Muchas Gracias por preferir Tatin´s Pizza, A continuacion adjuntamos su boleta:'

    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    
    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open('C:/Users/javie/Desktop/tatinbd.png', 'rb')
    
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload(open(RUTA+str("/boleta.pdf"), "rb").read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= {0}".format(os.path.basename(RUTA+str("/boleta.pdf"))))
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)
    
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Ciframos la conexión
    sesion_smtp.starttls()

    # Iniciamos sesión en el servidor con el correo y contraseña
    sesion_smtp.login('tatinspizza@gmail.com','laspizzadeltatin')

    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()

    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatarios, texto)

    # Cerramos la conexión
    sesion_smtp.quit()