from flask import Blueprint, render_template, request
blueprint = Blueprint( "vista_usuarios", __name__, "templates" )

import sys
sys.path.append("src")
from Model.logica import *
from Controller.controll import *

import sys
sys.path.append("src")

@blueprint.route("/")
def index():
    return render_template("index.html")

@blueprint.route("/crear_tablero")
def tablero():
    return render_template("crear_tablero.html")
    
@blueprint.route("/juego")
def juego():
    try:
        cantidad_barcos = int(request.args.get("cantidad"))  # Convertir la cantidad de barcos a entero
    except ValueError:
        mensaje_error = "La cantidad de barcos debe ser un número entero."
        return render_template('juego.html', error=mensaje_error)
    try:
        tablero = Tablero()
        tablero.colocar_barcos(cantidad_barcos)  # Colocar la cantidad especificada de barcos en el tablero
        tablero_html = tablero.imprimir_tablero_html()
        return render_template("juego.html", tablero_html=tablero_html)
    except ErrorCoordenadasVacias:
        mensaje_error = "La cantidad de barcos no puede ser vacía."
        return render_template('juego.html', error=mensaje_error)
    except ErrorCoordenadasString:
        mensaje_error = "La cantidad de barcos debe ser un número entero válido."
        return render_template('juego.html', error=mensaje_error)
    except ErrorCoordenadasNegativas:
        mensaje_error = "La cantidad de barcos no puede ser negativa."
        return render_template('juego.html', error=mensaje_error)
    except ErrorCoordenadasFueraRango:
        mensaje_error = "La cantidad de barcos debe estar entre 1 y 20."
        return render_template('juego.html', error=mensaje_error)
    except Exception as e:
        mensaje_error = f"Error: {str(e)}"
        return render_template('juego.html', error=mensaje_error)

@blueprint.route("/guardar_partida")
def guardar_partida():
    tablero = request.args["tablero"]
    return render_template("guardar_partida.html", tablero_html=tablero)

@blueprint.route("/guardado")
def guardado():
    nombre = request.args["nombre"]
    tablero_html = request.args["tablero"]
    tablero = Tablero.from_html(tablero_html)
    try:
        #primero intenta actualizarla buscando si hay alguna partida con el mismo nombre que tiene ahora mismo
        # (Si no ha cargado partida antes este nombre deberia ser 'None' por lo tanto no encontraria partida para actualizar)
        ControladorUsuario.updatePartida(tablero)

    #Si no se encuentra partida para actualizar
    except UpdateSinExistenciaError:
        #Se procede a guardar como partida nueva 
        try:
            ControladorUsuario.BuscarId(nombre)
        #Si el nombre esta repetido 
        except InsertarNombreRepetidoError:
            #Dice que ya hay una partida con ese nombre por lo tanto 
            mensaje = "Ya hay una partida guardada con este nombre, ingrese uno diferente."
            return render_template("guardado.html", mensaje=mensaje)
        else:
            #Inserta el tablero de este juego a la BD
            ControladorUsuario.InsertarTablero(tablero)
            #Inserta el diccionario de este juego a la BD
            ControladorUsuario.insertarDiccionarios(tablero)
            mensaje = "Partida guardada correctamente."
            return render_template("guardado.html", mensaje=mensaje)
    except Exception as e:
        mensaje = f"Error al guardar la partida: {str(e)}"
        return render_template("guardado.html", mensaje=mensaje)
    return render_template("index.html")

@blueprint.route("/seleccionar_partidas")
def seleccionar_partida():
    try:
        listado_partidas = ControladorUsuario.partidasCargadas()
        return render_template('seleccionar_partidas.html', partidas=listado_partidas)
    except NoHayPartidasGuardadasError:
        #Si no hay partidas guardadas para eliminar
        mensaje_error = "No hay partidas guardadas. "
        return render_template('seleccionar_partidas.html', error=mensaje_error)

@blueprint.route("/eliminar_partida")
def eliminar_partida():
    return render_template("eliminar_partida.html")

@blueprint.route("/eliminado")
def eliminado():
    nombre_partida = request.args["nombre_partida"]
    try:
        ControladorUsuario.eliminarPartida(nombre_partida)
        mensaje = "Partida eliminada correctamente."
    except EliminarSinExistenciaError:
        mensaje = "No se encontró la partida especificada."
    return render_template("eliminado.html", mensaje=mensaje)
