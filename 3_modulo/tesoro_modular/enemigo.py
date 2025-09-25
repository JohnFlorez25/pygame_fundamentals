"""
MÓDULO DEL ENEMIGO - CAZADOR DE TESOROS
======================================
Este módulo maneja todo lo relacionado con el enemigo perseguidor.

Conceptos enseñados:
- Inteligencia artificial básica
- Algoritmo de persecución
- Modularización de enemigos
"""

import pygame
import math
from configuracion import *

# ============================================================================
# FUNCIONES DE INICIALIZACIÓN DEL ENEMIGO
# ============================================================================

def cargar_sprite_enemigo():
    """
    Carga y escala el sprite del enemigo
    
    Returns:
        pygame.Surface: Imagen del enemigo escalada
        
    Conceptos enseñados:
    - Carga de sprites específicos
    - Escalado proporcional
    - Manejo de errores
    """
    try:
        sprite = pygame.image.load(ARCHIVO_ENEMIGO)
        sprite_escalado = pygame.transform.scale(sprite, (TAMANO_ENEMIGO, TAMANO_ENEMIGO))
        return sprite_escalado
    except pygame.error:
        print(f"Error: No se pudo cargar {ARCHIVO_ENEMIGO}")
        return None

def crear_enemigo():
    """
    Crea el estado inicial del enemigo
    
    Returns:
        dict: Diccionario con la información del enemigo
        
    Conceptos enseñados:
    - Inicialización de estado de enemigo
    - Propiedades específicas del perseguidor
    """
    enemigo = {
        'x': ENEMIGO_X_INICIAL,
        'y': ENEMIGO_Y_INICIAL,
        'activo': True
    }
    return enemigo

# ============================================================================
# FUNCIONES DE INTELIGENCIA ARTIFICIAL (IA BÁSICA)
# ============================================================================

def calcular_distancia(x1, y1, x2, y2):
    """
    Calcula la distancia entre dos puntos
    
    Args:
        x1, y1 (int): Coordenadas del primer punto
        x2, y2 (int): Coordenadas del segundo punto
        
    Returns:
        float: Distancia entre los puntos
        
    Conceptos enseñados:
    - Teorema de Pitágoras
    - Cálculos matemáticos básicos
    - Función auxiliar para IA
    """
    diferencia_x = x2 - x1
    diferencia_y = y2 - y1
    distancia = math.sqrt(diferencia_x * diferencia_x + diferencia_y * diferencia_y)
    return distancia

def mover_hacia_objetivo(enemigo, objetivo_x, objetivo_y):
    """
    Mueve al enemigo hacia el objetivo (persecución simple)
    
    Args:
        enemigo (dict): Estado del enemigo
        objetivo_x (int): Posición X del objetivo
        objetivo_y (int): Posición Y del objetivo
        
    Conceptos enseñados:
    - Algoritmo de persecución básico
    - Movimiento basado en diferencias
    - Normalización de movimiento
    - Límites de pantalla para enemigos
    """
    if not enemigo['activo']:
        return
    
    # Calcular la diferencia entre posiciones
    diferencia_x = objetivo_x - enemigo['x']
    diferencia_y = objetivo_y - enemigo['y']
    
    # Mover en X (horizontal)
    if diferencia_x > 0:  # Objetivo está a la derecha
        enemigo['x'] += min(VELOCIDAD_ENEMIGO, diferencia_x)
    elif diferencia_x < 0:  # Objetivo está a la izquierda
        enemigo['x'] += max(-VELOCIDAD_ENEMIGO, diferencia_x)
    
    # Mover en Y (vertical)
    if diferencia_y > 0:  # Objetivo está abajo
        enemigo['y'] += min(VELOCIDAD_ENEMIGO, diferencia_y)
    elif diferencia_y < 0:  # Objetivo está arriba
        enemigo['y'] += max(-VELOCIDAD_ENEMIGO, diferencia_y)
    
    # Aplicar límites de pantalla
    aplicar_limites_enemigo(enemigo)

