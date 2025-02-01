# === utilidades.py ===
"""
Módulo de funciones útiles y comunes para el juego.
"""
import random
import pygame

def generar_posicion_aleatoria(ancho_ventana, alto_ventana, tamanio):
    """
    Genera una posición aleatoria dentro de los límites de la ventana.
    """
    x = random.randint(tamanio, ancho_ventana - tamanio * 2)
    y = random.randint(tamanio, alto_ventana - tamanio * 2)
    return x, y

def hay_colision(x1, y1, tamanio1, x2, y2, tamanio2):
    """
    Detecta colisiones entre dos objetos rectangulares (AABB).
    """
    return (x1 < x2 + tamanio2 and
            x1 + tamanio1 > x2 and
            y1 < y2 + tamanio2 and
            y1 + tamanio1 > y2)

def mostrar_texto(ventana, texto, x, y, color=(255, 255, 255), tamanio=36):
    """
    Muestra texto en la ventana con más opciones de personalización.
    """
    fuente = pygame.font.Font(None, tamanio)
    superficie = fuente.render(texto, True, color)
    ventana.blit(superficie, (x, y))

def dibujar_rectangulo(ventana, x, y, tamanio, color):
    """
    Dibuja un rectángulo en la ventana.
    """
    pygame.draw.rect(ventana, color, (x, y, tamanio, tamanio))