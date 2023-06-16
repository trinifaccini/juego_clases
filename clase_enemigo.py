# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from clase_personaje import Personaje

class Enemigo (Personaje):
    def __init__(self, tamanio: tuple, animaciones: dict, pos_inicial: dict, vidas, danio) -> None:

        super().__init__(tamanio, animaciones, pos_inicial, vidas)
        self.danio = danio

    def update(self, pantalla):

        self.animar(pantalla, "quieto_derecha")
