# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from clase_objeto import Objeto

# PARA ITEMS ESPERACILES Y PARA TRAMPAS
# LOS ITEMS ESPECIALES VAN A SUMAR PUNTOS O VIDA
# LAS TRAMPAS VAN A RESTAR PUNTOS O VIDA

class Item(Objeto):

    def __init__(self, tamanio: tuple, imagen, pos_inicial: dict, puntos: int, vida:int, es_trampa=False) -> None:

        super().__init__(tamanio, imagen, pos_inicial)

        self.aporte_puntos = puntos
        self.aporte_vida = vida
        self.trampa = es_trampa

