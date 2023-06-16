# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from clase_personaje import Personaje

class Jugador (Personaje):
    def __init__(self, tamanio: tuple, animaciones: dict, pos_inicial: dict, vidas) -> None:

        super().__init__(tamanio, animaciones, pos_inicial, vidas)

        # SALTO - SOLO JUGADOR
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.gravedad = 1 # cuanto mas grande, mas rapido cae
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15

        self.puntos = 0

    def aplicar_gravedad(self, pantalla, lista_plataformas:list):

        if self.esta_saltando:
            if self.ultima_accion == "derecha":
                self.animar(pantalla, "salta_derecha")
            else:
                self.animar(pantalla, "salta_izquierda")

            self.mover(self.desplazamiento_y, "y")

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        # #Verifica en cada iteracion con que plataforma esta colisionando
        for p in lista_plataformas:
            if self.lados['bottom'].colliderect(p.lados['top']):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.lados["main"].bottom = p.lados['main'].top # POR QUE ACA NO PONEMOS A TODOS LOS LADOS DEL PERSONAJE??? 
                #Rompe cuando deja de verificar colision, entonces el personaje cae
                break
            else:
                self.esta_saltando = True


    def update(self, pantalla, lista_plataformas:list):

        match (self.accion):
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.ultima_accion = "derecha"
                self.mover(10, "x")
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.ultima_accion = "izquierda"
                self.mover(-10, "x")
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "quieto":
                if not self.esta_saltando: # solo animo si no está saltando
                    if self.ultima_accion == "derecha":
                        self.animar(pantalla, "quieto_derecha")
                    else:
                        self.animar(pantalla, "quieto_izquierda")


        self.aplicar_gravedad(pantalla, lista_plataformas) # se aplica siempre, no solo cuando salta


        