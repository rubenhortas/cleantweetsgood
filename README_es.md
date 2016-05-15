CleanTweetsGood
==================

¿QUÉ ES?

Es un programa que permite eliminar tweets de un usuario a partir de su histórico de twitter.

Se pueden eliminar tweets de dos formas:
    - Por contenido: Se eliminan los tweets que contengan una o varias palabras
         almacenadas en una lista negra definida por el usuario.
    - Por ID: Se eliminan los tweets a partir de su ID.

¿QUÉ *NO* ES?

No es un panic button ni una solución mágica. 

Aunque los tweets se borren del timeline, los cambios en el timeline tardan un tiempo en verse reflejados
(se puede comprobar descargando el historial de nuevo).

Los tweets borrados del timeline pueden quedar almacenados en sitios fuera del alcance de esta aplicación:
Los servidores de twitter, capturas de pantalla de otros usuarios... 
Cuando se borran los mensajes directos *no* se borran de la cuenta del otro usuario.

¿POR QUÉ?

Porque hay países donde las personas pueden  acabar en la cárcel por twittear.

Porque las empresas y los medios viven obsesionados con las redes sociales y algún tweet del pasado sacado 
de contexto puede hacerte tristemente famoso o puede hacer que pierdas una posible oportunidad de trabajo
o un trabajo.


CONFIGURACIÓN

* Iniciar sesión en twitter con tu cuenta: https://twitter.com

* Ir a https://apps.twitter.com/

* Hacer click en "Create New App"

* Rellenar el formulario:
    Name: CleanTweetsGood
    Description: Twitter cleaner
    Website: https://github.com/rubenhortas/cleantweetsgood
    Callback URL: Dejar en blanco

* Aceptar el acuerdo de desarrollador (Developer Agreement)

* Ir a la pestaña "Keys and Access Tokens"
    Obtener los tokens: Consumer Key, Consumer Secret, Access Token and Access Token Secret
    Configurar los tokens en el fichero configuration.py

* Ir a la pestaña "Permissions"
    Cambiar los permisos de "Access" a "Read, Write and Access direct messages"

* Hacer click en "Update settings"


REQUISITOS

* tweepy

* Descargar el histórico de twitter desde: https://twitter.com/settings/your_twitter_data

* Almacenar el histórico de twitter en el directorio raíz de la aplicación con el nombre: tweets.csv

USO:

uso: cleantweetsgood.py [-h] [-t] [-log] [-bl] [-dm] [-u USER [USER ...]]
                        [-id ID [ID ...]]

Limpia tu cuenta de twitter

argumentos opcionales:
    -h, --help            muestra este mensaje de ayuda y sale
    -t, --test            Ejecuta un test mostrando la salida esperada
    -log, --log           Guarda el resultado en un fichero de texto plano
    -bl, --blacklist      Elimina los tweets que contienen palabras que estén en la lista negra
    -dm, --direct_messages
                          Borra *TODOS* los mensajes directos
    -u USER [USER ...], --unfollow USER [USER ...]
                          Usuarios a dejar de seguir
    -id ID [ID ...]       IDs de los tweets a eliminar


AUTOR

Rubén Hortas
Contacto: rubenhortas at gmail.com
Website: http://www.rubenhortas.blogspot.com.es

LICENCIA

CC BY-NC-SA 3.0
http://creativecommons.org/licenses/by-nc-sa/3.0/

CONTACTO

Si tienes problemas, preguntas, ideas, o sugerencias puedes
contrubuir con este pequeño proyecto en el repositorio de github:

https://github.com/rubenhortas/CleanTweetsGood

WEB SITE

Visita el sitio del proyecto en github para ver las últimas novedades y descargas:

https://github.com/rubenhortas/CleanTweetsGood

