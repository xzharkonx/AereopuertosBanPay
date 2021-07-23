# API Aereopuertos - Ban Pay

## Versión de python utilizada
 - Consultar versión desde la consola: python --version
 - Versión: Python 3.7.4


## Paso 0. Entornos virtuales.

- Puedes utilizar alguna de estas herramientas  para crear el entorno virtual.
 - virtualenv
  - gestión global
 - pipenv
  - gestión por proyecto

Utilizaremos pipenv

Instalar pipenv
- pip install pipenv

Opciones de pipenv
- pipenv --help

## Paso 1. Crear entorno virtual para el proyecto.

- Crea una carpeta en el directorio de tu elección.
 - Nombre carpeta: AereopuertosBanPay
 - Ejemplo: C:\Users\usuario\Documents\AereopuertosBanPay

Posicionate dentro del directorio de esa carpeta desde la terminal.

Ahora utilizaremos el siguiente comando para crear el entorno de python
- Comando: pipenv --python [version]
- Ejemplo: pipenv --python 3.7.4

Si da problemas de creación intenta con la versión de tu python instalado o 
bien prueba con virtualenv.

Ahora correremos el entorno virtual para ese directorio con el siguiente comando.
- pipenv run python



Al ejecutarlo ya estaremos accediendo al interprete de python pero de este entorno virual.

Podemos ver los paquetes instalados en el entorno virutal para ese directorio con el siguiente comando.
- pipenv graph

O también con este comando para acceder solo a las de este entorno virtual.
- pipenv run pip list

Ver en donde se ha creado el entorno virtual.
- pipenv --venv

Si queremos remover el entorno virtual que creamos lo hacemos con el siguiente comando.
- pipenv --rm

Activar entonrno
- pipenv shell

## Paso 2. Instalar las siguietes librerías.

Una vez creado nuestro entorno virtual instalaremos las siguientes librerías para el correcto funcionamiento
de nuestro proyecto.

- django
 - Framework de Django
- django-ckeditor
 - Editor WYSIWYG para editar campos de texto en el panel de administrador.
- Pillow
 - Sirve para gestionar imágenes en nuestro panel de administrador y proyectos (Opcional).
- pylint
 - Es el Lighting para mostrar posibles errores de código de las importaciones en el entorno de VSCode.
- pylint-django
 - Complemento de pylint para Django.
- pylint-celery
 - También para el linting.

- Comando: pipenv install django django-ckeditor Pillow pylint pylint-django pylint-celery

Ahora instalaremos los paquetes del Api Rest de Google para conectarnos a las Sheets Api
- Comando: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

## Paso 3. Levantar nuestra API.
- Primero hay que estar el el directorio principal de nuestro proyecto donde se encuentra el archivo "manage.py"
- Despues habilitaremos el entorno de nuestro proyecto.
- Luego utilizaremos el siguiente comando para correr el servidor enbebido.
- python manage.py runserver

También se puede correr el servidor sin el entorno activado. Vamos un directorio atrás.
- pipenv run python AereopuertosBanPay/manage.py runserver