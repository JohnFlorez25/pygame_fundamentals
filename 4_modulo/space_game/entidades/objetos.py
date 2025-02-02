# === entidades/objetos.py ===
"""
Clases para los objetos del juego (energía y asteroides)
"""
import pygame
import random
from config import *

class Energia(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(ENERGIA_TAMAÑO)
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.reset_position()
        self.valor = random.randint(10, 30)
        
    def update(self):
        self.rect.y += VELOCIDAD_OBJETOS
        if self.rect.top > ALTO:
            self.reset_position()
            
    def reset_position(self):
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-100, -40)

class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(ASTEROIDE_TAMAÑO)
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.reset_position()
        self.velocidad = random.randint(2, 5)
        
    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.reset_position()
            
    def reset_position(self):
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidad = random.randint(2, 5)