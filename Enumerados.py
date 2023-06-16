from enum import Enum 

class Colores(Enum):
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    AZUL=(0,0,255)
    AZUL_CLARO=(0,150,255)

class Orientaciones(Enum):
    HORIZONTAL = "Horizontal"
    VERTICAL = "Vertical"