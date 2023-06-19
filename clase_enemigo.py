'''
ARCHIVO CLASE ENEMIGO 
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from clase_personaje import Personaje
from clase_proyectil import Proyectil


class Enemigo (Personaje):
    def __init__(self, tamanio: tuple, animaciones: dict, pos_inicial: dict, vidas, danio, apoyo, path_img="") -> None:

        super().__init__(tamanio, animaciones, pos_inicial, vidas)
        self.danio = danio
        self.rectangulo_apoyo = apoyo.lados['main']

        ## ELEGIR ALEATORIAMENTE ESTA DIRECCION
        self.accion = "derecha"
        self.lista_proyectiles = []
        self.path_img = path_img

    def lanzar_proyectil(self):

        # print(self.lados['main'].centerx)
        # print(self.lados['main'].centery)

        proyectil = Proyectil(
        (30, 30),self.path_img,
        (self.lados['main'].centerx, self.lados['left'].y), 100)

        self.lista_proyectiles.append(proyectil)

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

        for proyectil in self.lista_proyectiles:
            if proyectil.colisiono is True:
                self.lista_proyectiles.remove(proyectil)
            else:
                proyectil.update(pantalla)
