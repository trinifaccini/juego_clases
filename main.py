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
from configuracion_imagenes import *
from modo import *

################################################################

# Blitear y actualizar todos los objetos de mi pantalla
def actualizar_pantalla(pantalla, fondo, textos:list, lista_plataformas, jugador, enemigos, items):

    pantalla.blit(fondo, (0, 0))

    for texto in textos:
        pantalla.blit(texto['texto'], (texto['pos_x'], texto['pos_y']))

    # Plataformas
    for p in lista_plataformas:
       p.update(pantalla)


    # Personajes
    jugador.update(pantalla, lista_plataformas, enemigos)

    for enemigo in enemigos:
        enemigo.update(pantalla)

    for item in items:
        item.update(pantalla)



########################################################################

# PANTALLA

ANCHO_PANTALLA, ALTO_PANTALLA = 1200, 650
TAMANIO_PANTALLA = (ANCHO_PANTALLA, ALTO_PANTALLA)
FPS = 18

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)

# FONDO
fondo = pygame.image.load("Recursos/Fondos/fondo_negro.jpeg")
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
    (70,100),"Recursos/Obstaculos/coca.png",
    {"x": 200, "y": ALTO_PANTALLA-ALTO_PISO-ALTO_PLATAFORMA-70})

hamburguesa = Item(
    (60,40),"Recursos/Obstaculos/hamburguesa.png",
    {"x": 200, "y": ALTO_PANTALLA-ALTO_PISO-ALTO_PLATAFORMA-70})

items = [coca,hamburguesa]

# PERSONAJE
ANCHO_PERSONAJE = 80
ALTO_PERSONAJE = 95 
tamanio = (ANCHO_PERSONAJE, ALTO_PERSONAJE)
pos_inicial = {"x": ANCHO_PANTALLA/2,
               "y": ALTO_PANTALLA-ALTO_PERSONAJE-ALTO_PISO}
velocidad = 10  # Cuanto avanza o retrocede el personaje en pixeles


esquiador = Jugador(
    tamanio, diccionario_animaciones_personaje, pos_inicial, 3000)

enemigo_uno = Enemigo(
    tamanio, diccionario_animaciones_oso,
    {"x": ANCHO_PANTALLA/2+100, "y": ALTO_PANTALLA-ALTO_PERSONAJE-ALTO_PISO},
    1000, 100, piso)


enemigo_dos = Enemigo(
    tamanio, diccionario_animaciones_yeti,
    {"x": plataforma_uno.lados['main'].x,
     "y": plataforma_uno.lados['main'].y-ALTO_PERSONAJE},
    1000, 100, plataforma_uno)

enemigos = []
enemigos = [enemigo_uno, enemigo_dos]


# TEXTO
fuente = pygame.font.SysFont("Arial", 40)


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


while True:

    RELOJ.tick(FPS)

    manejar_eventos_juego(pygame.event.get())

    definir_accion_personaje(pygame.key.get_pressed(), esquiador)

    texto = fuente.render(f"Vidas: {esquiador.vidas_actuales}", False, "Green", "Blue")
    ancho_texto = texto.get_width()

    texto_vidas = {
        "texto": texto,
        "pos_x": ANCHO_PANTALLA-ancho_texto,
        "pos_y": 0
    }

    texto = fuente.render("Tiempo: ", False, "Green", "Blue")

    texto_tiempo = {
        "texto": texto,
        "pos_x": 0,
        "pos_y": 0
    }

    textos = [texto_vidas, texto_tiempo]

    actualizar_pantalla(PANTALLA, fondo, textos, lista_plataformas, esquiador, enemigos, items)

    if get_mode() is True:
        for p in lista_plataformas:
            dibujar_borde_rectangulos(PANTALLA, p.lados, "Green")
        for e in enemigos:
            dibujar_borde_rectangulos(PANTALLA, e.lados, "Blue")
        dibujar_borde_rectangulos(PANTALLA, esquiador.lados, "Red")

    pygame.display.update()
