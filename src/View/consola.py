#Importaciones de los modulos
import random
import sys
import os

# Agregar el directorio padre al path para permitir importaciones relativas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importaciones de módulos propios
from Model.logica import *
from Controller.controll import *

# Creación de excepciones personalizadas
class CoordenadasValorIncorrecto(ValueError):
    pass
class CantidadValorIncorrecto(ValueError):
    pass

# Función para ingresar cantidad de barcos, fila o columna
def Ingresar_cantidad(i):
    """Cuando recibe 1: para comprobar el ingreso de barcos 1-9 para colocarlos, 2/3: para comprobar ingreso de fila y columna 1-10 para disparar, respectivamente."""

    while True:
        try:
            if i == 1:
                cantidad = int(input("Ingrese la cantidad de barcos (1 - 9) que desea: "))
            if i == 2: 
                cantidad = int(input("Ingrese la fila (1 - 10) a la que desea disparar: "))
            if i == 3:
                cantidad = int(input("Ingrese la columna (1 - 10) a la que desea disparar: "))

            if i == 2 or i == 3:
                if 1 <= cantidad <= 10:
                    return cantidad
                else:
                    raise CantidadValorIncorrecto
            if i == 1:
                if 0 < cantidad <= 9:
                    return cantidad
                else:
                    raise CantidadValorIncorrecto
            
        except CantidadValorIncorrecto:
            if i == 1:
                print("Ingrese un valor entre 1 y 9")
            else:
                print("Ingrese un valor entre 1 y 10")
        except Exception:
            if i == 1:
                print("Ingrese un valor entre 1 y 9")
            else:
                print("Ingrese un valor entre 1 y 10")

# Función para preguntar al usuario si desea seguir jugando
def preguntar_seguir_jugando():
    """Seguir: False , Terminar: True"""
    print("\n")
    print("_______________________________________________")
    try:
        if int(input("Si desea continuar ingrese cualquier cosa, si desea terminar ingrese '0': ")) != 0:
            return False
        return True
    except Exception:
        return False
    



    

