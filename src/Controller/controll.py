#Imports necesarios
import sys
import os
import psycopg2

# Agregar el directorio padre al path para permitir importaciones relativas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importaciones de módulos propios
from Model.logica import Tablero
from Model import SecretConfig


#Errores
class UpdateSinExistenciaError(Exception):
    pass
class EliminarSinExistenciaError(Exception):
    pass
class NoHayPartidasGuardadasError(Exception):
    pass
class InsertarNombreRepetidoError(Exception):
    pass

class ControladorUsuario:
    """Clase para controlar la base de datos"""

    def crear_cursor():
        """Crear la conexión a la base de datos y retorna un cursor para hacer consultas"""
        connection=psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password= SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port= SecretConfig.PGPORT)
        #Todas las instrucciones se ejecutan a través de un cursor
        cursor=connection.cursor()
        return cursor 

    def CrearTabla():
        """ Crea la tabla de tableros en la BD """
        ejecucion = """create table tableros (
            id varchar( 20 ) not null,
            fila integer not null,
            columna integer not null,
            valor varchar(20) not null
            ); """
        #Crear un cursor
        cursor = ControladorUsuario.crear_cursor()
        #Crea las columnas de la tabla
        cursor.execute(ejecucion)
        #aplica los cambios
        cursor.connection.commit()
    
    def CrearTablaDiccionarios():
        """ Crea la tabla de diccionarios en la BD """

        #Crea un cursor
        cursor = ControladorUsuario.crear_cursor()

        #Crea las columnas de la tabla
        cursor.execute("""create table diccionarios (
  id varchar( 20 ) not null,
  nombre text not null,
  fila integer not null,
  columna integer not null
); """)
        
        #aplica los cambios
        cursor.connection.commit()

    def insertarDiccionarios(tablero: Tablero):
        """Recibe un objeto tablero e inserta el diccionario en la DB"""

        #recorre el diccionario barcos del objeto tablero
        for clave, valor in tablero.barcos.items():
            tupla1 = valor[0]  
            tupla2 = valor[1]

            #Crear un cursor
            cursor = ControladorUsuario.crear_cursor()

            #Inserta cada uno de los datos que esten dentro del diccionario 
            cursor.execute( f"""insert into diccionarios (id, nombre, fila, columna) 
                                values ('{tablero.nombre}', '{clave}', '{tupla1}','{tupla2}')""" )   
            
            #Aplica los cambios
            cursor.connection.commit()
            
    def InsertarTablero( tablero : Tablero ):
        """Recibe un objeto tablero e inserta la matriz tablero en la DB"""
        
        contadorFilas=0
        for filas in (tablero.tablero):
        
            contador=0

            for j in (filas):
                
                #crea un cursor
                cursor = ControladorUsuario.crear_cursor()

                #inserta cada valor dentro de la tabla con su respectiva fila, columna, valor y nombre/id
                cursor.execute( f"""insert into tableros (id, fila, columna, valor) 
                                values ('{tablero.nombre}', '{contadorFilas}', '{contador}','{j}')""" )    
                

                cursor.connection.commit()
                            
                contador+=1  

            contadorFilas+=1    

    def BuscarTableroId( id ):
        """ Retorna la matriz tablero de la base de datos """

        tablero=[]
        for i in range(10):
            tablero.append([])
            for j in range(10):

                #crea un cursor
                cursor = ControladorUsuario.crear_cursor()
                
                #Selecciona cada uno de los datos por fila, columna y nombre/id y organiza su valor en una matriz para luego retornarla 
                cursor.execute(f"""select valor from tableros where id = '{id}' and fila = '{i}' and columna = '{j}'""" )
                fila = cursor.fetchone()

                

                tablero[i].append(fila[0])
        
        return tablero
    
    def BuscarDiccionarioId( id ):
        """ Retorna el diccionario con los barcos dese la base de datos"""

        #crea un cursor
        cursor = ControladorUsuario.crear_cursor()

        diccionario={}
       
       #Selecciona el nombre, la fila y la columna de todos los datos con ese id
        cursor.execute(f"""select nombre, fila , columna from diccionarios where id = '{id}' """ )
        retorno = cursor.fetchall()

        
        #Los añade y organiza en el diccionario
        for i in retorno:
            diccionario[i[0]] = (i[1],i[2])
        
        return diccionario
    
    def BuscarId( id ):
        """Sirve para comprobar si hay datos con el mismo id"""

        cursor = ControladorUsuario.crear_cursor()

        #Selecciona los datos con dicho id
        cursor.execute(f"""select id from tableros where id = '{id}' """)

        retorno=cursor.fetchone()

        #Si encuentra algun dato con el id repetido levanta un error
        if retorno :
            raise InsertarNombreRepetidoError()
        
        #Si no encuentra ningun dato con ese id retorna None
        return retorno

    def EliminarTabla():
        """ Borra la tabla de taleros de la BD"""

        cursor = ControladorUsuario.crear_cursor()

        cursor.execute("""drop table tableros""" )
        
        cursor.connection.commit()

    def EliminarTablaDiccionarios():
        """ Borra la tabla de diccionarios de la BD """

        cursor = ControladorUsuario.crear_cursor()

        cursor.execute("""drop table diccionarios""" )
       
        cursor.connection.commit()
   
    def partidasCargadas():
        """Retorna una lista con los nombres de las partidas que hay guardadas en la DB"""

        cursor = ControladorUsuario.crear_cursor()
        
        #Selecciona uno de cada id que haya, es decir todos los ids pero sin repetir
        cursor.execute("""SELECT id, nombre FROM diccionarios;""")

        resultado=cursor.fetchall()

        #Si no encuentra ninguno significa que no hay partidas guardadas, entonces lanza error
        if not resultado:
            raise NoHayPartidasGuardadasError()

        ids = []
        #Añade a la lista cada nombre recolectado
        for i in resultado:
            ids.append(i[0])

        return ids
    
    def eliminarPartida( id ):
        """Recibe el id de la partida que desea eliminar de la DB"""

        cursor = ControladorUsuario.crear_cursor()
        #Busca si hay algun dato con dicho id
        cursor.execute(f"""select id from diccionarios where id = '{id}' """)
        retorno=cursor.fetchone()
        #Si no encuentra un dato con ese id levanta error
        if not retorno:
            raise EliminarSinExistenciaError()
        

        #Si encuentra dato con ese id entonces elimina los datos con ese id de la tabla de diccionarios y tableros
        cursor = ControladorUsuario.crear_cursor()
        cursor.execute( f"""delete from tableros where id= '{id}'""")   
        cursor.connection.commit()

        cursor = ControladorUsuario.crear_cursor()
        cursor.execute( f"""delete from diccionarios where id= '{id}'""")  
        cursor.connection.commit()
        
        return
    
    def updatePartida( tablero : Tablero):
        """Recibe el tablero que desea actualizar y lo actualiza si es posible"""

        #Por medio de la funcion buscarId se asegura de que haya algun dato con dicho id en la DB
        try:
            ControladorUsuario.BuscarId(tablero.nombre)

        except InsertarNombreRepetidoError:
            #Si encuentra algun dato con ese id entonces cambia los datos del tablero y del diccionario con ese id por los valores actuales

            contadorFilas=0

            for filas in (tablero.tablero):
            
                contador=0

                for j in (filas):
                    
                    cursor = ControladorUsuario.crear_cursor()


                    cursor.execute( f"""update tableros set valor = '{j}' where id = '{tablero.nombre}' and fila = '{contadorFilas}' and columna = '{contador}' """)   
                    

                    cursor.connection.commit()
                                
                    contador+=1  

                contadorFilas+=1    
            
            cursor = ControladorUsuario.crear_cursor()
            cursor.execute( f"""delete from diccionarios where id= '{tablero.nombre}'""")
            cursor.connection.commit()
            ControladorUsuario.insertarDiccionarios(tablero)

        else:
            #Si no encuentra ningun dato con ese id en la DB levanta error 
            raise UpdateSinExistenciaError()
        
        return