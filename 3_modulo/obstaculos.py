"""
Módulo que maneja la lógica de los obstáculos.
"""
import random
from config import *
from utilidades import generar_posicion_aleatoria

def inicializar_obstaculos():
    """
    Inicializa las posiciones y direcciones de los obstáculos.
    """
    obstaculos = []
    for _ in range(CANTIDAD_OBSTACULOS):
        x, y = generar_posicion_aleatoria(ANCHO_VENTANA, ALTO_VENTANA, OBSTACULO_TAMANIO)
        direccion_x = random.choice([-1, 1])
        direccion_y = random.choice([-1, 1])
        obstaculos.append([x, y, direccion_x, direccion_y])
    return obstaculos

def mover_obstaculos(obstaculos, velocidad):
    """
    Mueve todos los obstáculos y maneja rebotes.
    Ahora con movimiento en 2D.
    """
    for i in range(len(obstaculos)):
        x, y, dir_x, dir_y = obstaculos[i]
        
        # Actualizar posición
        nuevo_x = x + velocidad * dir_x
        nuevo_y = y + velocidad * dir_y
        
        # Rebotar en los bordes
        if nuevo_x <= 0 or nuevo_x >= ANCHO_VENTANA - OBSTACULO_TAMANIO:
            dir_x *= -1
            nuevo_x = x  # Evitar que se pegue a los bordes
        
        if nuevo_y <= 0 or nuevo_y >= ALTO_VENTANA - OBSTACULO_TAMANIO:
            dir_y *= -1
            nuevo_y = y  # Evitar que se pegue a los bordes
            
        obstaculos[i] = [nuevo_x, nuevo_y, dir_x, dir_y]
    
    return obstaculos