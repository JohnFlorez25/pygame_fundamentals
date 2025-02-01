# === powerups.py ===
"""
Módulo que maneja la lógica de los power-ups.
"""
import random
import pygame
from config import *
from utilidades import generar_posicion_aleatoria

def generar_powerup():
    """
    Genera un nuevo power-up con cierta probabilidad.
    """
    if random.randint(1, 100) <= POWERUP_PROBABILIDAD:
        x, y = generar_posicion_aleatoria(ANCHO_VENTANA, ALTO_VENTANA, POWERUP_TAMANIO)
        tipo = random.choice(['velocidad', 'inmunidad', 'puntos_dobles'])
        return x, y, tipo
    return None

def aplicar_powerup(tipo, tiempo_actual):
    """
    Aplica el efecto del power-up y retorna su duración.
    """
    efectos = {
        'velocidad': JUGADOR_VELOCIDAD_BOOST,
        'inmunidad': True,
        'puntos_dobles': 2
    }
    return efectos.get(tipo, None), tiempo_actual + POWERUP_DURACION