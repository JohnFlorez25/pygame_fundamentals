# === utilidades/colisiones.py ===
"""
Manejo de colisiones y eventos del juego
"""
import pygame

def verificar_colisiones(jugador, grupo_energia, grupo_asteroides):
    # Colisiones con energía
    colisiones_energia = pygame.sprite.spritecollide(jugador, grupo_energia, True)
    for energia in colisiones_energia:
        jugador.energia += energia.valor
        jugador.puntos += energia.valor
    
    # Colisiones con asteroides
    colisiones_asteroides = pygame.sprite.spritecollide(jugador, grupo_asteroides, True)
    if colisiones_asteroides:
        jugador.energia -= 25
        jugador.vidas -= 1
        return True if jugador.vidas <= 0 else False
    
    return False