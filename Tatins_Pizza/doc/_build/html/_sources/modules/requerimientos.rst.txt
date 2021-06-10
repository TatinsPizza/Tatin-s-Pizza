**Herramientas de desarrollo**
================================
* **Python:** Lenguaje de Programación. 
* **Django:** ​Framework de desarrollo web. 
* **Psycopg2:** Adaptador de base de datos Postgre para Python. 
* **Bootstrap:** Herramienta estilo de diseño grafico. 
* **PostgreSQL:** Base de datos. 
* **Git:** Sistema de Control de Versiones. 
* **GitHub:** Alojamiento del proyecto utilizando Git. 
* **Xhtml2pdf:** Librería utilizada para crear y modificar pdf.
* **Visual Studio Code:** Editor de código fuente, el cual cuenta con las herramientas para desarrollar eficientemente proyectos con las tecnologías nombradas con anterioridad.


**Arquitectura**
=================

Logíca
+++++++
**MVC:** Modelo-Vista-Controlador es un conocido patrón de arquitectura de software donde separa por lógicas la funcionalidad. Django redefine el modelo MVC a MVT (Models-Views-Templates).
Dónde lógica es:

* Models: Comunicar e interactuar con la base de datos.
* Views: Manipular e interpretar models, además de interactuar con templates.
* Templates: Visualizar y ofrecer interacción con el usuario.

.. figure:: /img/mvt.png
    :align: center

Base de datos
++++++++++++++
A continuacion el diagrama que representa las tablas y relaciones en la base de datos utilizando MySQLWorkbench

.. figure:: /img/base_datos.png
    :align: center

Modelo MVT
++++++++++

A continuacion nuestro model MVT que fue utilizado para crear proyecto:

.. figure:: /img/visitante.png
    :align: center

.. figure:: /img/cliente.png
    :align: center

.. figure:: /img/comida.png
    :align: center