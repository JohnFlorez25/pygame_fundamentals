"""
MÓDULO DE COLISIONES - CAZADOR DE TESOROS
========================================
Este módulo centraliza toda la lógica de detección de colisiones del juego.

Conceptos enseñados:
- Centralización de lógica de colisiones
- Funciones especializadas por tipo de colisión
- Separación de responsabilidades
"""

import pygame
from configuracion import *

# ============================================================================
# FUNCIONES BÁSICAS DE DETECCIÓN DE COLISIONES
# ============================================================================

def detectar_colision_rectangulos(rect1, rect2):
    """
    Detecta si dos rectángulos se superponen
    
    Args:
        rect1 (pygame.Rect): Primer rectángulo
        rect2 (pygame.Rect): Segundo rectángulo
        
    Returns:
        bool: True si hay colisión, False si no
        
    Conceptos enseñados:
    - Detección básica de colisiones
    - Función reutilizable para cualquier par de rectángulos
    """
    return rect1.colliderect(rect2)

def detectar_colision_circular(x1, y1, radio1, x2, y2, radio2):
    """
    Detecta colisión entre dos círculos (más precisa para algunos casos)
    
    Args:
        x1, y1 (int): Centro del primer círculo
        radio1 (int): Radio del primer círculo  
        x2, y2 (int): Centro del segundo círculo
        radio2 (int): Radio del segundo círculo
        
    Returns:
        bool: True si hay colisión, False si no
        
    Conceptos enseñados:
    - Detección circular de colisiones
    - Cálculo de distancias
    - Alternativa a colisiones rectangulares
    """
    # Calcular distancia entre centros
    distancia_x = x2 - x1
    distancia_y = y2 - y1
    distancia_cuadrada = distancia_x * distancia_x + distancia_y * distancia_y
    
    # Suma de radios
    suma_radios = radio1 + radio2
    suma_radios_cuadrada = suma_radios * suma_radios
    
    # Hay colisión si la distancia es menor que la suma de radios
    return distancia_cuadrada <= suma_radios_cuadrada

# ============================================================================
# FUNCIONES ESPECÍFICAS DEL JUEGO
# ============================================================================

def verificar_colision_jugador_tesoro(rect_jugador, rect_tesoro):
    """
    Verifica colisión específica entre jugador y un tesoro
    
    Args:
        rect_jugador (pygame.Rect): Rectángulo del jugador
        rect_tesoro (pygame.Rect): Rectángulo del tesoro
        
    Returns:
        bool: True si el jugador toca el tesoro
        
    Conceptos enseñados:
    - Funciones específicas para tipos de entidades
    - Reutilización de funciones básicas
    """
    return detectar_colision_rectangulos(rect_jugador, rect_tesoro)

def verificar_colision_jugador_enemigo(rect_jugador, rect_enemigo):
    """
    Verifica colisión específica entre jugador y enemigo
    
    Args:
        rect_jugador (pygame.Rect): Rectángulo del jugador
        rect_enemigo (pygame.Rect): Rectángulo del enemigo
        
    Returns:
        bool: True si el enemigo atrapa al jugador
        
    Conceptos enseñados:
    - Detección de colisiones peligrosas
    - Separación de lógica por tipo de interacción
    """
    return detectar_colision_rectangulos(rect_jugador, rect_enemigo)

# ============================================================================
# FUNCIONES DE PROCESAMIENTO MASIVO DE COLISIONES
# ============================================================================

def procesar_colisiones_jugador_tesoros(jugador, tesoros):
    """
    Procesa todas las colisiones entre el jugador y los tesoros
    
    Args:
        jugador (dict): Estado del jugador
        tesoros (list): Lista de tesoros
        
    Returns:
        int: Número de tesoros recogidos en este frame
        
    Conceptos enseñados:
    - Procesamiento de colisiones múltiples
    - Modificación de estado durante el procesamiento
    - Contadores de eventos
    - Importación de módulos hermanos
    """
    # Importar funciones de otros módulos (evitar importación circular)
    from jugador import obtener_rect_jugador, agregar_tesoro_jugador
    from tesoros import obtener_rect_tesoro, recoger_tesoro
    
    tesoros_recogidos_ahora = 0  # Contador para este frame
    
    # Solo verificar si el jugador está vivo
    if not jugador['vivo']:
        return 0
    
    # Obtener rectángulo del jugador una vez
    rect_jugador = obtener_rect_jugador(jugador)
    
    # Revisar cada tesoro
    for tesoro in tesoros:
        # Solo verificar tesoros visibles
        if tesoro['visible']:
            rect_tesoro = obtener_rect_tesoro(tesoro)
            
            # Verificar colisión
            if verificar_colision_jugador_tesoro(rect_jugador, rect_tesoro):
                # Recoger el tesoro
                recoger_tesoro(tesoro)
                agregar_tesoro_jugador(jugador)
                tesoros_recogidos_ahora += 1
    
    return tesoros_recogidos_ahora

