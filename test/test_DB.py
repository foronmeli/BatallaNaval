# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
#Lo importamos para incluir la ruta de busqueda de python
import sys
sys.path.append("src")
#Importar archivo de lógicxa para hacer las pruebas

# Importa la clase Tablero desde LogicTTY.logica
from Controller.controll import ControladorUsuario, UpdateSinExistenciaError,EliminarSinExistenciaError,InsertarNombreRepetidoError,NoHayPartidasGuardadasError
from Model.logica import Tablero


"""
    4 ERRORES 
    -Cuando se intenta hacer update sin tener un id igual en la base de datos,tablero.nombre
    -Cuando se intenta eliminar sin partidas cargadas
    -Cuando no hay partidas guardadas para cargar
    -cuando buscarId retorna un elemento con ese id significa que hay un elemento que ya tiene ese id entonces tira error

class UpdateSinExistenciaError(Exception):
    pass
class EliminarSinExistenciaError(Exception):
    pass
class NoHayPartidasGuardadasError(Exception):
    pass
class InsertarNombreRepetidoError(Exception):
    pass"""


class TestDataBase(unittest.TestCase):

      
    def test_update_error(self):

        #creamos un juego para actualizar
        juego1=Tablero(nombre="Walter")
        juego1.colocar_barcos(9)
        
        
        #reseteamos las tablas
        ControladorUsuario.EliminarTabla()
        ControladorUsuario.EliminarTablaDiccionarios()
        ControladorUsuario.CrearTabla()
        ControladorUsuario.CrearTablaDiccionarios()

        #intentamos actualizar el juego sin tenerlo guradado
        with self.assertRaises(UpdateSinExistenciaError):
            ControladorUsuario.updatePartida(juego1)

        return
    
    def test_update_normal(self):

        #creamos un juego para actualizar
        juego1=Tablero(nombre="Walter")
        juego1.colocar_barcos(9)

        #creamos otro juego con el mismo nombre para simular actualizacion
        juego2=Tablero(nombre="Walter")
        #Sin barcos para poder comprobar la accion
        
        #reseteamos las tablas
        ControladorUsuario.EliminarTabla()
        ControladorUsuario.EliminarTablaDiccionarios()
        ControladorUsuario.CrearTabla()
        ControladorUsuario.CrearTablaDiccionarios()

        #insertamos el primer juego a la tabla
        ControladorUsuario.insertarDiccionarios(juego1)
        ControladorUsuario.InsertarTablero(juego1)

        #actualizamos el juego 
        ControladorUsuario.updatePartida(juego2)

        self.assertNotEqual(juego1.tablero, juego2.tablero)
        matriz = [  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]    ]
        self.assertEqual(juego2.tablero, matriz )
        
        return
    
    def test_intentar_insertar_repetido_error(self):

        #creamos dos juegos diferentes con los mismos nombres
        juego1=Tablero(nombre="Walter")
        juego1.colocar_barcos(9)
        juego2=Tablero(nombre="Walter")
        juego2.colocar_barcos(9)
        
        #reseteamos las tablas
        ControladorUsuario.EliminarTabla()
        ControladorUsuario.EliminarTablaDiccionarios()
        ControladorUsuario.CrearTabla()
        ControladorUsuario.CrearTablaDiccionarios()

        #metemos el primer juego 
        ControladorUsuario.InsertarTablero(juego1)
        ControladorUsuario.insertarDiccionarios(juego1)

        #comprobamos que tire error
        with self.assertRaises(InsertarNombreRepetidoError):
            ControladorUsuario.BuscarId(juego2.nombre)
        
        with self.assertRaises(InsertarNombreRepetidoError):
            ControladorUsuario.BuscarId(juego2.nombre)

        return
    
    def test_insertar_normal(self):

        #creamos un juego para insertar
        juego1=Tablero(nombre="Lala")
        juego1.colocar_barcos(8)
  
        #reseteamos las tablas
        ControladorUsuario.EliminarTabla()
        ControladorUsuario.EliminarTablaDiccionarios()
        ControladorUsuario.CrearTabla()
        ControladorUsuario.CrearTablaDiccionarios()

        #insertamos el primer juego a la tabla
        ControladorUsuario.insertarDiccionarios(juego1)
        ControladorUsuario.InsertarTablero(juego1)
        
        #buscamos el juego
        resultado=ControladorUsuario.BuscarTableroId("Lala")
        
        
        self.assertEqual(resultado, juego1.tablero)
        
        return
        
    def test_eliminar_normal(self):

        #creamos un juego para eliminarlo luego
        juego1=Tablero(nombre="Lala")
        juego1.colocar_barcos(9)
             
        #reseteamos las tablas
        ControladorUsuario.EliminarTabla()
        ControladorUsuario.EliminarTablaDiccionarios()
        ControladorUsuario.CrearTabla()
        ControladorUsuario.CrearTablaDiccionarios()

        #insertamos el juego a la tabla
        ControladorUsuario.insertarDiccionarios(juego1)
        ControladorUsuario.InsertarTablero(juego1)

        #eliminamos la partida que acabamos de insertar
        ControladorUsuario.eliminarPartida("Lala")

    
        resultado=ControladorUsuario.BuscarId("Walter")
        self.assertEqual(None,resultado)

        return
    
    def test_eliminar_sin_partidas_guardadas_error(self):

             
        #reseteamos las tablas
        ControladorUsuario.EliminarTabla()
        ControladorUsuario.EliminarTablaDiccionarios()
        ControladorUsuario.CrearTabla()
        ControladorUsuario.CrearTablaDiccionarios()

        #Intentamos eliminar una partida con el id Walter que no se encuentra guardada 
        with self.assertRaises(EliminarSinExistenciaError):
            ControladorUsuario.eliminarPartida("Walter")
        
        return

    def test_mostrar_sin_partidas_guardadas_error(self):

             
        #reseteamos las tablas
        ControladorUsuario.EliminarTabla()
        ControladorUsuario.EliminarTablaDiccionarios()
        ControladorUsuario.CrearTabla()
        ControladorUsuario.CrearTablaDiccionarios()

        #Intentamos mostrar las partidas guardadas con el id Walter que no se encuentra guardada 
        with self.assertRaises(NoHayPartidasGuardadasError):
            ControladorUsuario.partidasCargadas()

        return
    
    def test_mostrar_normal(self):

        #creamos un juego para insertar
        juego1=Tablero(nombre="Lala")
        juego1.colocar_barcos(9)
             
        #reseteamos las tablas
        ControladorUsuario.EliminarTabla()
        ControladorUsuario.EliminarTablaDiccionarios()
        ControladorUsuario.CrearTabla()
        ControladorUsuario.CrearTablaDiccionarios()

        #insertamos el juego a la tabla
        ControladorUsuario.insertarDiccionarios(juego1)
        ControladorUsuario.InsertarTablero(juego1)

        #Mostramos la lista de partidas cargadas
        resultado=ControladorUsuario.partidasCargadas()

        self.assertEqual(resultado, ["Lala"])
        
        return
    
if __name__ == '__main__':
    unittest.main()