# Función principal para jugar
def Jugar():

    #Crea un objeto de la clase Tablero y lo guarda en juego
    juego = Tablero()
    print("\n")

    #Pregunta si desea modificar los datos guardados
    if input("Si desea modificar los datos guardados, ingrese 'si' , si no ingrese cualquier cosa. ")== "si":

        #si la respuesta es si, pregunta si desea cargar o eliminar o ninguna de las anteriores
        guardar_eliminar=input("Si desea cargar partida ingrese 'cargar', si desea eliminar partida ingrese 'eliminar', si no desea hacer las anteriores ingrese cualquier otro dato: ")
        
        #Si ingresa 'cargar'
        if guardar_eliminar=="cargar" :

            #Activa el switche de cargar_partida
            cargar_partida=True

            #Busca si hay partidas para cargar
            try:
                listado_partidas = ControladorUsuario.partidasCargadas()

            except NoHayPartidasGuardadasError:

                #Si no hay partidas guardadas 
                print("No hay partidas guardadas, se procedera con el juego normalmente. ")

                #Prosigue con el juego colocando los barcos
                juego.colocar_barcos(Ingresar_cantidad(1))
                #Cierra el switche
                cargar_partida=False

            else:

                #Si hay partidas guardadas las muestra
                print("Partidas guardadas: ",listado_partidas)

                #entra al bucle donde le pedira el nombre de la partida que desea cargar
                while cargar_partida:

                    #le pregunta el nombre o 'salir' si desea salir
                    entrada = str(input("Ingrese el nombre de la partida que desea cargar (ingrese 'salir' si desea salir de menu de cargar partida): "))

                    #si ingresa un nombre de una partida que si esta guardada entonces
                    if entrada in listado_partidas:

                        #cambia el diccionario del juego actual por el que cargo de la DB
                        juego.barcos=ControladorUsuario.BuscarDiccionarioId(entrada)
                        #cambia el tablero del juego actual por el que cargo de la DB
                        juego.tablero=ControladorUsuario.BuscarTableroId(entrada)
                        #Cambia el nombre de la partida actual de None a el nombre de la partida que se cargo (Servira mas adelante para la actualizacion de partidas)
                        juego.nombre=entrada
                        #Mensaje de confirmacion
                        print("Partida con nombre: ", entrada, " cargada exitosamente. ")
                        cargar_partida=False
                        #sale del bucle

                    #Si ingresa 'salir' entonces
                    elif entrada == "salir":
                        #Prosigue con el juego colocando los barcos
                        juego.colocar_barcos(Ingresar_cantidad(1))
                        cargar_partida=False
                        #Sale del bucle

                    #Si ingresa algun dato diferente a 'salir' o a el nombre de una partida guardada
                    else:
                        print("Ingrese un nombre de partida guardada existente.")
                        #Repite el bucle/itera de nuevo

        #Si ingresa 'eliminar'
        elif guardar_eliminar == "eliminar":

            #Activa el switche eliminar_partida
            eliminar_partida=True

            #Busca si hay partidas que eliminar
            try:
                listado_partidas = ControladorUsuario.partidasCargadas()
                
             
            except NoHayPartidasGuardadasError:

                #Si no hay partidas guardadas para eliminar
                print("No hay partidas guardadas para eliminar, se procedera con el juego normalmente. ")

                #Prosigue con el juego normalmente
                juego.colocar_barcos(Ingresar_cantidad(1))
                eliminar_partida=False
                #Sale del bucle

            else:

                #Si hay partidas guardadas 
                print("Partidas guardadas: ",listado_partidas)

                #entra al bucle para pedir nombre de la partida guardada a eliminar
                while eliminar_partida:

                    #le pide el nombre o 'salir' si desea salir
                    entrada = str(input("Ingrese el nombre de la partida que desea eliminar (ingrese 'salir' si desea salir de menu de eliminar partida): "))

                    #Si ingresa 'salir'
                    if entrada == "salir":

                        #Prosigue con el juego normalmente
                        juego.colocar_barcos(Ingresar_cantidad(1))
                        eliminar_partida=False
                        #sale del bucle 

                    else:

                        #Si ingresa un posible nombre
                        try:

                            #intenta eliminar la partida con dicho nombre
                            ControladorUsuario.eliminarPartida(entrada)
                        
                        #Si no hay partida con dicho nombre
                        except EliminarSinExistenciaError:

                            #Repite el bucle/itera otra vez
                            print("Ingrese un nombre de partida guardada existente.")
                        
                        #Si se encuentra una partida guardada con ese nombre se elimina
                        else:

                            #Prosigue con un juego nuevo normalmente
                            print("Partida con nombre: ", entrada, " eliminada exitosamente. ")
                            juego.colocar_barcos(Ingresar_cantidad(1))
                            eliminar_partida=False
                            #sale del bucle
        
        #Si ingresa algun dato diferente no elimina ni carga y 
        else:
            #prosigue con el juego normalmente
            juego.colocar_barcos(Ingresar_cantidad(1))

    #Si ingresa un dato diferente a 'si' entonces no hace ninguna modificacion a los datos y          
    else:   

        #prosigue con el juego normalmente   
        juego.colocar_barcos(Ingresar_cantidad(1))

    #Como el juego no se ha terminado entonces el switche se hace False hasta que esto cambie
    juego_terminado = False

    #Entra en el bucle de juego donde se disparara y mostrara el tablero
    while not juego_terminado:

        print("\n")
        #Muestra el tablero dos veces primero sin ocultar barcos y depues
        juego.mostrar_tablero()
        print("\n")
        #ocultando los barcos
        juego.imprimir_tablerocolor()
        print("\n")
        #pide los datos del disparo
        fila = Ingresar_cantidad(2)
        columna = Ingresar_cantidad(3)
        #Dispara en la fila y columna entregadas
        juego.disparar(fila, columna)
        #Elimina el barco del diccionario si hay un barco en esa posicion, si no no hace nada
        juego.eliminar_barco(fila, columna)

        #busca si el diccionario esta vacio, si es asi significa que no hay barcos restantes y el juego termina
        if juego.buscar_barco():
            print("\n")
            print("________________________")
            print(" ¡Felicidades, ganaste! ")
            return
        
        #Si todavia quedan barcos entonces pregunta si desea seguir jugando
        juego_terminado_respuesta = preguntar_seguir_jugando()

        #Si desea terminar el juego 
        if juego_terminado_respuesta==True:
            
            #pregunta si desea guardar la partida 
            if input("Desea guardar la partida? (ingrese si, o cualquier cosa si no lo desea): ") == "si" : 
                
                #si desea guardar la partida
                
                try:
                    
                    #primero intenta actualizarla buscando si hay alguna partida con el mismo nombre que tiene ahora mismo
                    # (Si no ha cargado partida antes este nombre deberia ser 'None' por lo tanto no encontraria partida para actualizar)
                    ControladorUsuario.updatePartida(juego)

                #Si no se encuentra partida para actualizar
                except UpdateSinExistenciaError:
                    
                    #Se procede a guardar como partida nueva 
                    print("No se encontro partida para actualizar, se procedera a guardar como partida nueva. ")

                    #activa el switche nombre_ para preguntar un nombre valido para el guardado de la partida
                    nombre_=True

                    #entra a dicho bucle
                    while nombre_:

                        #pide el nombre que desea
                        nombre=input("ingrese el nombre de la partida: ")

                        #Buscar el nombre en la DB para ver si esta repetido 
                        try:
                            ControladorUsuario.BuscarId(nombre)
                        
                        #Si el nombre esta repetido 
                        except InsertarNombreRepetidoError:

                            #Dice que ya hay una partida con ese nombre por lo tanto 
                            print("Ya hay una partida guardada con este nombre, ingrese uno diferente.")
                            #repite el bucle 
                        
                        # Si no hay ninguna partida con ese nombre
                        else:
                            
                            #entonces a esta partida le da el nombre que ingreso el usuario
                            juego.nombre=nombre
                            #Inserta el tablero de este juego a la BD
                            ControladorUsuario.InsertarTablero(juego)
                            #Inserta el diccionario de este juego a la BD
                            ControladorUsuario.insertarDiccionarios(juego)

                            #mensaje de confirmacion
                            print("Partida con nombre: ", nombre, " guardada correctamente. ")
                            #Termina todos los bucles anteriores para asi salir del juego
                            juego_terminado_respuesta=False
                            nombre_=False
                            juego_terminado=True  #Como el juego se va a terminar se hace el switche True
                            #Se dirige al mensaje final
                            
                #Si se encuentra una partida con el mismo nombre, entonces se actualiza
                else:

                    #Se da un mensaje de confirmacion
                    print("Partida actualizada correctamente. ")
                    #se cierran los anteriores bucles para terminar el juego
                    juego_terminado_respuesta=False     
                    juego_terminado=True    #Como el juego se va a terminar se hace el switche True
                    #Se dirige al mensaje final

            #Si no desea guardar la partida, entonces 
            else:

                #Sale de los bucles anteriores
                juego_terminado=True    #Como el juego se va a terminar se hace el switche True
                #Se dirige al mensaje final
               

                    

    #Finalmente imprime el mensaje final del juego
    print("\n")
    print(" ¡Gracias por jugar! ")



# Llamada a la función principal para iniciar el juego
Jugar()