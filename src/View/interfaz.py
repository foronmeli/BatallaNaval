# Importaciones necesarias
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

# Importación del módulo de lógica del juego
import sys
sys.path.append("src")
from Model.logica import Tablero

# Pantalla de bienvenida
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

        # Fondo con un color blanco para mayor contraste
        self.background_color = (1, 1, 1, 1)

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Etiqueta de bienvenida con una fuente grande y negrita
        welcome_label = Label(text="¡Bienvenido al juego de Batalla Naval!", font_size="40sp", font_name="Roboto-Bold", color=(1, 1, 1))
        layout.add_widget(welcome_label)

        # Botón para iniciar el juego
        start_game_button = Button(text="Iniciar Juego", size_hint_y=0.4, background_color=(0.196, 0.804, 0.196, 1))
        start_game_button.bind(on_press=self.start_game)
        layout.add_widget(start_game_button)

        # Botón para cargar partida (aún no implementado)
        load_game_button = Button(text="Cargar Partida", size_hint_y=0.4, background_color=(1, 0.843, 0, 1))
        load_game_button.bind(on_press=self.load_game)
        layout.add_widget(load_game_button)

        self.add_widget(layout)

    # Función para iniciar el juego
    def start_game(self, instance):
        self.manager.current = "game"

    # Función para cargar partida (no implementada todavía)
    def load_game(self, instance):
        pass

# Popup de alerta para indicar que un jugador ha ganado el juego
class AlertaJugador(Popup):
    def __init__(self, jugador, **kwargs):
        super(AlertaJugador, self).__init__(**kwargs)
        self.title = 'Alerta'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        contenido_caja = BoxLayout(orientation='vertical')
        
        mensaje_alerta = Label(text=f'¡El jugador {jugador} ha ganado el juego!')
        contenido_caja.add_widget(mensaje_alerta)
        self.content = contenido_caja

# Popup de impacto para indicar que un barco ha sido destruido
class MyPopupImpacto(Popup):
    def __init__(self, **kwargs):
        super(MyPopupImpacto, self).__init__(**kwargs)
        self.title = 'Alerta'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        content_layout = BoxLayout(orientation='vertical')
        
        mensaje_barco_destruido = Label(text='¡Barco destruido!')
        content_layout.add_widget(mensaje_barco_destruido)
        self.content = content_layout

# Pantalla del juego
class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        
        self.tablero_jugador = Tablero()
        self.tablero_jugador.colocar_barcos(20)

        contenedor_principal = BoxLayout(orientation="vertical")
        self.turno_label = Label(text="Vamos A jugar... ¡Tumba todos los barcos!", font_size="30sp", size_hint_y=0.2)
        contenedor_principal.add_widget(self.turno_label)

        contenedor_tablero = BoxLayout(orientation='vertical')
        for numero_fila in range(10):
            fila = BoxLayout(orientation="horizontal")
            for numero_columna in range(10):
                casilla = Button(text='O', font_size=20, disabled=False)
                casilla.fila = numero_fila
                casilla.columna = numero_columna
                casilla.bind(on_press=self.disparo_jugador)
                fila.add_widget(casilla)
            contenedor_tablero.add_widget(fila)

        contenedor_principal.add_widget(contenedor_tablero)
        self.add_widget(contenedor_principal)

    # Función para mostrar el popup de impacto cuando un barco es destruido
    def mostrar_popup_impacto(self):
        popup = MyPopupImpacto()
        popup.open()
    
    # Función para manejar el disparo del jugador
    def disparo_jugador(self, instance):
        resultado_disparo = self.tablero_jugador.disparar(instance.fila+1, instance.columna+1)

        if resultado_disparo == 'X':
            instance.text = 'X'
            instance.background_color = (255, 0, 0, 1)
            instance.disabled = True

            if self.tablero_jugador.barcos_destruidos():
                popup = AlertaJugador(jugador=1)
                popup.open()
            else:
                self.mostrar_popup_impacto()
        else:
            instance.text = ' '
            instance.background_color = (0.678, 0.847, 0.902, 5)
            instance.disabled = True

        if self.tablero_jugador.barcos_destruidos():
            popup = AlertaJugador(jugador=1)
            popup.open()
        elif self.tablero_jugador.casillas_presionadas() == 100:
            popup = AlertaJugador(jugador=1)
            popup.open()

# Administrador de pantallas del juego
class BattleshipScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(BattleshipScreenManager, self).__init__(**kwargs)
        
        self.add_widget(WelcomeScreen(name="welcome"))
        self.add_widget(GameScreen(name="game"))

# Clase principal de la aplicación
class BattleshipApp(App):
    def build(self):
        return BattleshipScreenManager()

# Ejecutar la aplicación si este script es el programa principal
if __name__ == '__main__':
    BattleshipApp().run()