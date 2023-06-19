'''
MAIN
'''

# pylint: disable=global-statement
# pylint: disable=invalid-name
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import sys, os, pygame
from clase_juego import Juego
from configuracion_imagenes import *
from modo import *
from datos_nivel_uno import nivel_uno
from datos_nivel_dos import nivel_dos
from datos_juego import esquiador, TAMANIO_PANTALLA

# PANTALLA
pygame.init()

# os.environ["SDL_VIDEO_CENTERES"] = '1'
# info = pygame.display.Info()
# ancho, alto = info.current_w, info.current_h

FPS = 18


RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)
fuente = pygame.font.Font("Recursos/Snowes.ttf", 60)

tiempo = 0

# Timer para el juego
TIMER_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(TIMER_EVENT, 1000)

def definir_accion_personaje(keys, jugador):

    if keys[pygame.K_RIGHT]:
        jugador.accion = "derecha"
    elif keys[pygame.K_LEFT]:
        jugador.accion = "izquierda"
    elif keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        jugador.accion = "salta"
    else:
        jugador.accion = "quieto"



niveles = [nivel_uno, nivel_dos]
juego = Juego(esquiador, niveles)



while True:

    RELOJ.tick(FPS)

    eventos = pygame.event.get()

    juego.manejar_eventos_juego(eventos)

    for evento in eventos:
        if evento.type == TIMER_EVENT:
            juego.update_personalizado()
            tiempo += 1
            if tiempo % 5 == 0:
                for enemigo in juego.niveles[juego.nivel_actual].enemigos:
                    enemigo.lanzar_proyectil()

    definir_accion_personaje(pygame.key.get_pressed(), juego.jugador)

    if esquiador.vidas_actuales == 0:
        juego.nivel_actual = 1

    juego.update(PANTALLA, fuente, tiempo)

    if get_mode() is True:
        for p in juego.niveles[juego.nivel_actual].plataformas:
            dibujar_borde_rectangulos(PANTALLA, p.lados, "Green")
        for e in juego.niveles[juego.nivel_actual].enemigos:
            dibujar_borde_rectangulos(PANTALLA, e.lados, "Blue")
        dibujar_borde_rectangulos(PANTALLA, juego.jugador.lados, "Red")
        for i in juego.niveles[juego.nivel_actual].items:
            dibujar_borde_rectangulos(PANTALLA, i.lados, "Yellow")
        for enemigo in juego.niveles[juego.nivel_actual].enemigos:
            for proyectil in enemigo.lista_proyectiles:
                dibujar_borde_rectangulos(PANTALLA, proyectil.lados, "Black")

    pygame.display.update()
