from django.http.response import HttpResponse
from app.models import Comentario, Comida, Usuario, Pedido, Usuario_Pedido, Pedido_Comida
from django.shortcuts import redirect, render
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse

# Librerias PDF
from django.template.loader import get_template
from xhtml2pdf import pisa
import smtplib
from django.conf import settings
from datetime import date
from datetime import datetime
# Librerias Email
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ----Usuario actual----
# Esta clase es creada con el fin de saber que usuario se encuentra logeado
# y asi porder permitir o no el ingreso a ciertas paginas


class Usuario_actual:
    id = 0
    logeado = False


# Intanciamos un objeto de la clase anterior
usuario_actual = Usuario_actual()

# Metodos verificacion permisos

# Nos retorna si el usuario esta logueado
def isLogeado():
    return usuario_actual.logeado

# Nos retorna si el usuario es admin
def isAdmin():
    usuario = Usuario.objects.get(id_usuario=usuario_actual.id)
    return usuario.isadmin()


# ----Carrito----
# Esta clase nos ayudara a llevar la cuenta de cuales son las comidas que
# fueron pedidas por el Usuario y sus respectivas cantidades


class Carrito:
    def __init__(self, comida):

        self.comida = comida
        self.cantidad = 1
        self.total = self.comida.precio


# Instanciamos un arreglo que usaremos para guardar los elementos del carrito
carrito_actual = []


# ----Visitante----

def index(request):

    # Este metodo se encarga de todo lo que ocurre en la pagina principal de nuestro proyecto

    # Obtenemos todos los comentarios desde la Base de datos
    comentarios = Comentario.objects.all()

    if not isLogeado():
        Admin = False
    else:
        Admin = isAdmin()

    # ahora creamos un diccionarioque contiene  tanto los comentarios como
    # una variable que usaremos para condicionar el html
    contexto = {
        "comentarios": comentarios,
        "isLogged": isLogeado(),
        "isAdmin": Admin

    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "index.html", contexto)


def registro(request):
    # Este metodo se encargara de todo lo que conlleva Registrar un nuevo usuario

    # Todo lo que se encuentra en el apartado del "if" es lo que se hara
    # cuando se llegue a este metodo mediante el formulario
    if request.method == "POST":
        # guardamos todas las variables que venian en el formulario en variables propias
        # (el nombre de las variables que esta entre conchetes es el "name" que se les asigno en los input de la template )
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        contrasena1 = request.POST["contrasena1"]
        contrasena2 = request.POST["contrasena2"]

        # Realizamos una comprobacion para asegurarnos de que no se repita el correo y que la contraseña que desea el usuario sea la correcta
        if Usuario.objects.filter(correo=correo).exists() or contrasena1 != contrasena2:
            # en caso de no cumplirce estas condiciones se le redirecciona de vuelta a el formulario
            return redirect("/tatinspizza.com/registro")

        # si el metodo llego hasta aqui es porque se cumplieron las condiciones
        # asi que creamos una intancia de Usuario y le asignamos sus respectivos atributos
        nuevo_usuario = Usuario()
        nuevo_usuario.nombre = nombre
        nuevo_usuario.correo = correo
        nuevo_usuario.contrasena = contrasena1
        # con el metodo ".save()" es que se guardan los objetos en la base de datos
        nuevo_usuario.save()
        # y ahora nos encargamos de cargar los datos del usuario actual y señalar que se encuentra logeado
        usuario_actual.id = nuevo_usuario.id_usuario
        usuario_actual.logeado = True

        # redireccionamos a la pagina principal
        return redirect("/tatinspizza.com")
    
    if not isLogeado():
        Admin = False
    else:
        Admin = isAdmin()

    # esto ocurre cuando no se llega a este metodo mediante redireccionamiento y no por un formulario
    # creamos el diccionario que contendra la variable que nos ayudara a condicionar el template
    contexto = {
        "isLogged": isLogeado(),
        "isAdmin": Admin
    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "registro.html", contexto)


