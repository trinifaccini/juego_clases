'''
ARCHIVO CLASE IMAGEN
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import pygame

class Imagen:
    def __init__(self, imagen, tamanio:tuple) -> None:

        imagen = pygame.image.load(imagen)
        imagen_reescalada = pygame.transform.scale(imagen, (tamanio[0], tamanio[1]))
        self.imagen = imagen_reescalada
        self.rectangulo = imagen_reescalada.get_rect() # no va a cambiar por mas que lo gire
        #self.superficie_imagen = pygame.transform.scale(self.imagen, (tamanio[0],tamanio[1]))

    def girar(self, flip_x, flip_y):
        self.imagen = pygame.transform.flip(self.imagen, flip_x, flip_y)
