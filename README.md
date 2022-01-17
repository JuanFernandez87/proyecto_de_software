# Proyecto de Software (materia de 3er año) -  Facultad de Informática
----
Para este proyecto se trabajó en una aplicación que permitia conocer y gestionar zonas con peligro de inundación y las acciones a llevar a cabo en caso de suceder un evento de este estilo.
Se desarrollaron dos aplicaciones, una privada donde los administradores del sistema y usuarios con permisos podian gestionar la informacíon de la aplicación. Ésta se realizo utizilando el lenguaje Python, el framework Flask, Jinja2 como motor de plantillas web y para gestionar la base de datos MariaDB.
En la aplicación privada las tareas que se pueden realizar son:
- Administrar Usuarios
- Gestionar puntos de encuentro
- Gestionar recorridos de evacuación
- Gestionar zonas inundables
- Gestionar denuncias

Y por otro lado una aplicación pública donde los y las habitantes podian ver información y realizar denuncias. En este caso para el Frontend usamos el Framework Vue3.

En el lado de la aplicación publica el sistema permitia:
- Ver información de puntos de encuentro
- Ver información de recorridos de evacuación
- Ver información de zonas inundables
- Ver mapa con denuncias
- Realizar denuncias

Integrantes del equipo:
- Verdugo, Felipe
- Pontiroli, Gaspar
- Fernandez, Juan Manuel

### Objetivo 
----
El 2 de abril de 2013, la ciudad sufrió un evento extraordinario que provocó que distintas
zonas de la ciudad quedaran inundadas con graves consecuencias.
El trabajo integrador de la cursada se enfocó en el desarrollo de un prototipo que brinde información a los y las habitantes de la ciudad de La Plata sobre:
- Zonas inundables de la ciudad;
- Puntos de encuentro en caso de una emergencia;
- Recorridos de evacuación.

También se podrá realizar denuncias respecto a alcantarillas tapadas, basurales, etc.

### Instalación
----
#### 1 Paso
- ***1 forma***. Dar clic en Code y luego en Donwload Zip 
- ***2 forma***. Crear una carpeta, ingresar a git bash y ejecutar

```css
  git clone https://github.com/JuanFernandez87/proyecto_de_software.git
```

#### 2 Paso
- Crear una base de datos con el nombre proyecto_software

#### 3 Paso
- Configurar la contraseña en el archivo .env
- Configurar el usuario en el archivo .env

#### 4 Paso
- Instalar virtualenv
```css
pip install virtualenv
```
- Dentro de la carpeta del proyecto iniciar el entorno virtual
```css
virtualenv entornoProyecto
```
- Activar el entorno virtual
```css
source entornoProyecto/bin/activate
```
- Instalar las librerias utilizadas
```css
pip install -r requirements.txt
```
#### 5 Paso 
- Instalar npm
```css
npm install vue@next
```
#### 6 Paso 
- Instalar Vue CLI 3
```css
yarn global add @vue/cli
```
#### 7 Paso 
- ***Ejecución de app privada***.  Dentro de la carpeta app ejecutar el comando
```css
flask run
```
- ***Ejecución de app pública***.   Dentro de la carpeta Web ejecutar el comando
```css
yarn serve
```