def inicio_sesion(request):
    # Todo lo que se encuentra en el apartado del "if" es lo que se hara
    # cuando se llegue a este metodo mediante el formulario
    if request.method == "POST":
        # guardamos todas las variables que venian en el formulario en variables propias
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]

        # Comprobamos que tanto el correo como la contraseña sean correctas
        if Usuario.objects.filter(correo=correo, contrasena=contrasena).exists():
            # De ser correctas cargamos los datos del usuario actual y señalamos que se encuentra logueado
            usuario = Usuario.objects.get(correo=correo)
            usuario_actual.id = usuario.id_usuario
            usuario_actual.logeado = True

            # redireccionamos a la pagina principal
            return redirect("/tatinspizza.com")
    # esto ocurre cuando no se llega a este metodo mediante redireccionamiento y no por un formulario

    if not isLogeado():
        Admin = False
    else:
        Admin = isAdmin()

    # creamos el diccionario que contendra la variable que nos ayudara a condicionar el template
    contexto = {
        "isLogged": isLogeado(),
        "isAdmin" : Admin
    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "inicio_sesion.html", contexto)


def cerrar_sesion(request):
    # Este metodo se encarga de quitar los datos de usaurio que se encontraba activo
    # y señalar que ya no hay un usuario logueado
    usuario_actual.id = 0
    usuario_actual.logeado = False

    # redireccionamos a la pagina principal
    return redirect("/tatinspizza.com")


def menu(request):
    # Este metodo se encargara de cargar la template y los datos necesarios
    # para mostrar el menu del cual dispone nuestro proyecto

    # Obtenemos todas la comidas desde la Base de datos
    comidas = Comida.objects.all()

    if not isLogeado():
        Admin = False
    else:
        Admin = isAdmin()

    # ahora creamos un diccionario que contiene  tanto las comidas como
    # una variable que usaremos para condicionar el html
    contexto = {
        "comidas": comidas,
        "isLogged": isLogeado(),
        "isAdmin": Admin
    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "menu.html", contexto)


def resultado_busqueda(request):
    # Este  metodo se encarga tanto de encontrar lo que el usario desea como de enviarlo a una
    # template donde pueda ser visualizado

    # Cuanto se llegue mediante el formulario
    if request.method == "POST":
        # guardamos en variables propias
        nombre = request.POST["nombre"]

        # Filtramoslas comidas en base a lo ingresado por el usaurio
        comidas = Comida.objects.filter(nombre__icontains=nombre)

        if not isLogeado():
            Admin = False
        else:
            Admin = isAdmin()

        # Creamos un diccionario que lleva tanto los resultados de la busqueda como
        # la variable que siempre usarmos para condicionar los templates
        contexto = {
            "resultados": comidas,
            "isLogged": isLogeado(),
            "isAdmin": Admin
        }

        # Ahora renderizamos una template y le enviamos el diccionario con los datos
        return render(request, "resultado_busqueda.html", contexto)

    # en caso de que no se llegue mediante el formulario se le redireccionara a la pagina principal
    return redirect("/tatinspizza.com")


# ----Cliente----

def mi_perfil(request):

    #Verificamos que el usuario este logueado (si no lo esta lo redirigimos a la pagina principal)
    if not isLogeado():
        return redirect("/tatinspizza.com")

    # Este metodo se encarga de enviarnos a una template donde el usuario pueda visualizar sus datos

    # obtenemos los datos del usuario logueados
    usuario = Usuario.objects.get(id_usuario=usuario_actual.id)

    # creamos un diccionario para enviar los datos y los condicionales(booleanos)
    contexto = {
        "usuario": usuario,
        "isLogged": isLogeado(),
        "isAdmin": isAdmin()

    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "mi_perfil.html", contexto)


def carrito(request):
    #Verificamos que el usuario este logueado (si no lo esta lo redirigimos a la pagina principal)
    if not isLogeado():
        return redirect("/tatinspizza.com")

    # Este metodo nos redirecciona a el carrito de compras y nos muestra lo que contiene


    # creamos un diccionario que contiene el arreglo de todo lo que hay en el carrito
    # y nuestras variables condicionales
    contexto = {
        "carrito": carrito_actual,
        "isLogged": isLogeado(),
        "isAdmin": isAdmin()
    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "carrito.html", contexto)


def agregar_al_carrito(request, id):
    #Verificamos que el usuario este logueado (si no lo esta lo redirigimos a la pagina principal)
    if not isLogeado():
        return redirect("/tatinspizza.com")

    # Este metodo se encarga de agregar comidas al carrito y si esta ya existen les incrementa en uno su cantidad

    # Obtenemos la comida que se nos solicito ingresar
    comida = Comida.objects.get(id_comida=id)

    # Recorremos nuestro carrito
    for carrito in carrito_actual:
        # Si la comida ya se encuentra en el arreglo
        if carrito.comida == comida:
            # obtenmos su indice
            indice = carrito_actual.index(carrito)
            # aumentamos su cantidad en 1
            carrito.cantidad += 1
            carrito.total += carrito.comida.precio

            # y redireccionamos al carrito
            return redirect("/tatinspizza.com/carrito")

    # En caso de o encontrarce la comida en el arreglo creamos una nueva instancia de carrito
    # y que esta contenga la comida deseada
    nuevo_carrito = Carrito(comida)
    # ahora la agregamos a nuestro arreglo de carrito
    carrito_actual.append(nuevo_carrito)
    # (para ver en que consiste este tipo de objeto vea el principio del archivo)

    # finalmente redirigimos a el menu
    return redirect("/tatinspizza.com/menu")


