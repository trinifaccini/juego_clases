# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


'''
CLASE JUEGO
'''

class Juego():

    def __init__(self, jugador, niveles:list) -> None:

        self.jugador = jugador
        self.nivel_actual = 0
        self.niveles = niveles

        
    def posicionar_textos(self, pantalla:dict, textos) -> None:

        for texto in textos:
            pantalla['rectangulo'].blit(texto['texto'], (texto['pos_x'], texto['pos_y']))

    def update(self, pantalla:dict, fuente, tiempo_transcurrido:float) -> None:

        self.niveles[self.nivel_actual].update(pantalla['rectangulo'], self.jugador)

        texto = fuente.render(f"Vidas: {self.jugador.vidas_actuales}", False, "Green", "Blue")
        ancho_texto = texto.get_width()

        texto_vidas = {
            "texto": texto,
            "pos_x": pantalla['ancho']-ancho_texto,
            "pos_y": 0
        }

        texto = fuente.render(f"Puntos: {self.jugador.puntos}", False, "Green", "Blue")

        texto_puntos = {
            "texto": texto,
            "pos_x": 0,
            "pos_y": 0
        }

        texto = fuente.render(f"Tiempo:{1000-tiempo_transcurrido}", False, "Green", "Blue")
        ancho_texto = texto.get_width()

        texto_tiempo = {
            "texto": texto,
            "pos_x": pantalla['ancho']/2-(ancho_texto/2),
            "pos_y": 0
        }

        textos = [texto_vidas, texto_puntos, texto_tiempo]

        self.posicionar_textos(pantalla, textos)
