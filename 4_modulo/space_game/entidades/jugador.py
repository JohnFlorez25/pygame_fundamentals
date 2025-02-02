"""
Clase para el jugador (nave espacial)
"""
import pygame
from config import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(NAVE_TAMAÑO)
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 10
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.energia = 100
        self.vidas = 3
        self.puntos = 0
        
    def update(self):
        # Movimiento horizontal
        self.rect.x += self.velocidad_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            
        # Movimiento vertical
        self.rect.y += self.velocidad_y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
    
    def mover(self, direccion):
        if direccion == "izquierda":
            self.velocidad_x = -NAVE_VELOCIDAD
        elif direccion == "derecha":
            self.velocidad_x = NAVE_VELOCIDAD
        elif direccion == "arriba":
            self.velocidad_y = -NAVE_VELOCIDAD
        elif direccion == "abajo":
            self.velocidad_y = NAVE_VELOCIDAD
    
    def detener(self, direccion):
        if direccion in ["izquierda", "derecha"]:
            self.velocidad_x = 0
        elif direccion in ["arriba", "abajo"]:
            self.velocidad_y = 0