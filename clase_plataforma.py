# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from clase_objeto import Objeto

class Plataforma(Objeto):
    def __init__(self, tamanio: tuple, imagen, pos_inicial: dict, tipo:str) -> None:

        super().__init__(tamanio, imagen, pos_inicial)

        self.tipo = tipo
