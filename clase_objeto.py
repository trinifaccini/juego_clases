# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pygame

from configuracion_imagenes import obtener_rectangulos

class Objeto:
    def __init__(self, tamanio: tuple, imagen, pos_inicial: dict) -> None:

        plataforma = pygame.image.load(imagen)
        self.superficie = pygame.transform.scale(plataforma, (tamanio[0],tamanio[1]))

        rectangulo = self.superficie.get_rect()
        rectangulo.x = pos_inicial['x']
        rectangulo.y = pos_inicial['y']

        self.lados = obtener_rectangulos(pygame.Rect(rectangulo))

    def update(self,pantalla):

        pantalla.blit(self.superficie, self.lados['main'])