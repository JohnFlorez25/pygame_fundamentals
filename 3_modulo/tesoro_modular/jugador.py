"""
MÓDULO DEL JUGADOR - CAZADOR DE TESOROS
======================================
Este módulo maneja todo lo relacionado con el explorador.

Conceptos enseñados:
- Modularización por responsabilidades
- Funciones específicas para una entidad
- Separación de lógica del jugador
"""

import pygame
from configuracion import *

# ============================================================================
# FUNCIONES DE INICIALIZACIÓN DEL JUGADOR
# ============================================================================

def cargar_sprite_jugador():
    """
    Carga y escala el sprite del jugador
    
    Returns:
        pygame.Surface: Imagen del jugador escalada
        
    Conceptos enseñados:
    - Carga de imágenes específicas
    - Escalado de sprites
    - Manejo de errores
    """
    try:
        sprite = pygame.image.load(ARCHIVO_JUGADOR)
        sprite_escalado = pygame.transform.scale(sprite, (TAMANO_JUGADOR, TAMANO_JUGADOR))
        return sprite_escalado
    except pygame.error:
        print(f"Error: No se pudo cargar {ARCHIVO_JUGADOR}")
        return None

def crear_jugador():
    """
    Crea el estado inicial del jugador
    
    Returns:
        dict: Diccionario con la información del jugador
        
    Conceptos enseñados:
    - Inicialización de estado
    - Uso de diccionarios para datos estructurados
    - Valores por defecto
    """
    jugador = {
        'x': JUGADOR_X_INICIAL,
        'y': JUGADOR_Y_INICIAL,
        'vivo': True,
        'tesoros_recogidos': 0
    }
    return jugador

# ============================================================================
# FUNCIONES DE MOVIMIENTO DEL JUGADOR
# ============================================================================

def mover_jugador(jugador, teclas_presionadas):
    """
    Actualiza la posición del jugador según las teclas presionadas
    
    Args:
        jugador (dict): Estado actual del jugador
        teclas_presionadas (pygame.key): Estado de las teclas
        
    Conceptos enseñados:
    - Modificación de diccionarios
    - Condicionales múltiples
    - Límites de pantalla
    - Validación de movimiento
    """
    # Solo mover si el jugador está vivo
    if not jugador['vivo']:
        return
    
    # Mover hacia la izquierda
    if teclas_presionadas[pygame.K_LEFT] and jugador['x'] > 0:
        jugador['x'] -= VELOCIDAD_JUGADOR
    
    # Mover hacia la derecha
    if teclas_presionadas[pygame.K_RIGHT] and jugador['x'] < ANCHO - TAMANO_JUGADOR:
        jugador['x'] += VELOCIDAD_JUGADOR
    
    # Mover hacia arriba
    if teclas_presionadas[pygame.K_UP] and jugador['y'] > 0:
        jugador['y'] -= VELOCIDAD_JUGADOR
    
    # Mover hacia abajo
    if teclas_presionadas[pygame.K_DOWN] and jugador['y'] < ALTO - TAMANO_JUGADOR:
        jugador['y'] += VELOCIDAD_JUGADOR

def obtener_rect_jugador(jugador):
    """
    Crea un rectángulo para el jugador (usado para colisiones)
    
    Args:
        jugador (dict): Estado del jugador
        
    Returns:
        pygame.Rect: Rectángulo del jugador
        
    Conceptos enseñados:
    - Creación de rectángulos para colisiones
    - Acceso a datos del diccionario
    """
    return pygame.Rect(jugador['x'], jugador['y'], TAMANO_JUGADOR, TAMANO_JUGADOR)

# ============================================================================
# FUNCIONES DE RENDERIZADO DEL JUGADOR
# ============================================================================

def dibujar_jugador(pantalla, sprite_jugador, jugador):
    """
    Dibuja el jugador en la pantalla
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        sprite_jugador (pygame.Surface): Imagen del jugador
        jugador (dict): Estado del jugador
        
    Conceptos enseñados:
    - Renderizado condicional
    - Uso de coordenadas del diccionario
    """
    if jugador['vivo'] and sprite_jugador:
        pantalla.blit(sprite_jugador, (jugador['x'], jugador['y']))

# ============================================================================
# FUNCIONES DE ESTADO DEL JUGADOR
# ============================================================================

def jugador_capturado(jugador):
    """
    Marca al jugador como capturado (pierde el juego)
    
    Args:
        jugador (dict): Estado del jugador
        
    Conceptos enseñados:
    - Modificación de estado
    - Lógica de derrota
    """
    jugador['vivo'] = False

def reiniciar_jugador(jugador):
    """
    Reinicia el estado del jugador a los valores iniciales
    
    Args:
        jugador (dict): Estado del jugador a reiniciar
        
    Conceptos enseñados:
    - Restablecimiento de estado
    - Reutilización de valores de configuración
    """
    jugador['x'] = JUGADOR_X_INICIAL
    jugador['y'] = JUGADOR_Y_INICIAL
    jugador['vivo'] = True
    jugador['tesoros_recogidos'] = 0

def agregar_tesoro_jugador(jugador):
    """
    Incrementa el contador de tesoros del jugador
    
    Args:
        jugador (dict): Estado del jugador
        
    Conceptos enseñados:
    - Incremento de contadores
    - Modificación de estado del jugador
    """
    jugador['tesoros_recogidos'] += 1

def jugador_ha_ganado(jugador):
    """
    Verifica si el jugador ha recogido suficientes tesoros para ganar
    
    Args:
        jugador (dict): Estado del jugador
        
    Returns:
        bool: True si ha ganado, False si no
        
    Conceptos enseñados:
    - Funciones que retornan booleanos
    - Condiciones de victoria
    """
    return jugador['tesoros_recogidos'] >= TESOROS_PARA_GANAR