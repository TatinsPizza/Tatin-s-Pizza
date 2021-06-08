**Views**
==========
En este apartado se definiran las funciones de nuestras Views

Variables
+++++++++++
* **Usuario_actual**: Variable global utilizada para almacenar los datos del usuario que esté utilizando la plataforma.
* **Carrito**: Variable global utilizada para almacenar las comidas y datos perteneciente a la comida.
* **carrito_actual[]**: Arreglo que almacena distintas comidas(**Carrito**).

index
+++++++
**index(request)**

Vista correspondiente a otorgar informacion y la opcion de inicio de sesion, en conjunto a buscar y listar comida

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   =======================================================================================
        Parametro   Definicion
        =========   =======================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **index.html** 
        =========   =======================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ======================================================================================================
        Retorno          Definicion
        ==============   ======================================================================================================
        render           Renderiza hacia la template **index.html** y con un diccionario correspondiente al estado del usuario
        ==============   ======================================================================================================

registro
++++++++++
**registro(request)**

Con esta views el usuario se registrará al sistema. registro en primera instancia nos redirige a su propia funcion, en donde si accedemos al formulario, en especifico: **"if request.method == "POST":"**, nos guardará los datos del formulario y no redirigirá a la vista **index**. 

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   =======================================================================================
        Parametro   Definicion
        =========   =======================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **registro.html** 
        =========   =======================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ===============================================================================================================================
        Retorno          Definicion
        ==============   ===============================================================================================================================
        render           Renderiza hacia la template **index.html** con la sesion iniciada y con un diccionario correspondiente al estado del usuario
        redirect         Redirige hace la direccion **tatinspizza.com** correspondiente a la vista **index**
        ==============   ===============================================================================================================================

inicio_sesion
++++++++++++++
**inicio_sesion(request)**

En esta view el usuario podrá iniciar sesión. inicio_sesion en primera instancia nos redirige a su propia funcion, en donde si accedemos al formulario, en especifico: **"if request.method == "POST":"**, nos guardará los datos del formulario y no redirigirá a la vista **index**

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ================================================================================================
        Parametro   Definicion
        =========   ================================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **iniciar_sesion.html** 
        =========   ================================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ===================================================================================
        Retorno          Definicion
        ==============   ===================================================================================
        render           Redirige hace la direccion **tatinspizza.com** correspondiente a la vista **index**
        ==============   ===================================================================================


cerrar_sesion
++++++++++++++
**cerrar_sesion(request)**

En esta view el usuario cierra la sesion dentro de la plataforma. Si el usuario cierra sesion será redirigido hacia la vista **index**.

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ====================================================================================================
        Parametro   Definicion
        =========   ====================================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **index.html** 
        =========   ====================================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ===================================================================================
        Retorno          Definicion
        ==============   ===================================================================================
        redirect         Redirige hace la direccion **tatinspizza.com** correspondiente a la vista **index**
        ==============   ===================================================================================


menu
+++++
**menu(request)**

En esta view el usuario podrá visualizar todas las comidas disponibles para pedir.

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   =======================================================================================
        Parametro   Definicion
        =========   =======================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **menu.html** 
        =========   =======================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ==========================================================================================================
        Retorno          Definicion
        ==============   ==========================================================================================================
        render           Renderiza hacia la template **menu.html** con un diccionario que contiene **Comida** y estado del usuario
        ==============   ==========================================================================================================


resultado_busqueda
++++++++++++++++++++++++++++++++
**resultado_busqueda(request)**

En esta view el usuario podrá buscar la comida que quiere segun su nombre. resultado_busqueda en primera instancia nos redirige a su propia funcion, en donde si accedemos al formulario, en especifico: **"if request.method == "POST":"**, nos guardará los datos del formulario y no redirigirá a la vista **resultado_busqueda**

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ====================================================================================================
        Parametro   Definicion
        =========   ====================================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **resultado_busqueda.html** 
        =========   ====================================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   =====================================================================================================================
        Retorno          Definicion
        ==============   =====================================================================================================================
        render           Renderiza hacia la template **resultado_busqueda.html** con un diccionario que contiene comidas y estado del usuario
        ==============   =====================================================================================================================


mi_perfil
++++++++++
**mi_perfil(request)**

