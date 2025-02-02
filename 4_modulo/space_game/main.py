# === main.py ===
"""
Módulo principal del juego
"""
import pygame
import random
from config import *
from entidades.jugador import Jugador
from entidades.objetos import Energia, Asteroide
from utilidades.scoring import SistemaScore
from utilidades.colisiones import verificar_colisiones

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Nave Espacial")
        self.reloj = pygame.time.Clock()
        self.estado = ESTADO_MENU
        self.todos_sprites = pygame.sprite.Group()
        self.energias = pygame.sprite.Group()
        self.asteroides = pygame.sprite.Group()
        self.sistema_score = SistemaScore()
        self.inicializar_juego()
    
    def inicializar_juego(self):
        self.jugador = Jugador()
        self.todos_sprites.add(self.jugador)
        
        # Crear energías iniciales
        for _ in range(4):
            energia = Energia()
            self.todos_sprites.add(energia)
            self.energias.add(energia)
        
        # Crear asteroides iniciales
        for _ in range(6):
            asteroide = Asteroide()
            self.todos_sprites.add(asteroide)
            self.asteroides.add(asteroide)
    
    def procesar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            
            elif evento.type == pygame.KEYDOWN:
                if self.estado == ESTADO_MENU:
                    if evento.key == pygame.K_RETURN:
                        self.estado = ESTADO_JUGANDO
                elif self.estado == ESTADO_JUGANDO:
                    if evento.key == pygame.K_LEFT:
                        self.jugador.mover("izquierda")
                    elif evento.key == pygame.K_RIGHT:
                        self.jugador.mover("derecha")
                    elif evento.key == pygame.K_UP:
                        self.jugador.mover("arriba")
                    elif evento.key == pygame.K_DOWN:
                        self.jugador.mover("abajo")
                elif self.estado == ESTADO_GAMEOVER:
                    if evento.key == pygame.K_RETURN:
                        self.reiniciar_juego()
            
            elif evento.type == pygame.KEYUP:
                if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    self.jugador.detener("horizontal")
                elif evento.key in [pygame.K_UP, pygame.K_DOWN]:
                    self.jugador.detener("vertical")
        
        return True
    
    def actualizar(self):
        if self.estado == ESTADO_JUGANDO:
            self.todos_sprites.update()
            
            # Generar nueva energía aleatoriamente
            if random.random() < 0.02:
                energia = Energia()
                self.todos_sprites.add(energia)
                self.energias.add(energia)
            
            # Verificar colisiones
            game_over = verificar_colisiones(
                self.jugador, 
                self.energias, 
                self.asteroides
            )
            
            if game_over or self.jugador.energia <= 0:
                self.estado = ESTADO_GAMEOVER
    
    def dibujar(self):
        self.pantalla.fill(NEGRO)
        
        if self.estado == ESTADO_MENU:
            self.dibujar_menu()
        elif self.estado == ESTADO_JUGANDO:
            self.todos_sprites.draw(self.pantalla)
            self.dibujar_hud()
        elif self.estado == ESTADO_GAMEOVER:
            self.dibujar_game_over()
        
        pygame.display.flip()
    
    def dibujar_menu(self):
        font = pygame.font.Font(None, 64)
        texto = font.render("NAVE ESPACIAL", True, BLANCO)
        texto_rect = texto.get_rect(center=(ANCHO/2, ALTO/2))
        self.pantalla.blit(texto, texto_rect)
        
        font = pygame.font.Font(None, 32)
        texto = font.render("Presiona ENTER para comenzar", True, BLANCO)
        texto_rect = texto.get_rect(center=(ANCHO/2, ALTO/2 + 50))
        self.pantalla.blit(texto, texto_rect)
    
    def dibujar_hud(self):
        font = pygame.font.Font(None, 32)
        textos = [
            f"Energía: {self.jugador.energia}",
            f"Vidas: {self.jugador.vidas}",
            f"Puntos: {self.jugador.puntos}"
        ]
        for i, texto in enumerate(textos):
            surface = font.render(texto, True, BLANCO)
            self.pantalla.blit(surface, (10, 10 + i*30))
    
    def dibujar_game_over(self):
        font = pygame.font.Font(None, 64)
        texto = font.render("GAME OVER", True, BLANCO)
        texto_rect = texto.get_rect(center=(ANCHO/2, ALTO/2))
        self.pantalla.blit(texto, texto_rect)
        
        font = pygame.font.Font(None, 32)
        texto = font.render(f"Puntuación final: {self.jugador.puntos}", True, BLANCO)
        texto_rect = texto.get_rect(center=(ANCHO/2, ALTO/2 + 50))
        self.pantalla.blit(texto, texto_rect)
        
        texto = font.render("Presiona ENTER para jugar de nuevo", True, BLANCO)
        texto_rect = texto.get_rect(center=(ANCHO/2, ALTO/2 + 100))
        self.pantalla.blit(texto, texto_rect)
    
    def reiniciar_juego(self):
        self.todos_sprites.empty()
        self.energias.empty()
        self.asteroides.empty()
        self.inicializar_juego()
        self.estado = ESTADO_JUGANDO
    
    def ejecutar(self):
        ejecutando = True
        while ejecutando:
            ejecutando = self.procesar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(FPS)
        
        pygame.quit()

if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()