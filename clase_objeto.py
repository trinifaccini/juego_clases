# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pygame

from configuracion_imagenes import obtener_rectangulos

class Objeto:
    def __init__(self, tamanio: tuple, imagen, pos_inicial: tuple) -> None:

        plataforma = pygame.image.load(imagen)
        self.ancho = tamanio[0]
        self.alto = tamanio[1]
        self.superficie = pygame.transform.scale(plataforma, (tamanio[0],tamanio[1]))

        rectangulo = self.superficie.get_rect()
        rectangulo.x = pos_inicial[0]
        rectangulo.y = pos_inicial[1]

        self.lados = obtener_rectangulos(pygame.Rect(rectangulo))

    def animar(self,pantalla):
        pantalla.blit(self.superficie, self.lados['main'])

    def update(self,pantalla):

        self.animar(pantalla)
  