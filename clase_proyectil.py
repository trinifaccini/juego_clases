# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from clase_objeto import Objeto


class Proyectil(Objeto):

    def __init__(self, tamanio: tuple, imagen, pos_inicial: dict, danio:int) -> None:

        super().__init__(tamanio, imagen, pos_inicial)

        self.danio = danio
        self.direccion = "derecha"
        self.colisiono = False

    def colisionar_pantalla(self, pantalla):

        if self.direccion == "derecha" and self.lados['right'].x >= pantalla.get_width()-200:
            self.colisiono = True

        elif self.direccion == "izquierda" and self.lados['left'].x == 0:
            self.colisiono = True

    def mover(self, velocidad:int) -> None:

        # La direccion del proyectil va a estar dada por la velocidad

        for lado in dict(self.lados):
            self.lados[lado].x += velocidad


    def update(self, pantalla) -> None:

        self.colisionar_pantalla(pantalla)
        self.mover(5)

        super().update(pantalla)
        self.mover(5)