def disminuir_al_carrito(request, id):
    #Verificamos que el usuario este logueado (si no lo esta lo redirigimos a la pagina principal)
    if not isLogeado():
        return redirect("/tatinspizza.com")

    # Este metodo lo usamos para disminuir la cantidad de cierta comida o eliminarla en caso de que llegue a 0

    # Obtenemos la comida a la que se nos solicito modificar su cantidad
    comida = Comida.objects.get(id_comida=id)

    # Recorremos nuestro carrito
    for carrito in carrito_actual:
        # Si encontramos la comida y su cantidad es mayor a 1
        if carrito.comida == comida and carrito.cantidad > 1:
            # disminuimos en uno la cantidad
            carrito.cantidad -= 1
            carrito.total -= carrito.comida.precio

        # Si no si encontramos la comida y su cantidad es igual a 1
        elif carrito.comida == comida and carrito.cantidad == 1:
            # obtenemos su indice
            indice = carrito_actual.index(carrito)
            # y la eliminamos
            carrito_actual.pop(indice)

    # Finalmente redireccionamos de vuelta a carrito
    return redirect("/tatinspizza.com/carrito")


def comentario(request):
    # Este Metodo resibe los datos del formulario existente en la template index

    #Verificamos que el usuario este logueado (si no lo esta lo redirigimos a la pagina principal)
    if not isLogeado():
        return redirect("/tatinspizza.com")
    

    if request.method == "POST":
        # Obtenemos el usuario actual
        usuario = Usuario.objects.get(id_usuario=usuario_actual.id)
        # Obtenemos el texto del formulario y lo coloco en variables propias
        texto = request.POST["texto"]

        # instanciamos un nuevo comentario
        nuevo_comentario = Comentario()
        # le asignanamos su texto
        nuevo_comentario.texto = texto
        # le asignamos su usuario
        nuevo_comentario.usuario = usuario
        # lo guardamos en la base de datos
        nuevo_comentario.save()

    # Redirecionamos a la pagina principal
    return redirect("/tatinspizza.com")


# ----Administrador----

# --Comida--
def monitoreo_comida(request):
    #Verificamos que el usuario este logueado y es admin (si no lo redirigimos a la pagina principal)
    if not isLogeado() or not isAdmin():
        return redirect("/tatinspizza.com")
    # Este metodo nos llevara a una tenplate en donde se encuentran todas la comidas
    # y podremos realizar diferentes acciones

    # Tomamos todas las comidas de la base de datos
    comidas = Comida.objects.all()


    # Creamos un diccionario par a enviar tanto las comidas como las variables que nos
    # ayuda a condicionar las templates
    contexto = {
        "comidas": comidas,
        "isLogged": isLogeado(),
        "isAdmin": isAdmin()

    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "monitoreo_comidas.html", contexto)


def eliminar_comida(request, id):
    #Verificamos que el usuario este logueado y es admin (si no lo redirigimos a la pagina principal)
    if not isLogeado() or not isAdmin():
        return redirect("/tatinspizza.com")

    # Metodo para eliminar una comida en base a su id

    # Obtenemos todas la comida coincidente seguna la variable id del parametro
    comida = Comida.objects.get(id_comida=id)
    # Una vez obtenida la comida se procera a borrar
    comida.delete()

    # redireccionamos de vuelta el Monitoreo de comidas
    return redirect("/tatinspizza.com/monitoreo_comidas")


