#Importaciones necesarias
import random
import numpy as np
from colorama import Fore, Style

# Definición de excepciones personalizadas
class ErrorCoordenadasString(Exception):
    pass

class ErrorCoordenadasNegativas(Exception):
    pass

class ErrorCoordenadasVacias(Exception):
    pass

class ErrorCoordenadasFueraRango(Exception):
    pass


# Clase del tablero
class Tablero:
    def __init__(self, filas=10, columnas=10,nombre=None):
        # Definición del tamaño del tablero y la matriz que lo representa
        self.filas = filas
        self.columnas = columnas
        self.tablero = [['O' for _ in range(self.columnas)] for _ in range(self.filas)]
        # Diccionario para almacenar las posiciones de los barcos en el tablero
        self.barcos = {}
        self.nombre=nombre

    # Método para colocar aleatoriamente los barcos en el tablero
    def hacer_barcos(self, i):
        while True:
            num_fila = random.randint(0, 9)
            num_columna = random.randint(0, 9)
            if self.tablero[num_fila][num_columna] == "O":
                self.tablero[num_fila][num_columna] = "B"
                self.barcos["barco " + str(i)] = (num_fila, num_columna)
                break

    # Método para colocar la cantidad especificada de barcos en el tablero
    def colocar_barcos(self, cantidad_barcos="_______________________"):

        if cantidad_barcos=="_______________________":
            raise ErrorCoordenadasVacias
        if isinstance(cantidad_barcos, str):
            raise ErrorCoordenadasString
        if cantidad_barcos<0:
            raise ErrorCoordenadasNegativas
        if not(0 < cantidad_barcos <= 20):
            raise ErrorCoordenadasFueraRango

        for i in range(cantidad_barcos):
            self.hacer_barcos(i)
    
    # Método para mostrar el tablero en la consola con colores
    def mostrar_tablero(self):
        """Muestra el tablero sin ocultar """

        # Obtener dimensiones del tablero
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        
        # Calcular la longitud máxima de un número de columna
        max_longitud_columna = len(str(columnas))
        
        # Imprimir los índices de las columnas
        print("   ", end="")
        for j in range(1, columnas + 1):
            print(Fore.RESET + f"{j:<{max_longitud_columna}}", end="")
        print()

        # Imprimir el tablero con los índices de fila y color
        for i, fila in enumerate(self.tablero):
            # Imprimir índice de fila
            print(Fore.RESET + f"{i+1:<3}", end="")
            fila_pintada = []
            for celda in fila:
                if celda == 'B':
                    fila_pintada.append(Fore.RED + celda)
                elif celda == 'O':
                    fila_pintada.append(Fore.BLUE + celda)
                elif celda == '~':
                    fila_pintada.append(Fore.BLUE + 'O')
                elif celda == 'X':
                    fila_pintada.append(Fore.YELLOW + celda)
                else:
                    fila_pintada.append(celda)
            print(' '.join(fila_pintada))
        
    # Método para imprimir el tablero sin colores
    def imprimir_tablero(self):
        for fila in self.tablero:
            fila_modificada = [Tablero.cambio_letra(c) for c in fila]
            print(' '.join(fila_modificada))

    def imprimir_tablero_html(self):
        html = "<table style='background: transparent;'>"
        for fila in self.tablero:
            html += "<tr>"
            for celda in fila:
                html += f"<td>{celda}</td>"
            html += "</tr>"
        html += "</table>"
        return html


    # Método estático para cambiar 'B' por 'O' en la impresión del tablero
    @staticmethod
    def cambio_letra(letra):
        if letra == 'B':
            return 'O'
        return letra
    
    # Método para simular un disparo en el tablero
    def disparar(self, fila="_____", columna="_____"):

        if fila=="_____" or columna=="_____":
            raise ErrorCoordenadasVacias
        if isinstance(fila, str) or isinstance(columna, str):
            raise ErrorCoordenadasString
        if fila<0 or columna<0:
            raise ErrorCoordenadasNegativas
        if not(1 <= fila <= 10 or 1 <= columna <= 10):
            raise ErrorCoordenadasFueraRango
    

        if self.tablero[fila - 1][columna - 1] == "X" or self.tablero[fila - 1][columna - 1] == "~":
            print("Ya disparaste en esta posición")
            return 
        if self.tablero[fila - 1][columna - 1] == "B":
            print(" ¡Barco destruido! ")
            self.tablero[fila - 1][columna - 1] = "X"
            return "X"
        else:
            print("El disparo ha dado en el agua")
            self.tablero[fila - 1][columna - 1] = "~"
            return "~"
    
    # Método para eliminar un barco del diccionario cuando es destruido
    def eliminar_barco(self, fila, columna):
        barco_a_eliminar = None
        for nombre_barco, coord_barco in self.barcos.items():
            if (fila - 1, columna - 1) == coord_barco:
                barco_a_eliminar = nombre_barco
                break

        if barco_a_eliminar is not None:
            del self.barcos[barco_a_eliminar]

        return
    
    # Método para verificar si todos los barcos han sido destruidos
    def buscar_barco(self):
        return len(self.barcos) == 0

    # Método para imprimir el tablero sin colores
    def imprimir_tablerocolor(self):
        """Muestra el tablero ocultando los barcos"""

        # Convertir el tablero a un array de numpy
        tablero_np = np.array(self.tablero)
        
        # Obtener dimensiones del tablero
        filas, columnas = tablero_np.shape
        
        # Imprimir los índices de las columnas con color verde
        print("   ", end="")
        for j in range(1, columnas + 1):
            print(Fore.YELLOW + f"{j:<4}", end="")
        print(Style.RESET_ALL)
        
        # Imprimir el tablero con los índices de fila y color
        for i in range(filas):
            # Imprimir índice de fila con color verde
            print(Fore.YELLOW + f"{i+1:<3}", end="")
            for j in range(columnas):
                # Cambiar 'B' por 'O' antes de imprimir
                if tablero_np[i, j] == 'B':
                    tablero_np[i, j] = 'O'
                # Imprimir cada celda del tablero
                print(Fore.RESET + f"{tablero_np[i, j]:<4}", end="")
            # Restablecer color después de imprimir una fila completa
            print(Style.RESET_ALL)

    # Método para verificar si todos los barcos han sido destruidos
    def barcos_destruidos(self):
        return len(self.barcos) == 0
    
    # Método para contar las casillas presionadas (con barcos destruidos o agua)
    def casillas_presionadas(self):
        total = 0
        for fila in self.tablero:
            total += fila.count('X') + fila.count('~')
        return total
    
    def contador_filas_columnas(self):
        cont_celdas = 0
        for fila in self.tablero:
            for celda in fila:  # Iterar sobre las celdas en cada fila
                cont_celdas += 1
        return cont_celdas