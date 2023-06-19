# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name

import pygame
from clase_enemigo import Enemigo
from clase_item import Item
from clase_nivel import Nivel
from clase_plataforma import Plataforma
from datos_juego import ANCHO_PANTALLA, ALTO_PANTALLA, ALTO_PISO, diccionario_animaciones

TAMANIO_PANTALLA = (ANCHO_PANTALLA, ALTO_PANTALLA)

alto_plataforma_tierra_nieve = 40
altura_plataforma_uno = 40
altura_plataforma_dos = 150

path_piso = "Recursos/Plataformas/plataforma_tierra_nieve.png"
path_plataforma_tierra_nieve = "Recursos/Plataformas/plataforma_tierra_nieve.png"

# ESTO VA A ESTAR EN UN JSON
datos_plataformas = [
    {
        "tamanio": (ANCHO_PANTALLA, ALTO_PISO),
        "path": path_piso,
        "pos_inicial": (0, ALTO_PANTALLA-ALTO_PISO),
    },
    {
        "tamanio": (200, alto_plataforma_tierra_nieve),
        "path": path_plataforma_tierra_nieve,
        "pos_inicial": (200, ALTO_PANTALLA-ALTO_PISO-alto_plataforma_tierra_nieve-altura_plataforma_uno)
    },
    {
        "tamanio": (200, alto_plataforma_tierra_nieve),
        "path": path_plataforma_tierra_nieve,
        "pos_inicial": (500, ALTO_PANTALLA-ALTO_PISO-alto_plataforma_tierra_nieve-altura_plataforma_dos)
    }
]

plataformas = []

for dato in datos_plataformas:

    p = Plataforma(dato['tamanio'], dato['path'], dato['pos_inicial'])
    plataformas.append(p)

# piso = Plataforma(
#     (ANCHO_PANTALLA, ALTO_PISO), "Recursos/Plataformas/plataforma_tierra_nieve.png",
#     {"x": 0, "y": ALTO_PANTALLA-ALTO_PISO}, "piso")

# ALTO_PLATAFORMA = 40
# plataforma_uno = Plataforma(
#     (200, ALTO_PLATAFORMA),"Recursos/Plataformas/plataforma_tierra_nieve.png",
#     {"x": 200, "y": ALTO_PANTALLA-ALTO_PISO-ALTO_PLATAFORMA-70}, "plataforma")

# ITEMS
coca = Item(
    (25, 55), "Recursos/Obstaculos/coca_dibujo.png",
    (200, ALTO_PANTALLA/2), 0, 100)

hamburguesa = Item(
    (60, 40), "Recursos/Obstaculos/hamburguesa.png",
    (200, ALTO_PANTALLA/2), 100, 0)


# FONDO
fondo = pygame.image.load("Recursos/Fondos/fondo_nivel_2.png")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)


# TRAMPAS
ALTO_TRAMPA_PASTO = 70
trampa_pasto = Item(
    (50, ALTO_TRAMPA_PASTO), "Recursos/Obstaculos/trampa_pasto.png",
    (plataformas[1].lados['main'].x,
     plataformas[1].lados['main'].y-ALTO_TRAMPA_PASTO),
    0, -100, True)

ALTO_TRAMPA_ARBOL = 200
trampa_arbol = Item(
    (70, ALTO_TRAMPA_ARBOL), "Recursos/Obstaculos/arbol_1.png",
    (plataformas[1].lados['main'].x+100,
     plataformas[1].lados['main'].y-ALTO_TRAMPA_ARBOL),
    0, -100, True)


items = [trampa_pasto, trampa_arbol]

enemigo_uno = Enemigo(
    (40,40), diccionario_animaciones['yeti'],
    {"x": plataformas[1].lados['main'].x,
     "y": plataformas[1].lados['main'].y-40},
    1000, 100, plataformas[1],
    "Recursos/Obstaculos/bola_nieve_1.png")

enemigos = []
enemigos = [enemigo_uno]

nivel_dos = Nivel(fondo, plataformas, enemigos, items)