def crear_comida(request):
    # Metodo para agregar una comida a nuestra base de datos

    #Verificamos que el usuario este logueado y es admin (si nolo redirigimos a la pagina principal)
    if not isLogeado() or not isAdmin():
        return redirect("/tatinspizza.com")

    # Todo lo que se encuentra en el apartado del "if" es lo que se hara
    # cuando se llegue a este metodo mediante el formulario
    if request.method == "POST":
        # guardamos todas las variables que venian en el formulario en variables propias
        # (el nombre de las variables que esta entre conchetes es el "name" que se les asigno en los input de la template )
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"]

        # En caso que se repita el nombre se rederigira a la misma direccion para volver a repetir el proceso
        if Comida.objects.filter(nombre=nombre).exists():
            return redirect("/tatinspizza.com/crear_comida")

        # si el metodo llego hasta aqui es porque se cumplieron las condiciones
        # asi que creamos una intancia de Comida y le asignamos sus respectivos atributos
        nueva_comida = Comida()
        nueva_comida.nombre = nombre
        nueva_comida.descripcion = descripcion
        nueva_comida.precio = precio
        # luego de asignados los datos lo guardaremos
        nueva_comida.save()

        # de completado el proceso se redirigira a la siguiente direccion
        return redirect("/tatinspizza.com/monitoreo_comidas")

    # Obtenemos si el usuario es admin (para los parametros de nav en la template)
    
    contexto = {
        "isLogged": isLogeado(),
        "isAdmin": isAdmin()
    }
    # en primera instancia se renderizara hacia la template
    return render(request, "crear_comida.html", contexto)


def editar_comida(request, id):
    #Verificamos que el usuario este logueado y es admin (si no lo redirigimos a la pagina principal)
    if not isLogeado() or not isAdmin():
        return redirect("/tatinspizza.com")

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
        # luego de asignados los datos lo guardaremos
        actualizar_comida.save()

        # Luego de creada se redirecciona de vuelta  monitoreo comidas
        return redirect("/tatinspizza.com/monitoreo_comidas")

    # Obtenemos la camina de que actualizara
    comida = Comida.objects.get(id_comida=id)

    # creamos un diccionario para enviar tanto la comiva como la variable condicional
    contexto = {
        "comida": comida,
        "isLogged": isLogeado(),
        "isAdmin": isAdmin()
    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "editar_comida.html", contexto)

# --Cliente--


def monitoreo_Usuario(request):
    # Metodo para redirigirnos a una template que permitira realiza acciones con los usuarios

    #Verificamos que el usuario este logueado y es admin (si no lo redirigimos a la pagina principal)
    if not isLogeado() or not isAdmin():
        return redirect("/tatinspizza.com")

    # obtenemos todos los usuarios de la base de datos
    usuarios = Usuario.objects.all()

    # creamos un diccionario para enviarle los usuarios y la variable condicional
    contexto = {
        "usuarios": usuarios,
        "isLogged": isLogeado(),
        "isAdmin": isAdmin()
    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "monitoreo_usuario.html", contexto)


def editar_usuario(request, id):
    # Metodo para poder modificar usuarios

    #Verificamos que el usuario este logueado (si no lo esta lo redirigimos a la pagina principal)
    if not isLogeado():
        return redirect("/tatinspizza.com")

    # Todo lo que se encuentra en el apartado del "if" es lo que se hara
    # cuando se llegue a este metodo mediante el formulario
    if request.method == "POST":
        # tomamos las variables del formulario y las asignamos a locales
        # (el nombre de las variables que esta entre conchetes es el "name" que se les asigno en los input de la template )
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        contrasena2 = request.POST["contrasena1"]
        contrasena1 = request.POST["contrasena2"]

        # si es que la contraseñas del formulario no son coincidentes se rederigirá de nuevo a la misma direccion sin permitir la edicion del usuario
        if contrasena1 != contrasena2:
            return redirect("/tatinspizza.com/editar_cliente/"+str(id))

        # si el metodo llego hasta aqui es porque se cumplieron las condiciones
        # asi que traemos la instancia de Comida  desde  la base de datos
        actualizar_usuario = Usuario.objects.get(id_usuario=id)
        # y sutituimos sus atributos
        actualizar_usuario.nombre = nombre
        actualizar_usuario.correo = correo
        actualizar_usuario.contrasena = contrasena1
        # lo guardamos en la base de datos
        actualizar_usuario.save()

        # Luego de editado el usuario se redirigira hacia la siguiente ruta
        return redirect("/tatinspizza.com/monitoreo_clientes")

    # Obtenemos el usuario coincidente con el id del parametro
    usuario = Usuario.objects.get(id_usuario=id)

    # creamos un  diccionario para enviar tanto el usuario como la variable condicional
    contexto = {
        "usuario": usuario,
        "isLogged": isLogeado(),
        "isAdmin": isAdmin(),

    }

    # en primera instancia se renderizara hacia la template
    return render(request, "editar_usuario.html", contexto)


