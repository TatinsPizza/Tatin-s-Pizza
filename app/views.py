from app.models import Comentario, Comida, Usuario
from django.shortcuts import redirect, render

# ----Usuario actual----
# Esta clase es creada con el fin de saber que usuario se encuentra logeado
# y asi porder permitir o no el ingreso a ciertas paginas


class Usuario_actual:
    id = 1
    logeado = True


# Intanciamos un objeto de la clase anterior
usuario_actual = Usuario_actual()

# ----Carrito----
# Esta clase nos ayudara a llevar la cuenta de cuales son las comidas que
# fueron pedidas por el Usuario y sus respectivas cantidades


class Carrito:
    def __init__(self, comida):

        self.comida = comida
        self.cantidad = 1


# Instanciamos un arreglo que usaremos para guardar los elementos del carrito
carrito_actual = []


# ----Visitante----

def index(request):
    # Este metodo se encarga de todo lo que ocurre en la pagina principal de nuestro proyecto

    # Obtenemos todos los comentarios desde la Base de datos
    comentarios = Comentario.objects.all()

    # ahora creamos un diccionarioque contiene  tanto los comentarios como
    # una variable que usaremos para condicionar el html
    contexto = {
        "comentarios": comentarios,
        "isLogged": usuario_actual.logeado
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

    # esto ocurre cuando no se llega a este metodo mediante redireccionamiento y no por un formulario
    # creamos el diccionario que contendra la variable que nos ayudara a condicionar el template
    contexto = {
        "isLogged": usuario_actual.logeado,
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
    # creamos el diccionario que contendra la variable que nos ayudara a condicionar el template
    contexto = {
        "isLogged": usuario_actual.logeado,
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

    # ahora creamos un diccionario que contiene  tanto las comidas como
    # una variable que usaremos para condicionar el html
    contexto = {
        "comidas": comidas,
        "isLogged": usuario_actual.logeado
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

        # Creamos un diccionario que lleva tanto los resultados de la busqueda como
        # la variable que siempre usarmos para condicionar los templates
        contexto = {
            "resultados": comidas,
            "isLogged": usuario_actual.logeado
        }

        # Ahora renderizamos una template y le enviamos el diccionario con los datos
        return render(request, "resultado_busqueda.html", contexto)

    # en caso de que no se llegue mediante el formulario se le redireccionara a la pagina principal
    return redirect("/tatinspizza.com")


# ----Cliente----

def mi_perfil(request):
    # Este metodo se encarga de enviarnos a una template donde el usuario pueda visualizar sus datos

    # obtenemos los datos del usuario logueados
    usuario = Usuario.objects.get(id_usuario=usuario_actual.id)

    # creamos un diccionario para enviar los datos y el condicional de siempre
    contexto = {
        "usuario": usuario,
        "isLogged": usuario_actual.logeado,

    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "mi_perfil.html", contexto)


def carrito(request):
    # Este metodo nos redirecciona a el carrito de compras y nos muestra lo que contiene

    # creamos un diccionario que contiene el arreglo de todo lo que hay en el carrito
    # y nuestra variable condicional
    contexto = {
        "carrito": carrito_actual,
        "isLogged": usuario_actual.logeado,
    }

    # Ahora renderizamos una template y le enviamos el diccionario con los datos
    return render(request, "carrito.html", contexto)


def agregar_al_carrito(request, id):
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
            carrito_actual[indice].cantidad += 1
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
    # Este metodo lo usamos para disminuir la cantidad de cierta comida o eliminarla en caso de que llegue a 0

    # Obtenemos la comida a la que se nos solicito modificar su cantidad
    comida = Comida.objects.get(id_comida=id)

    for carrito in carrito_actual:
        if carrito.comida == comida and carrito.cantidad > 1:
            carrito.cantidad -= 1
        elif carrito.comida == comida and carrito.cantidad == 1:
            indice = carrito_actual.index(carrito)
            carrito_actual.pop(indice)

    return redirect("/tatinspizza.com/carrito")


# Incompleto
def boleta(request, id):
    return render(request, "boleta.html")

# Casi-Completo


def comentario(request):
    if request.method == "POST":
        usuario = Usuario.objects.get(id_usuario=usuario_actual.id)
        texto = request.POST["texto"]

        nuevo_comentario = Comentario()
        nuevo_comentario.texto = texto
        nuevo_comentario.usuario = usuario
        nuevo_comentario.save()

    return redirect("/tatinspizza.com")


# ----Administrador----

# --Comida--
def monitoreo_comida(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"]

        nueva_comida = Comida()
        nueva_comida.nombre = nombre
        nueva_comida.descripcion = descripcion
        nueva_comida.precio = precio
        nueva_comida.save()

        return redirect("tatinspizza.com/monitoreo_comidas")

    comidas = Comida.objects.all()

    contexto = {
        "comidas": comidas,
    }

    return render(request, "monitoreo_comidas.html", contexto)


def editar_Comida(request, id):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"]

        actualizar_comida = Comida.objects.get(id_comida=id)
        actualizar_comida.nombre = nombre
        actualizar_comida.descripcion = descripcion
        actualizar_comida.precio = precio
        actualizar_comida.save()
        return redirect("tatinspizza.com/monitoreo_comidas")

    comida = Comida.objects.get(id_comida=id)

    contexto = {
        "comida": comida,
    }

    return render(request, "editar_comida.html", contexto)

# --Cliente--


def monitoreo_Usuario(request):

    clientes = Usuario.objects.all()

    contexto = {
        "clientes": clientes,
    }

    return render(request, "monitoreo_clientes.html", contexto)


def editar_Usuario(request, id):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]

        actualizar_usuario = Usuario.objects.get(id_usuario=id)
        actualizar_usuario.nombre = nombre
        actualizar_usuario.correo = correo
        actualizar_usuario.contrasena = contrasena
        actualizar_usuario.save()

        return redirect("tatinspizza.com/monitoreo_clientes")

    cliente = Usuario.objects.get(id_usuario=id)

    contexto = {
        "cliente": cliente,
    }

    return render(request, "editar_cliente.html", contexto)
