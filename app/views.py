from app.models import Comentario, Comida, Usuario
from django.shortcuts import redirect, render

# ----Usuario actual----


class Usuario_actual:
    id = 0
    logeado = False


usuario_actual = Usuario_actual()

# ----Carrito----
pedido = []
cantidad = []

# ----Visitante----
# Incompleto


def index(request):
    return render(request, "index.html")

# Casi-Completo (falta verificacion de correo)

def registro(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        contrasena1 = request.POST["contrasena1"]
        contrasena2 = request.POST["contrasena2"]


        if Usuario.objects.filter(correo=correo).exist() and contrasena1 != contrasena2:
            return redirect("tatinspizza.com/registro")

        nuevo_usuario = Usuario()
        nuevo_usuario.nombre = nombre
        nuevo_usuario.correo = correo
        nuevo_usuario.contrasena = contrasena1
        nuevo_usuario.save()

        return redirect("tatinspizza.com/inicio_sesion")

    return render(request, "registro.html")

# Incompleto (falta redirijir al iniciar sesion)


def inicio_sesion(request):
    if request.method == "POST":
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]

        if Usuario.objects.filter(correo=correo, contrasena=contrasena).exists():
            usuario = Usuario.objects.get(correo=correo)
            usuario_actual.id = usuario.id_usuario
            usuario_actual.logeado = True

            return redirect("")

    return render(request, "inicio_sesion.html")

# Completo


def menu(request):
    comidas = Comida.objects.all()

    contexto = {
        "comidas": comidas,
    }

    return render(request, "menu.html", contexto)

# Completo


def comida(request, id):
    comida = Comida.objects.get(id_comida=id)

    contexto = {
        "comida": comida,
    }

    return render(request, "comida.html", contexto)

# completo
def busqueda(request):
    return render(request, "comida.html")

# Completo


def resultado_busqueda(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]

        comidas = Comida.objects.filter(nombre__icontains=nombre)

        contexto = {
            "comidas": comidas,
        }

        return render(request, "resultado_busqueda.html", contexto)

    return redirect("tatinspizza.com/busqueda")


# ----Cliente----


# Incompleto
def cuenta(request, id):
    usuario = Usuario.objects.get(id_usuario=usuario_actual.id)

    contexto = {
        "usuario": usuario,
    }

    return render(request, "cuenta.html", contexto)

# Incompleto


def carrito(request):

    return render(request, "carrito.html")

# Incompleto


def agregar_al_carrito(request, id):
    comida = Comida.objects.get(id_comida=id)

    if comida in pedido:
        indice = pedido.index(comida)
        aumentar_al_carrito(indice)

    else:
        pedido.append(comida)
        cantidad.append(1)

    return redirect("tatinspizza.com/menu")


def aumentar_al_carrito(indice):
    cantidad[indice] += 1

    return redirect("tatinspizza.com/carrito")


def disminuir_al_carrito(request, id):
    comida = Comida.objects.get(id_comida=id)
    indice = pedido.index(comida)

    if (cantidad[indice] == 1):
        quitar_al_carrito(indice)

    else:
        cantidad[indice] -= 1

    return redirect("tatinspizza.com/carrito")


def quitar_al_carrito(indice):
    pedido.pop(indice)
    cantidad.pop(indice)

    return redirect("tatinspizza.com/carrito")


# Incompleto
def pedir(request, id):
    return render(request, "pedir.html")

# Incompleto


def boleta(request, id):
    return render(request, "boleta.html")

# Casi-Completo


def comentario(request):
    if request.method == "POST":
        usuario = Usuario.objects.get(id_usuario=usuario_actual.id)
        comentario = request.POST["comentario"]

        nuevo_comentario = Comentario()
        nuevo_comentario.comentario = comentario
        nuevo_comentario.usuario = usuario
        nuevo_comentario.save()

        return redirect("tatinspizza.com/comentarios")

    comentarios = Comentario.objects.all()

    contexto = {
        "comentarios": comentarios,
    }

    return render(request, "comentarios.html", contexto)


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
        "clientes": clientes,
    }

    return render(request, "monitoreo_clientes.html", contexto)


def editar_cliente(request, id):
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
