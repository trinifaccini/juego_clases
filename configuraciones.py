"""
CONFIGURACIONES DE IMAGEN

"""
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=consider-using-enumerate

import pygame

#########################


def girar_imagenes(lista, flip_x, flip_y) -> list:
    lista_girada = []

    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada


def reescalar_imagen(lista_imagenes, alto, ancho):

    for i in range(len(lista_imagenes)):  # en un rango, si modifica
        lista_imagenes[i] = pygame.transform.scale(
            lista_imagenes[i], (alto, ancho))


def obtener_rectangulos(principal: pygame.Rect) -> dict:
    diccionario = {}

    diccionario = {
        "main": principal,
        "bottom": pygame.Rect(principal.left, principal.bottom-10, principal.width, 10),
        "right": pygame.Rect(principal.right-5, principal.top, 5, principal.height),
        "left": pygame.Rect(principal.left, principal.top, 5, principal.height),
        "top": pygame.Rect(principal.left, principal.top, principal.width, 10)
    }

    return diccionario


def dibujar_borde_rectangulos(pantalla, lados_rectangulo: dict, color: str):

    for lado in lados_rectangulo:
        pygame.draw.rect(pantalla, color, lados_rectangulo[lado], 2)

###################


# Definimos los fotogramas de cada animacion

personaje_quieto_derecha = [
    pygame.image.load("Recursos/Personajes/Esquiador/Quieto/esquiador_quieto_0.png"),
    pygame.image.load("Recursos/Personajes/Esquiador/Quieto/esquiador_quieto_1.png"),
    pygame.image.load("Recursos/Personajes/Esquiador/Quieto/esquiador_quieto_2.png"),
    pygame.image.load("Recursos/Personajes/Esquiador/Quieto/esquiador_quieto_3.png"),
    ]

personaje_quieto_izquierda = girar_imagenes(personaje_quieto_derecha, True, False)


personaje_camina_derecha = [
    pygame.image.load("Recursos/Personajes/Esquiador/Moviendose/esquiador_moviendose_0.png"),
    pygame.image.load("Recursos/Personajes/Esquiador/Moviendose/esquiador_moviendose_1.png"),
    pygame.image.load("Recursos/Personajes/Esquiador/Moviendose/esquiador_moviendose_2.png"),
    pygame.image.load("Recursos/Personajes/Esquiador/Moviendose/esquiador_moviendose_3.png")
]

personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)

personaje_salta_derecha = [
    pygame.image.load("Recursos/Personajes/Esquiador/Saltando/esquiador_saltando_0.png"),
                 #    pygame.image.load("Salta/1.png"),
                 #    pygame.image.load("Salta/2.png"),
                 #    pygame.image.load("Salta/3.png")
                 ]

personaje_salta_izquierda = girar_imagenes(personaje_salta_derecha, True, False)

####

oso_quieto_derecha = [
    pygame.image.load("Recursos/Personajes/Oso/Quieto/oso_quieto_0.png"),
   #pygame.image.load("Recursos/Personajes/Oso/Quieto/oso_quieto_1.png"),
    ]

oso_quieto_izquierda = girar_imagenes(oso_quieto_derecha, True, False)

oso_camina_derecha = [
    pygame.image.load("Recursos/Personajes/Oso/Camina/oso_camina_0.png"),
    pygame.image.load("Recursos/Personajes/Oso/Camina/oso_camina_1.png"),
    pygame.image.load("Recursos/Personajes/Oso/Camina/oso_camina_2.png"),
    pygame.image.load("Recursos/Personajes/Oso/Camina/oso_camina_3.png"),
    pygame.image.load("Recursos/Personajes/Oso/Camina/oso_camina_4.png"),
    pygame.image.load("Recursos/Personajes/Oso/Camina/oso_camina_5.png"),
    pygame.image.load("Recursos/Personajes/Oso/Camina/oso_camina_6.png"),
    pygame.image.load("Recursos/Personajes/Oso/Camina/oso_camina_7.png"),

]

oso_camina_izquierda = girar_imagenes(oso_camina_derecha, True, False)

####
yeti_quieto_derecha = [
    pygame.image.load("Recursos/Personajes/Yeti/Quieto/yeti_quieto_0.png"),
    ]

yeti_quieto_izquierda = girar_imagenes(yeti_quieto_derecha, True, False)

yeti_camina_derecha = [
    pygame.image.load("Recursos/Personajes/Yeti/Camina/yeti_camina_0.png"),
    pygame.image.load("Recursos/Personajes/Yeti/Camina/yeti_camina_1.png"),
    pygame.image.load("Recursos/Personajes/Yeti/Camina/yeti_camina_2.png"),
    pygame.image.load("Recursos/Personajes/Yeti/Camina/yeti_camina_3.png"),
    pygame.image.load("Recursos/Personajes/Yeti/Camina/yeti_camina_4.png"),

]

yeti_camina_izquierda = girar_imagenes(oso_camina_derecha, True, False)

yeti_ataca_derecha = [
    pygame.image.load("Recursos/Personajes/Yeti/Ataca/yeti_ataca_0.png"),
    pygame.image.load("Recursos/Personajes/Yeti/Ataca/yeti_ataca_1.png"),
    pygame.image.load("Recursos/Personajes/Yeti/Ataca/yeti_ataca_2.png"),
    pygame.image.load("Recursos/Personajes/Yeti/Ataca/yeti_ataca_3.png"),
    pygame.image.load("Recursos/Personajes/Yeti/Ataca/yeti_ataca_4.png"),
    pygame.image.load("Recursos/Personajes/Yeti/Ataca/yeti_ataca_5.png"),
    ]

yeti_ataca_izquierda = girar_imagenes(yeti_ataca_derecha, True, False)
