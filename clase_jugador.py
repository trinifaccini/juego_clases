'''
ARCHIVO CLASE JUGADOR
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from clase_personaje import Personaje

class Jugador (Personaje):
    def __init__(self, tamanio: tuple, animaciones: dict, pos_inicial: dict, vidas) -> None:

        super().__init__(tamanio, animaciones, pos_inicial, vidas)

        self.accion = "quieto"

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

            self.mover(self.desplazamiento_y,pantalla, "y")

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

    def mover(self, velocidad, pantalla, eje:str):

        for lado in dict(self.lados):
            if eje == "x":
                if self.accion == "derecha":
                    nueva_x = self.lados["main"].x + velocidad
                    if nueva_x < pantalla.get_rect().width -  self.lados["main"].width:
                        self.lados[lado].x += velocidad
                else:
                    nueva_x = self.lados["main"].x - velocidad
                    if nueva_x > 0:
                        self.lados[lado].x += velocidad
            else:
                self.lados[lado].y += velocidad

    def colisionar_enemigos(self, enemigos:list):

        for enemigo in enemigos:

            if self.lados['main'].colliderect(enemigo.lados['main']):
                self.vidas_actuales -= enemigo.danio

    # Colisionar con items (especiales o trampas)
    def colisionar_items(self, items:list):

        for item in items:

            if self.lados['main'].colliderect(item.lados['main']):
                self.vidas_actuales += item.aporte_vida
                self.puntos += item.aporte_puntos
                if item.trampa is not True:
                    items.remove(item)
        

    def update(self, pantalla, lista_plataformas:list, enemigos:list, items:list):
   # def update(self, pantalla):

        match (self.accion):
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.ultima_accion = "derecha"
                self.mover(10, pantalla, "x")
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.ultima_accion = "izquierda"
                self.mover(-10, pantalla, "x")
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
        self.colisionar_items(items)
        
    def update_personalizado(self, enemigos, items):

        self.colisionar_enemigos(enemigos)
