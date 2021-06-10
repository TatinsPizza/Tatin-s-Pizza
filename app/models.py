from django.db import models

# Create your models here.

# Modelo Usuario
class Usuario(models.Model):
    # definimos "id_usuario" como primary key
    id_usuario = models.AutoField(primary_key=True)

    # Definimos "nombre" como un campo del tipo char con un maximo de 100 caracteres
    nombre = models.CharField(max_length=100)

    # Definimos "correo" como un campo del tipo char con un maximo de 100 caracteres
    correo = models.CharField(max_length=100)

    # Definimos "contrasena" como un campo del tipo char con un maximo de 20 caracteres
    contrasena = models.CharField(max_length=20)

    # Definimos "admin" como un campo del tipo SmallInteger (se usara como un Boolean)
    admin = models.SmallIntegerField(default= 0)

    # Este metodo nos retornara el campo "admin" como boolean
    def isadmin(self):
        if self.admin == 0:
            return False
        else:
            return True


# Modelo Comentario
class Comentario(models.Model):
    # definimos "id_comentario" como primary key
    id_comentario = models.AutoField(primary_key=True)

    # Definimos "texto" como un campo del tipo char con un maximo de 200 caracteres
    texto = models.CharField(max_length=200)

    # Definimos "usuario" como un campo clave foranea del tipo Usuario
    # (este se trabaja como un objeto  del tipo "Usuario" pero se guarda en la base de datos solo su id)
    usuario = models.ForeignKey(
        Usuario, null=True, blank=True, on_delete=models.CASCADE)


# Modelo Pedido
class Pedido(models.Model):
    # definimos "id_pedido" como primary key
    id_pedido = models.AutoField(primary_key=True)

    # Definimos "fecha" como un campo del tipo Date
    fecha = models.DateTimeField(auto_now_add=True)


# Modelo Comida
class Comida(models.Model):
    # definimos "id_comida" como primary key
    id_comida = models.AutoField(primary_key=True)

    # Definimos "nombre" como un campo del tipo char con un maximo de 45 caracteres
    nombre = models.CharField(max_length=45)

    # Definimos "descripcion" como un campo del tipo char con un maximo de 200 caracteres
    descripcion = models.CharField(max_length=200)

    # Definimos "precio" como un campo del tipo Integer y siempre positivo
    precio = models.PositiveIntegerField()


# Modelo Usuario_Pedido
class Usuario_Pedido(models.Model):
    # (al no crearle primary key a este modelo Django la crea automaticamente con el nombre de "id")

    # Definimos "usuario" como un campo clave foranea del tipo Usuario
    usuario = models.ForeignKey(
        Usuario, null=True, blank=True, on_delete=models.CASCADE)

    # Definimos "pedido" como un campo clave foranea del tipo Pedido
    pedido = models.ForeignKey(
        Pedido, null=True, blank=True, on_delete=models.CASCADE)


# Modelo Pedido_Comida
class Pedido_Comida(models.Model):
    # (al no crearle primary key a este modelo Django la crea automaticamente con el nombre de "id")

    # Definimos "comida" como un campo clave foranea del tipo Comida
    comida = models.ForeignKey(
        Comida, null=True, blank=True, on_delete=models.CASCADE)

    # Definimos "pedido" como un campo clave foranea del tipo Pedido
    pedido = models.ForeignKey(
        Pedido, null=True, blank=True, on_delete=models.CASCADE)