def aplicar_limites_enemigo(enemigo):
    """
    Mantiene al enemigo dentro de los límites de la pantalla
    
    Args:
        enemigo (dict): Estado del enemigo
        
    Conceptos enseñados:
    - Validación de límites
    - Funciones auxiliares
    - Prevención de errores visuales
    """
    # Límite izquierdo
    if enemigo['x'] < 0:
        enemigo['x'] = 0
    
    # Límite derecho
    if enemigo['x'] > ANCHO - TAMANO_ENEMIGO:
        enemigo['x'] = ANCHO - TAMANO_ENEMIGO
    
    # Límite superior
    if enemigo['y'] < 0:
        enemigo['y'] = 0
    
    # Límite inferior
    if enemigo['y'] > ALTO - TAMANO_ENEMIGO:
        enemigo['y'] = ALTO - TAMANO_ENEMIGO

# ============================================================================
# FUNCIONES DE COMPORTAMIENTO DEL ENEMIGO
# ============================================================================

def actualizar_enemigo(enemigo, jugador):
    """
    Actualiza el comportamiento del enemigo cada frame
    
    Args:
        enemigo (dict): Estado del enemigo
        jugador (dict): Estado del jugador (objetivo)
        
    Conceptos enseñados:
    - Función de actualización principal
    - Comportamiento condicional
    - Integración de múltiples sistemas
    """
    # Solo perseguir si el jugador está vivo
    if jugador['vivo'] and enemigo['activo']:
        # Mover hacia el jugador
        mover_hacia_objetivo(enemigo, jugador['x'], jugador['y'])

def obtener_rect_enemigo(enemigo):
    """
    Crea un rectángulo para el enemigo (usado para colisiones)
    
    Args:
        enemigo (dict): Estado del enemigo
        
    Returns:
        pygame.Rect: Rectángulo del enemigo
        
    Conceptos enseñados:
    - Rectángulos para colisiones
    - Tamaños específicos por entidad
    """
    return pygame.Rect(enemigo['x'], enemigo['y'], TAMANO_ENEMIGO, TAMANO_ENEMIGO)

# ============================================================================
# FUNCIONES DE RENDERIZADO DEL ENEMIGO
# ============================================================================

def dibujar_enemigo(pantalla, sprite_enemigo, enemigo):
    """
    Dibuja el enemigo en la pantalla
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        sprite_enemigo (pygame.Surface): Imagen del enemigo
        enemigo (dict): Estado del enemigo
        
    Conceptos enseñados:
    - Renderizado condicional
    - Uso de sprites específicos
    """
    if enemigo['activo'] and sprite_enemigo:
        pantalla.blit(sprite_enemigo, (enemigo['x'], enemigo['y']))

# ============================================================================
# FUNCIONES DE ESTADO DEL ENEMIGO
# ============================================================================

def reiniciar_enemigo(enemigo):
    """
    Reinicia el estado del enemigo a los valores iniciales
    
    Args:
        enemigo (dict): Estado del enemigo a reiniciar
        
    Conceptos enseñados:
    - Restablecimiento de estado
    - Reutilización para múltiples partidas
    """
    enemigo['x'] = ENEMIGO_X_INICIAL
    enemigo['y'] = ENEMIGO_Y_INICIAL
    enemigo['activo'] = True

def desactivar_enemigo(enemigo):
    """
    Desactiva al enemigo (para pausas o fin de juego)
    
    Args:
        enemigo (dict): Estado del enemigo
        
    Conceptos enseñados:
    - Control de estado de entidades
    - Funciones de control de gameplay
    """
    enemigo['activo'] = False

# ============================================================================
# FUNCIONES DE INFORMACIÓN DEL ENEMIGO
# ============================================================================

def distancia_al_jugador(enemigo, jugador):
    """
    Calcula la distancia entre el enemigo y el jugador
    
    Args:
        enemigo (dict): Estado del enemigo
        jugador (dict): Estado del jugador
        
    Returns:
        float: Distancia entre enemigo y jugador
        
    Conceptos enseñados:
    - Reutilización de funciones auxiliares
    - Cálculos de distancia para gameplay
    """
    return calcular_distancia(enemigo['x'], enemigo['y'], jugador['x'], jugador['y'])