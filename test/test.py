# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
#Lo importamos para incluir la ruta de busqueda de python
import sys
sys.path.append("src")
#Importar archivo de lógicxa para hacer las pruebas

# Importa la clase Tablero desde LogicTTY.logica
from Model.logica import Tablero, ErrorCoordenadasFueraRango, ErrorCoordenadasNegativas,ErrorCoordenadasString,ErrorCoordenadasVacias



class TestTablero(unittest.TestCase):

# Prueba para verificar el tamaño del tablero
    def test_tamaño_creado_1(self):

        # Configuración del tablero
        filas=10
        columnas=10
        tablero = Tablero(filas,columnas)

        # Tamaño de tablero esperado
        expected=filas*columnas

        resultado=tablero.contador_filas_columnas()
        
        
        self.assertEqual(expected,resultado)

# Prueba para verificar el tamaño del tablero
    def test_tamaño_creado_2(self):

        # Configuración del tablero
        filas=5
        columnas=5
        tablero = Tablero(filas,columnas)

        # Tamaño de tablero esperado
        expected=filas*columnas

        resultado=tablero.contador_filas_columnas()
        
        
        self.assertEqual(expected,resultado)

# Prueba para verificar si hay barcos
    def test_hay_barcos_1(self):

        # Configuración del tablero
        filas=10
        columnas=10
        tablero = Tablero(filas,columnas)
        tablero.colocar_barcos(2)

        # resultado esperado
        expected=False

        resultado=tablero.buscar_barco()
        
        
        self.assertEqual(expected,resultado)
        

# Prueba para verificar si no hay barcos
    def test_no_hay_barcos_1(self):

        # Configuración del tablero
        filas=10
        columnas=10
        tablero = Tablero(filas,columnas)
        tablero.colocar_barcos(1)
        tablero.barcos={}

        # resultado esperado
        expected=True

        resultado=tablero.buscar_barco()
        
        self.assertEqual(expected,resultado)
    

# Prueba para verificar error
    def test_error_entrada_str_1(self):

        # Configuración del tablero
        filas=10
        columnas=10
        tablero = Tablero(filas,columnas)

        with self.assertRaises(ErrorCoordenadasString):
            tablero.colocar_barcos("s")

# Prueba para verificar error
    def test_error_entrada_negativa_1(self):

        # Configuración del tablero
        filas=10
        columnas=10
        tablero = Tablero(filas,columnas)

        with self.assertRaises(ErrorCoordenadasNegativas):
            tablero.colocar_barcos(-2)

# Prueba para verificar error
    def test_error_entrada_vacia_1(self):

        # Configuración del tablero
        filas=10
        columnas=10
        tablero = Tablero(filas,columnas)

        with self.assertRaises(ErrorCoordenadasVacias):
            tablero.colocar_barcos()

# Prueba para verificar error
    def test_error_entrada_fuera_rango_1(self):

        # Configuración del tablero
        filas=10
        columnas=10
        tablero = Tablero(filas,columnas)


        with self.assertRaises(ErrorCoordenadasFueraRango):
            tablero.colocar_barcos(888)

# Prueba para verificar si no gano
    def test_no_ganar_1(self):

        # Configuración del tablero
        filas=10
        columnas=10
        tablero = Tablero(filas,columnas)
        tablero.colocar_barcos(3)

        # resultado esperado
        expected=False

        #mirar si no gano
        resultado=tablero.buscar_barco()
        
        self.assertEqual(expected,resultado)

# Prueba para verificar si gana
    def test_ganar_1(self):

        # Configuración del tablero
        filas=10
        columnas=10
        tablero = Tablero(filas,columnas)
        tablero.colocar_barcos(2)
        tablero.barcos={}

        # resultado esperado
        expected=True

        #mirar si no gano
        resultado=tablero.buscar_barco()
        
        self.assertEqual(expected,resultado)

#PRUEBAS DE DISPARO ________________________________________________

# Prueba para verificar si el disparo golpea barco
    def test_disparar_acierto_1(self):

        # Configuración del tablero
        tablero = Tablero()
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]
                         

        # Resultado esperado
        expected="X"

        resultado=tablero.disparar(1,1)

        self.assertEqual(expected,resultado)

# Prueba para verificar si el disparo golpea barco
    def test_disparar_acierto_2(self):

        # Configuración del tablero
        tablero = Tablero()
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]
                         

        # Resultado esperado
        expected="X"

        resultado=tablero.disparar(2,2)

        self.assertEqual(expected,resultado)

# Prueba para verificar si el disparo golpea agua
    def test_disparar_falla_1(self):

        # Configuración del tablero
        tablero = Tablero()
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]
                         

        # Resultado esperado
        expected="~"

        resultado=tablero.disparar(1,2)

        self.assertEqual(expected,resultado)

# Prueba para verificar si el disparo golpea agua
    def test_disparar_falla_2(self):

        # Configuración del tablero
        tablero = Tablero()
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]
                         

        # Resultado esperado
        expected="~"

        resultado=tablero.disparar(5,5)

        self.assertEqual(expected,resultado)

# Prueba para verificar si el disparo esta fuera de rango
    def test_disparar_error_rango_1(self):

        # Configuración del tablero
        tablero = Tablero()
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]

        with self.assertRaises(ErrorCoordenadasFueraRango):
            tablero.disparar(11,12)

# Prueba para verificar si el disparo recibe coordenadas negativas
    def test_disparar_error_negativas_1(self):

        # Configuración del tablero
        tablero = Tablero()
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]

        with self.assertRaises(ErrorCoordenadasNegativas):
            tablero.disparar(-1,-2)

# Prueba para verificar si el disparo recibe coordenadas nulas
    def test_disparar_error_vacias_1(self):

        # Configuración del tablero
        tablero = Tablero()
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]

        with self.assertRaises(ErrorCoordenadasVacias):
            tablero.disparar()

# Prueba para verificar si el disparo recibe coordenadas en string
    def test_disparar_error_string_1(self):

        # Configuración del tablero
        tablero = Tablero()
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]

        with self.assertRaises(ErrorCoordenadasString):
            tablero.disparar("s","d")

# Prueba para verificar si el disparo golpea agua de nuevo
    def test_disparar_mismo_lugar_agua(self):

        # Configuración del tablero
        tablero = Tablero()
        #                          3   4
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","~","O","O","O","O","O","O","O"],   #3
                         ["O","O","O","X","O","O","O","O","O","O"],   #4
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]
                         

        # Resultado esperado
        expected=None

        resultado=tablero.disparar(3,3)

        self.assertEqual(expected,resultado)

# Prueba para verificar si el disparo golpea a un barco destruido
    def test_disparar_barco_destruido(self):

        # Configuración del tablero
        tablero = Tablero()
        #                          3   4
        tablero.tablero=[["B","O","O","O","O","O","O","O","O","O"],
                         ["O","B","O","O","O","O","O","O","O","O"],
                         ["O","O","~","O","O","O","O","O","O","O"],   #3
                         ["O","O","O","X","O","O","O","O","O","O"],   #4
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","O"],
                         ["O","O","O","O","O","O","O","O","O","B"]]
                         

        # Resultado esperado
        expected=None

        resultado=tablero.disparar(4,4)

        self.assertEqual(expected,resultado)

if __name__ == '__main__':
    unittest.main()

