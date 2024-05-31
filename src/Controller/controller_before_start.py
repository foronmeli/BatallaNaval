#Imports necesarios
import sys
import os
import psycopg2

# Agregar el directorio padre al path para permitir importaciones relativas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controll import ControladorUsuario

#Elimina las tablas de diccionario y tablero
ControladorUsuario.EliminarTabla()
ControladorUsuario.EliminarTablaDiccionarios()
#Y las vuelve a agregar para asi tener un comienzo limpio y evitar errores
ControladorUsuario.CrearTablaDiccionarios()
ControladorUsuario.CrearTabla()

print("terminado")
