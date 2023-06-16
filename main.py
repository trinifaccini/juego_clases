# pylint: disable=global-statement
# pylint: disable=invalid-name
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import sys
import pygame
from clase_jugador import Jugador
from clase_enemigo import Enemigo
from clase_plataforma import Plataforma
from configuraciones import *
from modo import *

################################################################

# Blitear y actualizar todos los objetos de mi pantalla


def actualizar_pantalla(pantalla, fondo, lista_plataformas, personajes):

    pantalla.blit(fondo, (0, 0))

    # Plataformas

    for p in lista_plataformas:
        pantalla.blit(p.superficie, (p.lados['main'].x, p.lados['main'].y))

    # Personajes
    personajes[0].update(pantalla, lista_plataformas)
    personajes[1].update(pantalla)
    #personajes[2].update(pantalla)


########################################################################


ANCHO_PANTALLA, ALTO_PANTALLA = 1300, 700
TAMANIO_PANTALLA = (ANCHO_PANTALLA, ALTO_PANTALLA)
FPS = 18

ALTO_PISO = 20

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)

# FONDO
fondo = pygame.image.load("Recursos/Fondos/fondo_nivel_1.png")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)

ALTO_PISO = 20
piso = Plataforma(
    (ANCHO_PANTALLA, ALTO_PISO), "Recursos/Plataformas/plataforma_tierra_nieve.png",
    {"x": 0, "y": ALTO_PANTALLA-ALTO_PISO}, "piso")

ALTO_PLATAFORMA = 40
plataforma_uno = Plataforma(
    (200, ALTO_PLATAFORMA),"Recursos/Plataformas/plataforma_tierra_nieve.png",
    {"x": 200, "y": ALTO_PANTALLA-ALTO_PISO-ALTO_PLATAFORMA-70}, "plataforma")

lista_plataformas = [piso, plataforma_uno]

# PERSONAJE
ANCHO_PERSONAJE = 80
ALTO_PERSONAJE = 95
tamanio = (ANCHO_PERSONAJE, ALTO_PERSONAJE)
pos_inicial = {"x": ANCHO_PANTALLA/2,
               "y": ALTO_PANTALLA-ALTO_PERSONAJE-ALTO_PISO}
velocidad = 10  # Cuanto avanza o retrocede el personaje en pixeles

diccionario_animaciones_personaje = {}
diccionario_animaciones_personaje = {
    "quieto_derecha": personaje_quieto_derecha,
    "quieto_izquierda": personaje_quieto_izquierda,
    "camina_derecha": personaje_camina_derecha,
    "camina_izquierda": personaje_camina_izquierda,
    "salta_derecha": personaje_salta_derecha,
    "salta_izquierda": personaje_salta_izquierda
}

diccionario_animaciones_oso = {}
diccionario_animaciones_oso = {
    "quieto_derecha": oso_quieto_derecha,
    "quieto_izquierda": oso_quieto_izquierda,
    "camina_derecha": oso_camina_derecha,
    "camina_izquierda": oso_camina_izquierda
}

diccionario_animaciones_yeti = {}
diccionario_animaciones_yeti = {
    "quieto_derecha": yeti_quieto_derecha,
    "quieto_izquierda": yeti_quieto_izquierda,
    "camina_derecha": yeti_camina_derecha,
    "camina_izquierda": yeti_camina_izquierda,
    "ataca_derecha": yeti_ataca_derecha,
    "ataca_izquierda": yeti_ataca_izquierda
}


esquiador = Jugador(
    tamanio, diccionario_animaciones_personaje, pos_inicial, 3000)

# enemigo_uno = Enemigo(
#     tamanio, diccionario_animaciones_oso,
#     {"x": ANCHO_PANTALLA/2+100, "y": ALTO_PANTALLA-ALTO_PERSONAJE-ALTO_PISO},
#     1000, 100)


enemigo_dos = Enemigo(
    tamanio, diccionario_animaciones_yeti,
    {"x": ANCHO_PANTALLA/2-100, "y": ALTO_PANTALLA-ALTO_PERSONAJE-ALTO_PISO},
    1000, 100)

personajes = [esquiador, enemigo_dos]

while True:

    RELOJ.tick(FPS)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        esquiador.accion = "derecha"
    elif keys[pygame.K_LEFT]:
        esquiador.accion = "izquierda"
    elif keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        esquiador.accion = "salta"
    elif keys[pygame.K_TAB]:
        change_mode()
    else:
        esquiador.accion = "quieto"

    actualizar_pantalla(PANTALLA, fondo, lista_plataformas, personajes)

    if get_mode() is True:
        for p in lista_plataformas:
            dibujar_borde_rectangulos(PANTALLA, p.lados, "Green")
        dibujar_borde_rectangulos(PANTALLA, esquiador.lados, "Red")

    pygame.display.update()