def eliminar_usuario(request, id):
    #Verificamos que el usuario este logueado y es admin (si no lo redirigimos a la pagina principal)
    if not isLogeado() or not isAdmin():
        return redirect("/tatinspizza.com")

   # Obtenermos todas los usuarios de la Base de datos
    usuario = Usuario.objects.get(id_usuario=id)
    # Ya obtenido el usuario lo borraremos
    usuario.delete()
    # Luego de borrado rederigiremos hace la template
    return redirect("/tatinspizza.com/monitoreo_clientes")


def realizar_pedido(request):
    #Verificamos que el usuario este logueado (si no lo esta lo redirigimos a la pagina principal)
    if not isLogeado() or not carrito_actual:
        return redirect("/tatinspizza.com")



    # Obtenemos el usuario que se encuentra logueado
    usuario = Usuario.objects.get(id_usuario=usuario_actual.id)
    total = 0

    # Creamos un nuevo Pedido
    nuevo_pedido = Pedido()
    # Lo guardamos
    nuevo_pedido.save()

    # Creamos una nueva relacion Usuario_Pedido
    nuevo_usuario_pedido = Usuario_Pedido()
    # Le asignamos el usuario
    nuevo_usuario_pedido.usuario = usuario
    # Le asignamos el pedido
    nuevo_usuario_pedido.pedido = nuevo_pedido
    # Lo guardamos
    nuevo_usuario_pedido.save()

    # Recorremos nuestro carrito
    for carrito in carrito_actual:
        # y segun la cantidad de cada comida
        for i in range(carrito.cantidad):
            # Creamos una nueva relacion Pedido_Comida
            total += carrito.comida.precio
            nuevo_pedido_comida = Pedido_Comida()
            # Le asignamos el Pedido
            nuevo_pedido_comida.pedido = nuevo_pedido
            # Le asignamos la comida
            nuevo_pedido_comida.comida = carrito.comida
            # Lo guardamos
            nuevo_pedido_comida.save()

    # Datos utilizados para obtener el tiempo y fecha donde se ha realizado la boleta
    ahora = datetime.now()
    fecha = ahora.strftime('%d/%m/%Y')
    hora = ahora.strftime('%H:%M')

    # Obtenemos la template donde tenemos nuestra estructura de la boleta
    template = get_template('../templates/boleta.html')
    # creamos un diccionario con los datos que queremos imprimir en la boleta

    subtotal = round(total / 1.19)
    iva = round(subtotal * 0.19)

    context = {
        'total': total,
        'subtotal': subtotal,
        'iva': iva,
        'usuario': usuario,
        'carrito': carrito_actual,
        'pedido': nuevo_pedido,
        'fecha': fecha,
        'hora': hora,
    }
    html = template.render(context)

    # IMPORTANTE: parametro ruta es la ruta donde queremos guardar nuestra boleta temporal,
    # en este caso será la ruta donde se encuentra el proyecto en una carpteta /temp
    RUTA = "C:/Users/javie/OneDrive/Python/Tatins_Pizza/app/temp"
    file = open(os.path.join(RUTA, str('boleta') + '.pdf'), "w+b")

    # Creamos la boleta con pisaStatus
    pisaStatus = pisa.CreatePDF(
        html, dest=file)

    pisaStatus = pisa.CreatePDF(html, dest=file, link_callback=template)

    # Utilizamos el metodo para enviar nuestra boleta por correo
    enviar_boleta(RUTA, usuario.correo)

    # validacion de un error
    if pisaStatus.err:
        return HttpResponse('Error <pre>', html, '</pre>')

    # Limpiamos el carrito
    carrito_actual.clear()


    contexto = {
        "isLogged": isLogeado(),
        "isAdmin": isAdmin()
        
    }

    # Ahora renderizamos una template
    return render(request, "gracias.html",contexto)

    


def enviar_boleta(RUTA, correo):
    # IMPORTANTE: parametro ruta es la ruta donde queremos guardar nuestra boleta temporal,
    # en este caso será la ruta donde se encuentra el proyecto en una carpteta /temp

    # Datos usados para enviar gmail
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
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= {0}".format(
        os.path.basename(RUTA+str("/boleta.pdf"))))
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Ciframos la conexión
    sesion_smtp.starttls()
    # Iniciamos sesión en el servidor con el correo y contraseña
    sesion_smtp.login('tatinspizza@gmail.com', 'laspizzadeltatin')
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
    sesion_smtp.login('tatinspizza@gmail.com', 'laspizzadeltatin')
    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()
    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatario, texto)
    # Cerramos la conexión
    sesion_smtp.quit()
