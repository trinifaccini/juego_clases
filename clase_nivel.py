# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

'''
ARCHIVO CLASE NIVEL
'''


# las vidas son por NIVEL

class Nivel():

    def __init__(self, fondo, plataformas, enemigos, items) -> None:

        self.fondo = fondo
        self.tiempo_total_nivel = 1000
        self.tiempo_restante_nivel = 1000
        self.enemigos = enemigos
        self.items = items
        self.plataformas = plataformas # las plataformas van a venir con las trampas

    def posicionar_jugador(self) -> None:
        pass

    def posicionar_plataformas(self, rect_pantalla) -> None:

        for plataforma in self.plataformas:
            plataforma.update(rect_pantalla)

    def posicionar_enemigos(self, rect_pantalla) -> None:

        for enemigo in self.enemigos:
            enemigo.update(rect_pantalla)

    def posicionar_items(self, rect_pantalla) -> None:

        for item in self.items:
            item.update(rect_pantalla)


    def update(self, rect_pantalla, jugador) -> None:

        rect_pantalla.blit(self.fondo, (0, 0))

        self.posicionar_plataformas(rect_pantalla)
        self.posicionar_enemigos(rect_pantalla)
        self.posicionar_items(rect_pantalla)

        jugador.update(rect_pantalla, self.plataformas, self.enemigos, self.items)
