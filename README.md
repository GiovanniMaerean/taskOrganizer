# README

La aplicación web “Task Organizer” se trata de una aplicación que permitirá al usuario organizar sus tareas pendientes, similar a otras aplicaciones de gestión de tareas. Dicha aplicación permite crear cursos, asignaturas de dichos cursos y tareas de dichas asignaturas, además de poder eliminarlas y ver los detalles de cada uno de los objetos. 

Los usuarios tendrán cuentas asociadas a ellos, por lo que todas las clases, asignaturas y tareas serán privadas para dicho usuario, y no podrán ser accedidas por otros usuarios.

##DEPENDENCIAS
Para ejecutar todas las dependencias de la aplicación web se pueden instalar mediante el comando de poetry:

```poetry
poetry install
```

En caso contrario, revisar el fichero [requeriments.txt](requeriments.txt)

## PASOS DE EJECUCIÓN
### Paso 1

Situate en el directorio de la aplicación, abre la terminal y genera las migraciones mediante el comando:

```python
python manage.py makemigrations
```

### Paso 2
Aplica las migraciones generadas mediante el comando:

```python
python manage.py migrate
```

### Paso 3
Ejecuta la aplicación web mediante el comando:

```python
python manage.py runserver
```

### Paso 4
Abre un navegador e introduce la **IP del servidor** de la aplicación web. Por defecto dicha dirección IP es la "http://127.0.0.1:8000/".


## CREAR SUPERUSUARIO
Una vez hayamos creado y aplicado las migraciones, podemos crear un superusuario, que nos permitirá acceder a la vista de administrador, desde la cual podremos crear y eliminar instancias de modelos con total libertad, además de editarlos.

Para crear un **superusuario** deberemos utilizar el comando:

```python
python manage.py createsuperuser
```

Ahora deberemos ejecutar el servidor de la aplicación y añadir a la url base "/admin", que en el caso de la IP por defecto sería "http://127.0.0.1:8000/admin/".

## EMPLEO DE LA APLCACIÓN
### INICIO DE SESIÓN O REGISTRO
Al entrar al servidor de la aplicación se nos pedirá iniciar sesión o registrarse. En caso de no tener ya una cuenta, el usuario deberá registrarse para después iniciar sesión. En caso de ya poseer una cuenta, podrá iniciar sesión directamente.

### PÁGINA PRINCIPAL
Una vez hemos inciado sesión, se nos llevará a la página principal, donde nos aparecerán todas las instancias que hayamos creado. Estas instancias serán de tres tipos:

* Cursos
* Asignaturas
* Tareas

Todas las tareas tienen una asignatura asociada, y todas las asignaturas tienen un curso asociado. Mediante la barra superior podremos elegir a que otra vista queremos desplazarnos, siendo estas la página principal, la página de crear curso, la página de crear asignatura y la página de crear tarea. El último botón sirve para cerrar sesión, lo que nos permitirá poder volver a iniciar sesión con una cuenta diferente.

### CREACIÓN DE INSTANCIAS
Para crear una nueva instancia deberemos dirigirnos al apartado específico de la instancia que queramos crear, ubicado en la barra superior. Una vez nos hayamos movido a dicha vista, deberemos rellenar el formulario que generará la instancia con todos los datos que le proporcionemos. Cuando hayamos ingresado los datos, solo quedará darle a "Crear" para crear la instancia. La aplicación nos mostrará a continuación los detalles de dicha instancia.

