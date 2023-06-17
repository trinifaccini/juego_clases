'''
ARCHIVO CLASE ENEMIGO 
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from clase_personaje import Personaje


class Enemigo (Personaje):
    def __init__(self, tamanio: tuple, animaciones: dict, pos_inicial: dict, vidas, danio, apoyo) -> None:

        super().__init__(tamanio, animaciones, pos_inicial, vidas)
        self.danio = danio
        self.rectangulo_apoyo = apoyo.lados['main']

        ## ELEGIR ALEATORIAMENTE ESTA DIRECCION
        self.accion = "derecha"

    def mover(self, velocidad):

        # REBOTE SOBRE LA PLATAFORMA EN LA QUE SE ENCUENTRA
        if self.accion == "derecha" and self.lados['right'].x == self.rectangulo_apoyo.x + self.rectangulo_apoyo.width:
            self.accion = "izquierda"

        elif self.accion == "izquierda" and self.lados['left'].x == self.rectangulo_apoyo.x:
            self.accion = "derecha"

        for lado in dict(self.lados):
            self.lados[lado].x += velocidad

    def update(self, pantalla):

        match (self.accion):
            case "derecha":
                self.animar(pantalla, "camina_derecha")
                self.mover(5)
            case "izquierda":
                self.animar(pantalla, "camina_izquierda")
                self.mover(-5)