En esta view el usuario puede ver sus datos y tiene la posiblidad de editar sus datos mediante la redireccionamiento hacia la view **editar_perfil** 

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ==========================================================================================
        Parametro   Definicion
        =========   ==========================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **mi_perfil.html** 
        =========   ==========================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ==============================================================================================================
        Retorno          Definicion
        ==============   ==============================================================================================================
        render           Renderiza hacia la template **mi_perfil.html** con un diccionario que contiene al usuario y tambien su estado
        ==============   ==============================================================================================================

carrito
+++++++++
**carrito(request)**

En esta view el usuario puede visualizar su carrito, donde carrito posee todas las comidas agregadas además de editar su cantidad, eliminar y agregar mas elementos. 

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ==========================================================================================
        Parametro   Definicion
        =========   ==========================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **carrito.html** 
        =========   ==========================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ===========================================================================================================================
        Retorno          Definicion
        ==============   ===========================================================================================================================
        render           Renderiza hacia la template **carrito.html** con un diccionario que contiene el **carrito_actual** y el estado del usuario
        ==============   ===========================================================================================================================

agregar_al_carrito
++++++++++++++++++++
**agregar_al_carrito(request,id)**

En esta view el usuario es activada por el comportamiento del boton dentro de la template **carrito.html**, en donde si se activa se agrega una unidad de comida respectiva.

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ==========================================================================================
        Parametro   Definicion
        =========   ==========================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **carrito.html** 
        id          id_comida de **Comida**
        =========   ==========================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   =======================================================================================
        Retorno          Definicion
        ==============   =======================================================================================
        redirect         Redirige hace la direccion **tatinspizza.com/menu** correspondiente a la vista **menu**
        ==============   =======================================================================================


disminuir_al_carrito
+++++++++++++++++++++++++
**disminuir_al_carrito(request,id)**

En esta view el usuario es activada por el comportamiento del boton dentro de la template **carrito.html**, en donde si se activa se disminuirá una unidad de comida respectiva.

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ==========================================================================================
        Parametro   Definicion
        =========   ==========================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **carrito.html** 
        id          id_comida de **Comida**
        =========   ==========================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   =========================================================================================
        Retorno          Definicion
        ==============   =========================================================================================
        redirect         Redirige hacia la direccion **tatinspizza.com/menu** correspondiente a la vista **menu**
        ==============   =========================================================================================


comentario
+++++++++++++++++++++++++
**comentario(request)**

Esta view es utilizada por el usuario para dejar un **comentario** y sea visualizado en **index.html**

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ==========================================================================================
        Parametro   Definicion
        =========   ==========================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **index.html** 
        =========   ==========================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   =====================================================================================
        Retorno          Definicion
        ==============   =====================================================================================
        redirect         Redirige hacie la direccion **tatinspizza.com** correspondiente a la vista **index**
        ==============   =====================================================================================


monitoreo_comidas
+++++++++++++++++++++++++
**monitoreo_comidas(request)**

Esta view es utilizada para visualizar las comidas, donde es posible crearlas, editarlas y/o eliminarlas mediante las funciones **crear_comida()** , **editar_comida()** y **eliminar_comida()**.

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ==========================================================================================
        Parametro   Definicion
        =========   ==========================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la templates correspondientes
        =========   ==========================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ====================================================================================================================================
        Retorno          Definicion
        ==============   ====================================================================================================================================
        render           Renderiza hacia la template **monitoreo_comidas.html** con un diccionario que contiene todas las **Comida** y el estado del usuario
        ==============   ====================================================================================================================================


eliminar_comida
++++++++++++++++
**eliminar_comida(request,id)**

Esta view es utilizada para eliminar una comida segun su id.

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ===================================================================================================
        Parametro   Definicion
        =========   ===================================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **monitoreo_comidas.html**
        id          id_comida de **Comida**
        =========   ===================================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   =======================================================================================================
        Retorno          Definicion
        ==============   =======================================================================================================
        redirect         Redirige hace la direccion **tatinspizza.com/monitoreo_comidas** correspondiente a la vista **index**
        ==============   =======================================================================================================


crear_comida
++++++++++++
**crear_comida(request,id)**

Esta view es utilizada para crear una comida segun su id. crear_comida en primera instancia nos redirige a su propia funcion, en donde si accedemos al formulario, en especifico: **"if request.method == "POST":"**, nos guardará los datos del formulario y no redirigirá a la vista **crear_comida**

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ==================================================================================================
        Parametro   Definicion
        =========   ==================================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **monitoreo_comida.html**
        id          id_comida de **Comida**
        =========   ==================================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ====================================================================================================================================
        Retorno          Definicion
        ==============   ====================================================================================================================================
        render           Renderiza hacia la template **monitoreo_comidas.html** con un diccionario que contiene todas las **Comida** y el estado del usuario
        ==============   ====================================================================================================================================


