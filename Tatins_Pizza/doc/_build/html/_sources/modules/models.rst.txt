
**Models**
=============
Modelos utilizados en nuestro proyecto

Usuario
*********
Sujeto que usa la página y que realiza las acciones dentro de la plataforma.

* **id_usuario**: clave primaria.
* **nombre**: nombre del usuario que usa la plataforma.
* **correo**: email del usuario.
* **contrasena**: clave del usuario para ingresar a la .
* **admin**: campo utilizado para evaluar permiso de administrador

Comentario 
***********
Corresponden a los comentarios de los clientes registrados en el sistema

* **id_comentario**: clave primaria.
* **texto**: cuerpo del comentario.
* **usuario**: usuario quien publica.

Pedido 
********
Objeto utilizado para llevar el registro de una compra

* **id:** clave primaria.
* **fecha:** registra cuando fue realizada la compra.

Comida 
*******
Comida es la comida del restaurante

* **id_comida**: clave primaria.
* **nombre**: nombre de la comida.
* **descripcion**: cuerpo que describe la comdia.
* **precio**: valor de la comida.