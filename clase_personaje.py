# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from configuraciones import reescalar_imagen, obtener_rectangulos

# Todos los personajes van a tener:

# AGREGAR LIMITE EN EJE X

class Personaje:
    def __init__(self, tamanio: tuple, animaciones: dict, pos_inicial: dict, vidas) -> None:

        # CONFECCION - TODOS
        self.ancho = tamanio[0]
        self.alto = tamanio[1]

        # ANIMACIONES - TODOS
        self.contador_pasos = 0 #ya no es un atributo global
        self.accion = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.ultima_accion = "derecha"

        # RECTANGULO PERSONAJE (MAIN) - TODOS
        # se que todos los personajes van a tener un quieto_derecha
        rectangulo = self.animaciones["quieto_derecha"][0].get_rect()
        rectangulo.x = pos_inicial['x']
        rectangulo.y = pos_inicial['y']

        # RECTANGULOS LADOS PERSONAJE (TODOS) - TODOS
        self.lados = obtener_rectangulos(rectangulo)

        self.vidas_inicial = vidas
        self.vidas_actuales = vidas

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], self.ancho, self.alto)

    # Secuencia de imagenes de cada animacion
    # Superposicion de cada fotograma
    # Tener en cuenta que esta funcion se llama en cada vuelta del loop
    def animar(self, pantalla, accion: str):

        imagenes_accion = self.animaciones[accion]

        # cuantas imagenes tengo para esa accion en particular
        largo = len(imagenes_accion)

        # necesito saber si el contador de pasos es mayor a la
        # cantidad de imagenes que tengo para la animacion
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(imagenes_accion[self.contador_pasos], self.lados['main'])
        self.contador_pasos += 1

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
        