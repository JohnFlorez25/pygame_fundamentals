"""
Módulo que maneja toda la lógica relacionada con el jugador.
"""
import pygame
from config import *

def mover_jugador(x, y, velocidad, teclas):
    """
    Actualiza la posición del jugador según las teclas presionadas.
    Ahora incluye movimiento diagonal normalizado.
    """
    dx = 0
    dy = 0
    
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        dx -= 1
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        dx += 1
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        dy -= 1
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        dy += 1
        
    # Normalizar el movimiento diagonal
    if dx != 0 and dy != 0:
        dx *= 0.707  # 1/√2
        dy *= 0.707
        
    # Actualizar posición
    nuevo_x = x + dx * velocidad
    nuevo_y = y + dy * velocidad
    
    # Mantener dentro de los límites
    nuevo_x = max(0, min(nuevo_x, ANCHO_VENTANA - JUGADOR_TAMANIO))
    nuevo_y = max(0, min(nuevo_y, ALTO_VENTANA - JUGADOR_TAMANIO))
    
    return nuevo_x, nuevo_y

def regresar_a_inicio(x, y):
    """
    Regresa al jugador a su posición inicial con una pequeña animación.
    """
    return JUGADOR_X_INICIAL, JUGADOR_Y_INICIAL
