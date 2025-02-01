"""
Módulo principal del juego que integra todos los componentes.
"""
import pygame
import sys
from config import *
from utilidades import *
from jugador import *
from obstaculos import *
from powerups import *

def inicializar_juego():
    """
    Inicializa Pygame y configura la ventana.
    """
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption(TITULO_JUEGO)
    return ventana

def main():
    ventana = inicializar_juego()
    reloj = pygame.time.Clock()
    
    # Estado del juego
    jugador_x = JUGADOR_X_INICIAL
    jugador_y = JUGADOR_Y_INICIAL
    velocidad = JUGADOR_VELOCIDAD_NORMAL
    vidas = JUGADOR_VIDAS_INICIAL
    puntos = 0
    nivel = 1
    
    # Inicializar obstáculos
    obstaculos = inicializar_obstaculos()
    velocidad_obstaculos = OBSTACULO_VELOCIDAD_INICIAL
    
    # Generar primer objetivo
    objetivo_x, objetivo_y = generar_posicion_aleatoria(ANCHO_VENTANA, ALTO_VENTANA, OBJETIVO_TAMANIO)
    
    # Sistema de power-ups
    powerup_activo = None
    tiempo_powerup = 0
    multiplicador_puntos = 1
    
    corriendo = True
    while corriendo and vidas > 0:
        tiempo_actual = pygame.time.get_ticks()
        
        # === Manejo de eventos ===
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
                
        # === Actualización ===
        teclas = pygame.key.get_pressed()
        jugador_x, jugador_y = mover_jugador(jugador_x, jugador_y, velocidad, teclas)
        obstaculos = mover_obstaculos(obstaculos, velocidad_obstaculos)
        
        # Verificar colisiones con obstáculos
        for obs in obstaculos:
            if hay_colision(jugador_x, jugador_y, JUGADOR_TAMANIO, 
                          obs[0], obs[1], OBSTACULO_TAMANIO):
                if powerup_activo != 'inmunidad':
                    vidas -= 1
                    jugador_x, jugador_y = regresar_a_inicio(jugador_x, jugador_y)
                    break
        
        # Verificar colisión con objetivo
        if hay_colision(jugador_x, jugador_y, JUGADOR_TAMANIO,
                       objetivo_x, objetivo_y, OBJETIVO_TAMANIO):
            puntos += OBJETIVO_VALOR * multiplicador_puntos
            objetivo_x, objetivo_y = generar_posicion_aleatoria(ANCHO_VENTANA, ALTO_VENTANA, OBJETIVO_TAMANIO)
            
            # Posible generación de power-up
            nuevo_powerup = generar_powerup()
            if nuevo_powerup:
                powerup_activo = nuevo_powerup
            
            # Sistema de niveles
            if puntos >= nivel * PUNTOS_PARA_NIVEL:
                nivel += 1
                velocidad_obstaculos += OBSTACULO_INCREMENTO_VELOCIDAD
        
        # Manejar power-ups activos
        if powerup_activo:
            if tiempo_actual > tiempo_powerup:
                powerup_activo = None
                velocidad = JUGADOR_VELOCIDAD_NORMAL
                multiplicador_puntos = 1
        
        # === Renderizado ===
        ventana.fill(COLOR_NEGRO)
        
        # Dibujar jugador
        dibujar_rectangulo(ventana, jugador_x, jugador_y, JUGADOR_TAMANIO, COLOR_ROJO)
        
        # Dibujar obstáculos
        for obs in obstaculos:
            dibujar_rectangulo(ventana, obs[0], obs[1], OBSTACULO_TAMANIO, COLOR_AZUL)
        
        # Dibujar objetivo
        dibujar_rectangulo(ventana, objetivo_x, objetivo_y, OBJETIVO_TAMANIO, COLOR_VERDE)
        
        # Dibujar power-up si existe
        if powerup_activo:
            dibujar_rectangulo(ventana, powerup_activo[0], powerup_activo[1], 
                             POWERUP_TAMANIO, COLOR_AMARILLO)
        
        # Mostrar información
        mostrar_texto(ventana, f"Puntos: {puntos}", 10, 10)
        mostrar_texto(ventana, f"Vidas: {vidas}", 10, 40)
        mostrar_texto(ventana, f"Nivel: {nivel}", 10, 70)
        
        pygame.display.flip()
        reloj.tick(FPS)
    
    # === Pantalla de fin de juego ===
    if vidas <= 0:
        ventana.fill(COLOR_NEGRO)
        mostrar_texto(ventana, "¡Juego Terminado!", ANCHO_VENTANA//3, ALTO_VENTANA//2)
        mostrar_texto(ventana, f"Puntuación final: {puntos}", 
                     ANCHO_VENTANA//3, ALTO_VENTANA//2 + 50)
        mostrar_texto(ventana, f"Nivel alcanzado: {nivel}",
                     ANCHO_VENTANA//3, ALTO_VENTANA//2 + 100)
        pygame.display.flip()
        pygame.time.wait(3000)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()