editar_comida
+++++++++++++++++++++++++
**editar_comida(request,id)**

Esta view es utilizada para editar una comida segun su id. editar_comida en primera instancia nos redirige a su propia funcion, en donde si accedemos al formulario, en especifico: **"if request.method == "POST":"**, nos guardará los datos del formulario y no redirigirá a la vista **editar_comida**

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ==================================================================================================
        Parametro   Definicion
        =========   ==================================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **monitoreo_comida.html**
        id          id_comida de **Comida**
        =========   ==================================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ====================================================================================================================================
        Retorno          Definicion
        ==============   ====================================================================================================================================
        render           Renderiza hacia la template **monitoreo_comidas.html** con un diccionario que contiene todas las **Comida** y el estado del usuario
        ==============   ====================================================================================================================================


monitoreo_usuarios
+++++++++++++++++++++++++
**monitoreo_usuarios(request,id)**

Esta view es utilizada para visualizar los usuarios, donde es posible editarlas y/o eliminarlas mediante las funciones **eliminar_usuario()** y **editar_usuario()**.

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ====================================================================================================
        Parametro   Definicion
        =========   ====================================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **monitoreo_usuarios.html**
        =========   ====================================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   =====================================================================================================================================
        Retorno          Definicion
        ==============   =====================================================================================================================================
        render           Renderiza hacia la template **monitoreo_usuarios.html** con un diccionario que contiene todas los **Usuario** y el estado del usuario
        ==============   =====================================================================================================================================


eliminar_usuario
+++++++++++++++++++++++++
**eliminar_usuario(request,id)**

Esta view es utilizada para eliminar un usuario segun su id.

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ===================================================================================================
        Parametro   Definicion
        =========   ===================================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **monitoreo_usuarios.html**
        id          id_usuario de **Usuario**
        =========   ===================================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   ====================================================================================================================================
        Retorno          Definicion
        ==============   ====================================================================================================================================
        redirect         Redirige hacia la direccion **tatinspizza.com/monitoreo_usuarios** correspondiente a la vista **monitoreo_usuarios**
        ==============   ====================================================================================================================================


editar_usuario
+++++++++++++++++++++++++
**editar_usuario(request,id)**

Esta view es utilizada para editar una comida segun su id. editar_usuario en primera instancia nos redirige a su propia funcion, en donde si accedemos al formulario, en especifico: **"if request.method == "POST":"**, nos guardará los datos del formulario y no redirigirá a la vista **editar_usuario**

**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ====================================================================================================
        Parametro   Definicion
        =========   ====================================================================================================
        request     Solitud o pedido utilizado para obtener y dar informacion a la template **monitoreo_usuarios.html**
        id          id_usuario de **Usuario**
        =========   ====================================================================================================

**Retornos:**

    .. table:: Retorno de la funcion
        :widths: 20,70

        ==============   =====================================================================================================================
        Retorno          Definicion
        ==============   =====================================================================================================================
        redirect         Redirige hacia la direccion **tatinspizza.com/monitoreo_usuarios** correspondiente a la vista **monitoreo_usuarios**
        ==============   =====================================================================================================================

boleta
+++++++++++++++++++++++++
**boleta()**

Este metodo es utilizado para generar y enviar boleta, utilizando **enviar_boleta()**, Aqui utilizamos dentro de codigo 

enviar_boleta
+++++++++++++++++++++++++
**enviar_boleta(RUTA,correo)**

Metodo utilizado para enviar boleta hacia un correo electronico, aqui se importan variables librerias que funcione y tambien necesita de un correo y contraseña real de gmail


**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ====================================================================================================
        Parametro   Definicion
        =========   ====================================================================================================
        RUTA        ruta en donde tenemos nuestra boleta.pdf
        correo      correo del **Usuario**
        =========   ====================================================================================================

enviar_bienvenida
+++++++++++++++++++++++++
**enviar_bienvenida(correo)**

Metodo utilizado para enviar saludo hacia un correo electronico, aqui se importan variables librerias que funcione y tambien necesita de un correo y contraseña real de gmail


**Parametros:**

    .. table:: Parametros de la funcion
        :widths: 20,70

        =========   ====================================================================================================
        Parametro   Definicion
        =========   ====================================================================================================
        correo      correo del **Usuario**
        =========   ====================================================================================================