def procesar_colision_jugador_enemigo(jugador, enemigo):
    """
    Procesa la colisión entre jugador y enemigo
    
    Args:
        jugador (dict): Estado del jugador
        enemigo (dict): Estado del enemigo
        
    Returns:
        bool: True si hubo colisión (jugador capturado)
        
    Conceptos enseñados:
    - Procesamiento de colisión de derrota
    - Modificación de estado crítico
    - Funciones que cambian el estado del juego
    """
    # Solo verificar si ambos están activos
    if not jugador['vivo'] or not enemigo['activo']:
        return False
    
    # Importar funciones necesarias
    from jugador import obtener_rect_jugador, jugador_capturado
    from enemigo import obtener_rect_enemigo
    
    # Obtener rectángulos
    rect_jugador = obtener_rect_jugador(jugador)
    rect_enemigo = obtener_rect_enemigo(enemigo)
    
    # Verificar colisión
    if verificar_colision_jugador_enemigo(rect_jugador, rect_enemigo):
        # El jugador ha sido capturado
        jugador_capturado(jugador)
        return True
    
    return False

# ============================================================================
# FUNCIONES DE UTILIDAD PARA COLISIONES
# ============================================================================

def esta_dentro_de_pantalla(x, y, ancho_objeto, alto_objeto):
    """
    Verifica si un objeto está completamente dentro de los límites de pantalla
    
    Args:
        x, y (int): Posición del objeto
        ancho_objeto, alto_objeto (int): Dimensiones del objeto
        
    Returns:
        bool: True si está dentro, False si sale de los límites
        
    Conceptos enseñados:
    - Validación de límites de pantalla
    - Función auxiliar para prevenir errores
    """
    return (x >= 0 and y >= 0 and 
            x + ancho_objeto <= ANCHO and 
            y + alto_objeto <= ALTO)

def distancia_entre_objetos(obj1, obj2):
    """
    Calcula la distancia entre los centros de dos objetos
    
    Args:
        obj1, obj2 (dict): Objetos con propiedades 'x' e 'y'
        
    Returns:
        float: Distancia entre los centros
        
    Conceptos enseñados:
    - Cálculo de distancias entre objetos
    - Función auxiliar para IA y gameplay
    - Uso de propiedades de diccionarios
    """
    import math
    
    dx = obj2['x'] - obj1['x']
    dy = obj2['y'] - obj1['y']
    return math.sqrt(dx * dx + dy * dy)

def objetos_se_superponen(obj1, obj2, margen=0):
    """
    Verifica si dos objetos se superponen considerando un margen adicional
    
    Args:
        obj1, obj2 (dict): Objetos con posición y tamaño implícito
        margen (int): Margen adicional para la detección
        
    Returns:
        bool: True si se superponen (considerando margen)
        
    Conceptos enseñados:
    - Detección con tolerancia
    - Uso de márgenes para gameplay
    - Flexibilidad en detección de colisiones
    """
    # Crear rectángulos expandidos con margen
    rect1 = pygame.Rect(obj1['x'] - margen, obj1['y'] - margen, 
                       TAMANO_JUGADOR + 2*margen, TAMANO_JUGADOR + 2*margen)
    rect2 = pygame.Rect(obj2['x'] - margen, obj2['y'] - margen,
                       TAMANO_TESORO + 2*margen, TAMANO_TESORO + 2*margen)
    
    return detectar_colision_rectangulos(rect1, rect2)

# ============================================================================
# FUNCIONES DE ANÁLISIS DE COLISIONES
# ============================================================================

def obtener_lado_colision(rect1, rect2):
    """
    Determina desde qué lado se produce una colisión
    
    Args:
        rect1, rect2 (pygame.Rect): Rectángulos que colisionan
        
    Returns:
        str: 'izquierda', 'derecha', 'arriba', 'abajo' o 'centro'
        
    Conceptos enseñados:
    - Análisis detallado de colisiones
    - Determinación de dirección de impacto
    - Lógica condicional compleja
    """
    centro1_x = rect1.centerx
    centro1_y = rect1.centery
    centro2_x = rect2.centerx  
    centro2_y = rect2.centery
    
    # Calcular diferencias
    diff_x = centro2_x - centro1_x
    diff_y = centro2_y - centro1_y
    
    # Determinar lado basado en la diferencia mayor
    if abs(diff_x) > abs(diff_y):
        return 'derecha' if diff_x > 0 else 'izquierda'
    else:
        return 'abajo' if diff_y > 0 else 'arriba'