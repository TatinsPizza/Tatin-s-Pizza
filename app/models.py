from django.db import models

# Create your models here.
#Falta modificar los usuarios

#listo
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=20)
    admin = models.PositiveSmallIntegerField()

    def isadmin(self):
        if self.admin == 0:
            return False
        else:
            return True



#Incompleto
class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario,null=True, blank=True, on_delete=models.CASCADE)


    
#Listo
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    estado = models.SmallIntegerField()
    fecha = models.DateTimeField(auto_now_add = True)

#Listo
class Comida(models.Model):
    id_comida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    ingredientes = models.CharField(max_length=200)
    precio = models.PositiveIntegerField()
    
#Listo
class Pedido_Comida(models.Model):
    comida = models.ForeignKey(Comida,null=False, blank=False, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido,null=False, blank=False, on_delete=models.CASCADE)


