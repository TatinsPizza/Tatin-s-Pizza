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

# ----Usuario actual----


class Usuario_actual:
    id = 14
    logeado = True


usuario_actual = Usuario_actual()

# ----Carrito----
pedido = []
cantidad = []

# ----Visitante----
# Incompleto


# Incompleto
def mi_perfil(request):
    usuario = Usuario.objects.get(id_usuario=usuario_actual.id)

    contexto = {
        "usuario": usuario,
    }

    return render(request, "mi_perfil.html", contexto)



# ----Administrador----

def monitoreo_comidas(request):
    #Obtenemos todas las comidas desde la base de datos
    comidas = Comida.objects.all()
    #A traves del contexto enviaremos los datos
    contexto = {
        "comidas": comidas,
    }
    #Finalmente renderizaremos la template y enviaremos el contexto
    return render(request, "monitoreo_comidas.html", contexto)

def eliminar_comida(request,id):
    #Obtenemos todas la comida coincidente seguna la variable id del parametro
    comida = Comida.objects.get(id_comida = id)
    #Una vez obtenida la comida se procera a borrar
    comida.delete()
    #Una vez borrada redirigiremos hacia la siguiente direccion
    return redirect("/tatinspizza.com/monitoreo_comidas")

def crear_comida(request):
    # Todo lo que se encuentra en el apartado del "if" es lo que se hara
    # cuando se llegue a este metodo mediante el formulario
    if request.method == "POST":
         # guardamos todas las variables que venian en el formulario en variables propias
        # (el nombre de las variables que esta entre conchetes es el "name" que se les asigno en los input de la template )
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"]

        #En caso que se repita el nombre se rederigira a la misma direccion para volver a repetir el proceso
        if Comida.objects.filter(nombre=nombre).exists():
            return redirect("/tatinspizza.com/crear_comida")

        # si el metodo llego hasta aqui es porque se cumplieron las condiciones
        # asi que creamos una intancia de Comida y le asignamos sus respectivos atributos
        nueva_comida = Comida()
        nueva_comida.nombre = nombre
        nueva_comida.descripcion = descripcion
        nueva_comida.precio = precio
        #luego de asignados los datos lo guardaremos
        nueva_comida.save()

        #de completado el proceso se redirigira a la siguiente direccion
        return redirect("/tatinspizza.com/monitoreo_comidas")
    #en primera instancia se renderizara hacia la template
    return render(request,"crear_comida.html")

def editar_comida(request, id):
    # Todo lo que se encuentra en el apartado del "if" es lo que se hara
    # cuando se llegue a este metodo mediante el formulario
    if request.method == "POST":
         # guardamos todas las variables que venian en el formulario en variables propias
        # (el nombre de las variables que esta entre conchetes es el "name" que se les asigno en los input de la template )
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"]
        
        # si el metodo llego hasta aqui es porque se cumplieron las condiciones
        # asi que creamos una intancia de Comida y le asignamos sus respectivos atributos
        actualizar_comida = Comida.objects.get(id_comida=id)
        actualizar_comida.nombre = nombre
        actualizar_comida.descripcion = descripcion
        actualizar_comida.precio = precio
         #luego de asignados los datos lo guardaremos
        actualizar_comida.save()

        #de completado el proceso se redirigira a la siguiente direccion
        return redirect("/tatinspizza.com/monitoreo_comidas")
    #Obtenemos los datos de la comida coincidente segun el id como parametro
    comida = Comida.objects.get(id_comida=id)
    #Asignaremos la comida coincidente a un diccionario para enviar los datos hacia la template
    contexto = {
        "comida": comida,
    }
    #en primera instancia se renderizara hacia la template
    return render(request, "editar_comida.html", contexto)

# --Cliente--


def monitoreo_usuarios(request):
    #Obtenermos todas los usuarios de la Base de datos
    usuarios = Usuario.objects.all()
    #Atraves de este contexto enviaremos la informacion obtenida de los usuarios
    contexto = {
        "usuarios": usuarios,
    }
    #Finalmente renderizaremos la template enviandole el contexto
    return render(request, "monitoreo_usuarios.html", contexto)

def eliminar_usuario(request,id):
   #Obtenermos todas los usuarios de la Base de datos
    usuario = Usuario.objects.get(id_usuario = id)
    #Ya obtenido el usuario lo borraremos
    usuario.delete()
    #Luego de borrado rederigiremos hace la template
    return redirect("/tatinspizza.com/monitoreo_usuarios")

