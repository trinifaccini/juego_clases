'''
MAIN
'''

# pylint: disable=global-statement
# pylint: disable=invalid-name
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import sys
import pygame
from clase_item import Item
from clase_jugador import Jugador
from clase_enemigo import Enemigo
from clase_plataforma import Plataforma
from clase_proyectil import Proyectil
from clase_nivel import Nivel
from clase_juego import Juego
from configuracion_imagenes import *
from modo import *

# PANTALLA

ANCHO_PANTALLA, ALTO_PANTALLA = 1000, 450
TAMANIO_PANTALLA = (ANCHO_PANTALLA, ALTO_PANTALLA)
FPS = 18

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)

# FONDO
fondo = pygame.image.load("Recursos/Fondos/fondo_nivel_1.png")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)

# PLATAFORMAS

ALTO_PISO = 20
piso = Plataforma(
    (ANCHO_PANTALLA, ALTO_PISO), "Recursos/Plataformas/plataforma_tierra_nieve.png",
    {"x": 0, "y": ALTO_PANTALLA-ALTO_PISO}, "piso")

ALTO_PLATAFORMA = 40
plataforma_uno = Plataforma(
    (200, ALTO_PLATAFORMA),"Recursos/Plataformas/plataforma_tierra_nieve.png",
    {"x": 200, "y": ALTO_PANTALLA-ALTO_PISO-ALTO_PLATAFORMA-70}, "plataforma")

lista_plataformas = [piso, plataforma_uno]

# ITEMS
coca = Item(
    (25,55),"Recursos/Obstaculos/coca_dibujo.png",
    {"x": 200, "y": ALTO_PANTALLA-ALTO_PISO-ALTO_PLATAFORMA-70}, 0, 100)

hamburguesa = Item(
    (60,40),"Recursos/Obstaculos/hamburguesa.png",
    {"x": 200, "y": ALTO_PANTALLA-ALTO_PISO-ALTO_PLATAFORMA-70}, 100, 0)

# TRAMPAS
ALTO_TRAMPA_PASTO = 70
trampa_pasto = Item(
    (50,ALTO_TRAMPA_PASTO),"Recursos/Obstaculos/trampa_pasto.png",
    {"x": plataforma_uno.lados['main'].x,
     "y": plataforma_uno.lados['main'].y-ALTO_TRAMPA_PASTO}, 
    0, -100, True)

ALTO_TRAMPA_ARBOL = 200
trampa_arbol = Item(
    (70,ALTO_TRAMPA_ARBOL),"Recursos/Obstaculos/arbol_1.png",
    {"x": plataforma_uno.lados['main'].x+100,
     "y": plataforma_uno.lados['main'].y-ALTO_TRAMPA_ARBOL}, 
    0, -100, True)


items = [coca, trampa_pasto,trampa_arbol]

# PERSONAJE
ANCHO_PERSONAJE = 80
ALTO_PERSONAJE = 95
tamanio = (ANCHO_PERSONAJE, ALTO_PERSONAJE)
pos_inicial = {"x": ANCHO_PANTALLA/2,
               "y": ALTO_PANTALLA-ALTO_PERSONAJE-ALTO_PISO}
velocidad = 10  # Cuanto avanza o retrocede el personaje en pixeles


esquiador = Jugador(
    tamanio, diccionario_animaciones_personaje, pos_inicial, 3000)

proyectil = Proyectil(
    (20,20),"Recursos/Obstaculos/bola_nieve_1.png",
    {"x": 200, "y": ALTO_PANTALLA-ALTO_PISO-ALTO_PLATAFORMA-70}, 100)


enemigo_uno = Enemigo(
    tamanio, diccionario_animaciones_oso,
    {"x": ANCHO_PANTALLA/2+100, "y": ALTO_PANTALLA-ALTO_PERSONAJE-ALTO_PISO},
    1000, 100, piso)

# enemigo_dos = Enemigo(
#     tamanio, diccionario_animaciones_yeti,
#     {"x": plataforma_uno.lados['main'].x,
#      "y": plataforma_uno.lados['main'].y-ALTO_PERSONAJE},
#     1000, 100, plataforma_uno,
#     "Recursos/Obstaculos/bola_nieve_1.png")

enemigos = []
enemigos = [enemigo_uno]

# PROYECTILES


# TEXTO
fuente = pygame.font.SysFont("Arial", 40)

# NIVEL
nivel_uno = Nivel(fondo, lista_plataformas, enemigos, items)
niveles = [nivel_uno]
juego = Juego(esquiador, niveles)

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

def manejar_eventos_juego(eventos):

    for evento in eventos:

        match evento.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            case pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    change_mode()

dict_pantalla = {
    "rectangulo": PANTALLA,
    "ancho": ANCHO_PANTALLA,
    "alto": ALTO_PANTALLA
}


while True:

    RELOJ.tick(FPS)

    eventos = pygame.event.get()

    manejar_eventos_juego(eventos)

    for evento in eventos:
        if evento.type == TIMER_EVENT:
            tiempo += 1

            if tiempo % 5 == 0:
                for enemigo in juego.niveles[juego.nivel_actual].enemigos:
                    enemigo.lanzar_proyectil()

    definir_accion_personaje(pygame.key.get_pressed(), esquiador)

    #if esquiador.vidas_actuales <= 0:
        # pygame.quit()
        # sys.exit(0)

    juego.update(dict_pantalla, fuente, tiempo)

    if get_mode() is True:
        for p in lista_plataformas:
            dibujar_borde_rectangulos(PANTALLA, p.lados, "Green")
        for e in enemigos:
            dibujar_borde_rectangulos(PANTALLA, e.lados, "Blue")
        dibujar_borde_rectangulos(PANTALLA, esquiador.lados, "Red")
        for i in items:
            dibujar_borde_rectangulos(PANTALLA, i.lados, "Yellow")
        for enemigo in juego.niveles[juego.nivel_actual].enemigos:
            for proyectil in enemigo.lista_proyectiles:
                dibujar_borde_rectangulos(PANTALLA, proyectil.lados, "Black")

    pygame.display.update()
