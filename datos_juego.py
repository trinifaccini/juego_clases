from clase_jugador import Jugador
from configuracion_imagenes import * 

ANCHO_PANTALLA, ALTO_PANTALLA = 1400, 750
TAMANIO_PANTALLA = (ANCHO_PANTALLA, ALTO_PANTALLA)
ANCHO_PERSONAJE, ALTO_PERSONAJE = 80, 95
ALTO_PISO = 20

diccionario_animaciones_esquiador = {
    "quieto_derecha": personaje_quieto_derecha,
    "quieto_izquierda": personaje_quieto_izquierda, 
    "camina_derecha": personaje_camina_derecha, 
    "camina_izquierda": personaje_camina_izquierda, 
    "salta_derecha": personaje_salta_derecha, 
    "salta_izquierda": personaje_salta_izquierda
}

diccionario_animaciones_oso = {
    "quieto_derecha": oso_quieto_derecha, 
    "quieto_izquierda": oso_quieto_izquierda, 
    "camina_derecha": oso_camina_derecha, 
    "camina_izquierda": oso_camina_izquierda 

}

diccionario_animaciones_yeti = {
    "quieto_derecha": yeti_camina_derecha, 
    "quieto_izquierda": yeti_camina_izquierda, 
    "camina_derecha": yeti_camina_derecha, 
    "camina_izquierda": yeti_camina_izquierda, 
    "ataca_derecha" : yeti_ataca_derecha,
    "ataca_izquierda": yeti_ataca_izquierda
}

diccionario_animaciones = {
    "jugador": diccionario_animaciones_esquiador,
    "oso": diccionario_animaciones_oso,
    "yeti": diccionario_animaciones_yeti
}

tamanio = (ANCHO_PERSONAJE, ALTO_PERSONAJE)

pos_inicial = {"x": ANCHO_PANTALLA/2,
               "y": ALTO_PANTALLA-ALTO_PERSONAJE-ALTO_PISO}


esquiador = Jugador(tamanio, diccionario_animaciones_esquiador, pos_inicial, 3000)