def editar_usuario(request, id):
    # Todo lo que se encuentra en el apartado del "if" es lo que se hara
    # cuando se llegue a este metodo mediante el formulario
    if request.method == "POST":
         # guardamos todas las variables que venian en el formulario en variables propias
        # (el nombre de las variables que esta entre conchetes es el "name" que se les asigno en los input de la template )
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        contrasena2 = request.POST["contrasena1"]
        contrasena1 = request.POST["contrasena2"]

        #si es que la contraseñas del formulario no son coincidentes se rederigirá de nuevo a la misma direccion sin permitir la edicion del usuario
        if contrasena1 != contrasena2:
            return redirect("/tatinspizza.com/editar_usuario/"+str(id))

         # si el metodo llego hasta aqui es porque se cumplieron las condiciones
        # asi que creamos una intancia de Comida y le asignamos sus respectivos atributos
        actualizar_usuario = Usuario.objects.get(id_usuario=id)
        actualizar_usuario.nombre = nombre
        actualizar_usuario.correo = correo
        actualizar_usuario.contrasena = contrasena1
        #luego guardaremos 
        actualizar_usuario.save()

        #Luego de editado el usuario se redirigira hacia la siguiente ruta
        return redirect("/tatinspizza.com/monitoreo_usuarios")

    #Obtenemos el usuario coincidente con el id del parametro
    usuario = Usuario.objects.get(id_usuario=id)
    #Asignaremos el usuario coincidente a un diccionario para enviar los datos hacia la template
    contexto = {
        "usuario": usuario,
    }
    #en primera instancia se renderizara hacia la template
    return render(request, "editar_usuario.html", contexto)

def boleta():

    #cliente que pide la comida
    comidas = ['churrasssco','Chacarero','Lomito','Bebida','Café']
    descripciones = [1233124,123123,123123,12312,123123]

    #Datos utilizados para obtener el tiempo y fecha donde se ha realizado la boleta
    ahora = datetime.now()
    fecha = ahora.strftime('%d/%m/%Y')
    hora = ahora.strftime('%H:%M')
    
    #Obtenemos la template donde tenemos nuestra estructura de la boleta
    template = get_template('../templates/boleta.html')
    #creamos un diccionario con los datos que queremos imprimir en la boleta
    context = {'title': 'primer titulo','comidas':comidas,'descripcion':'precios','subtotal':12312,'total':13123,'impuesto':1231, 'fecha':fecha,'hora':hora}
    html = template.render(context)

    #IMPORTANTE: parametro ruta es la ruta donde queremos guardar nuestra boleta temporal, 
    #en este caso será la ruta donde se encuentra el proyecto en una carpteta /temp
    RUTA = "C:/Users/javie/OneDrive/Python/Tatins_Pizza/app/temp"
    file = open(os.path.join(RUTA, str('boleta') + '.pdf'), "w+b")
    
    #Creamos la boleta con pisaStatus
    pisaStatus = pisa.CreatePDF(
        html,dest=file)

    pisaStatus = pisa.CreatePDF(html, dest=file, link_callback=template)
    
    #Utilizamos el metodo para enviar nuestra boleta por correo
    enviar_boleta(RUTA,'r.millanao02@ufromail.cl')
   
    #validacion de un error
    if pisaStatus.err:
        return HttpResponse('Error <pre>',html,'</pre>')


def enviar_boleta(RUTA,correo):
    #IMPORTANTE: parametro ruta es la ruta donde queremos guardar nuestra boleta temporal, 
    #en este caso será la ruta donde se encuentra el proyecto en una carpteta /temp

    #Datos usados para enviar gmail
    remitente = 'tatinspizza@gmail.com'
    destinatario = correo
    asunto = '[Boleta] Tatin´s Pizza'
    cuerpo = 'Muchas Gracias por preferir Tatin´s Pizza, A continuacion adjuntamos su boleta:'

    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
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
    sesion_smtp.sendmail(remitente, destinatario, texto)
    # Cerramos la conexión
    sesion_smtp.quit()

def enviar_bienvenida(correo):
    remitente = 'tatinspizza@gmail.com'
    destinatario = correo
    asunto = '[Bienvenida]'
    cuerpo = 'Bienvenido/a a Tatin´s Pizza, se ha registrado como usuario en nuestra sistema web. Lo invitamos cordialmente a desgustar nuestros famosas pizzas\nAtte. Tatin´s Pizza Workers'
    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Ciframos la conexión
    sesion_smtp.starttls()
    # Iniciamos sesión en el servidor con el correo y contraseña
    sesion_smtp.login('tatinspizza@gmail.com','laspizzadeltatin')
    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()
    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatario,texto)
    # Cerramos la conexión
    sesion_smtp.quit()