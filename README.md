# Documentación del Juego de Batalla Naval

## Hecho por
Desarrolladores
- Melissa Foronda
- Andrea Marquez
Trabajado sobre el proyeto de:
- Walter y Luis Miguel

## Descripción
Este proyecto consiste en la implementación de un juego de batalla naval en Python. El juego permite a un jugador intentar hundir todos los barcos en un tablero de tamaño 10x10 utilizando coordenadas de disparo. O por medio de click a botones si usamos la interfaz grafica de kivy.

## Requisitos del Sistema
- Tener Python Instalado
- Tener Psycopg2
    pip install psycopg2
- Tener Kivy instalado
    pip install kivy[base]
- Tener Flask instalado
    pip install flask

## Instrucciones de Instalación
1. Copie el enlace HTTPS del github: "https://github.com/WalterBedoyaPerez/ProyectoBatallaNavalDB.git".
2. Abre una terminal (preferiblemente git bash) y clona el repositorio usando: `https://github.com/WalterBedoyaPerez/ProyectoBatallaNavalDB.git` .
3. Cambia/parate al repositorio usando: `cd ProyectoBatallaNavalDB`.
4. Cambia/parate a la carpeta src usando: `cd src`.

### Para interactuar con la base de datos 

1. Cambia al directorio de consola usando: `cd Controller` . 
2. Ejecuta el archivo preparativo de la base de datos:  `py controller_before_start.py` . 
3. Devuelvete a src usando `cd ..` . 
4. Cambia al directorio de View usando: `cd View` .
5. Ejectuta el archivo para jugar usando: `py consola.py` .


### Interfaz grafica

1. Cambia al directorio de interfaz usando: `cd View` .
2. Ejectuta el archivo usando: `py interfaz.py` .
3. Si deseas devolverte usa: `cd ..`

### Consola

1. Cambia al directorio de consola usando: `cd View` .
2. Ejectuta el archivo usando: `py consola.py` .
3. Si deseas devolverte usa: `cd ..`

### Web
1. Ejecuta el comando desde la carpeta raiz: `python app.py`
2. Correlo usando: `python -m flask run --debug`

## Estructura del Código
El código está organizado en cinco archivos principales:
- `logica.py`: Contiene la lógica del juego.
- `controll.py`: contiene la logica para el manejo de la base de datos.
- `test_DB.py`: contiene los test de la base de datos.
- `consola.py`: El archivo para que el usuario juegue/corra el juego por consola.
- `interfaz.py`: El archivo para que el usuario juegue/corra el juego por interfaz grafica.

## Descripción de las Funciones Principales

### Funcion crear tablero
Esta es la funcionalidad que recibe los datos del tablero y los crea haciendo uso de la clase "TableroBarcos".

### Funcion disparar
Esta es la funcionalidad que recibe las Coordenadas del disparo y nos confirma si disparamos a un barco o si fallamos, usando la clase "Disparar".


## Ejemplos de Uso
1. Sigue las instrucciones de instalacion
2. Una vez ejecutado entregas los datos que te pide el juego
3. Entregas las coordenadas donde crees que hay un barco o seleccionas el lugar donde crees que hay un barco y asi sucesivamente hasta que logres hallar y destruir todos los barcos.
4. Puedes volver a ejecutar el archivo para volver a jugar! :D