"""
MÓDULO DE TESOROS - CAZADOR DE TESOROS
=====================================
Este módulo maneja todo lo relacionado con la generación y gestión de tesoros.

Conceptos enseñados:
- Generación procedural básica
- Gestión de colecciones de objetos
- Modularización de game objects
"""

import pygame
import random
from configuracion import *

# ============================================================================
# FUNCIONES DE INICIALIZACIÓN DE TESOROS
# ============================================================================

def cargar_sprite_tesoro():
    """
    Carga y escala el sprite de los tesoros
    
    Returns:
        pygame.Surface: Imagen del tesoro escalada
        
    Conceptos enseñados:
    - Carga de sprites reutilizables
    - Escalado uniforme
    - Manejo de errores en recursos
    """
    try:
        sprite = pygame.image.load(ARCHIVO_TESORO)
        sprite_escalado = pygame.transform.scale(sprite, (TAMANO_TESORO, TAMANO_TESORO))
        return sprite_escalado
    except pygame.error:
        print(f"Error: No se pudo cargar {ARCHIVO_TESORO}")
        return None

def crear_tesoro(x, y):
    """
    Crea un tesoro individual en una posición específica
    
    Args:
        x (int): Posición X del tesoro
        y (int): Posición Y del tesoro
        
    Returns:
        dict: Diccionario con la información del tesoro
        
    Conceptos enseñados:
    - Creación de objetos individuales
    - Parámetros de posición
    - Estructura de datos para objetos
    """
    tesoro = {
        'x': x,
        'y': y,
        'visible': True,
        'recogido': False
    }
    return tesoro

# ============================================================================
# FUNCIONES DE GENERACIÓN DE TESOROS
# ============================================================================

def generar_posicion_aleatoria():
    """
    Genera una posición aleatoria válida para un tesoro
    
    Returns:
        tuple: Tupla con coordenadas (x, y) aleatorias
        
    Conceptos enseñados:
    - Generación de números aleatorios
    - Cálculo de rangos válidos
    - Prevención de spawn en bordes
    """
    x = random.randint(MARGEN_BORDE, ANCHO - MARGEN_TESORO)
    y = random.randint(MARGEN_BORDE, ALTO - MARGEN_TESORO)
    return x, y

def verificar_distancia_minima(nuevo_x, nuevo_y, tesoros_existentes, distancia_minima=80):
    """
    Verifica que un nuevo tesoro no esté muy cerca de otros tesoros
    
    Args:
        nuevo_x (int): Posición X del nuevo tesoro
        nuevo_y (int): Posición Y del nuevo tesoro
        tesoros_existentes (list): Lista de tesoros ya creados
        distancia_minima (int): Distancia mínima entre tesoros
        
    Returns:
        bool: True si la posición es válida, False si está muy cerca
        
    Conceptos enseñados:
    - Validación de posiciones
    - Bucles para verificar condiciones
    - Prevención de overlap entre objetos
    """
    for tesoro in tesoros_existentes:
        # Calcular distancia con teorema de Pitágoras simplificado
        diferencia_x = nuevo_x - tesoro['x']
        diferencia_y = nuevo_y - tesoro['y']
        distancia_cuadrada = diferencia_x * diferencia_x + diferencia_y * diferencia_y
        
        # Comparar con distancia mínima al cuadrado (evita usar sqrt)
        if distancia_cuadrada < distancia_minima * distancia_minima:
            return False
    
    return True

def crear_lista_tesoros(cantidad):
    """
    Crea una lista completa de tesoros en posiciones aleatorias válidas
    
    Args:
        cantidad (int): Número de tesoros a crear
        
    Returns:
        list: Lista de diccionarios con información de cada tesoro
        
    Conceptos enseñados:
    - Bucles con intentos limitados
    - Generación procedural con validación
    - Prevención de bucles infinitos
    - Construcción de listas
    """
    tesoros = []  # Lista vacía para almacenar tesoros
    intentos_maximos = 100  # Prevenir bucles infinitos
    
    for i in range(cantidad):
        tesoro_colocado = False
        intentos = 0
        
        # Intentar colocar tesoro hasta encontrar posición válida
        while not tesoro_colocado and intentos < intentos_maximos:
            x, y = generar_posicion_aleatoria()
            
            # Verificar que no esté muy cerca de otros tesoros
            if verificar_distancia_minima(x, y, tesoros):
                nuevo_tesoro = crear_tesoro(x, y)
                tesoros.append(nuevo_tesoro)
                tesoro_colocado = True
            
            intentos += 1
        
        # Si no se pudo colocar después de muchos intentos, usar posición aleatoria simple
        if not tesoro_colocado:
            x, y = generar_posicion_aleatoria()
            nuevo_tesoro = crear_tesoro(x, y)
            tesoros.append(nuevo_tesoro)
    
    return tesoros

# ============================================================================
# FUNCIONES DE GESTIÓN DE TESOROS
# ============================================================================

def obtener_rect_tesoro(tesoro):
    """
    Crea un rectángulo para un tesoro (usado para colisiones)
    
    Args:
        tesoro (dict): Estado del tesoro
        
    Returns:
        pygame.Rect: Rectángulo del tesoro
        
    Conceptos enseñados:
    - Creación de rectángulos para colisiones
    - Uso de tamaños específicos
    """
    return pygame.Rect(tesoro['x'], tesoro['y'], TAMANO_TESORO, TAMANO_TESORO)

def recoger_tesoro(tesoro):
    """
    Marca un tesoro como recogido
    
    Args:
        tesoro (dict): Tesoro a recoger
        
    Conceptos enseñados:
    - Modificación de estado de objetos
    - Cambio de múltiples propiedades
    """
    tesoro['visible'] = False
    tesoro['recogido'] = True

def contar_tesoros_visibles(tesoros):
    """
    Cuenta cuántos tesoros siguen visibles (no recogidos)
    
    Args:
        tesoros (list): Lista de tesoros
        
    Returns:
        int: Número de tesoros visibles
        
    Conceptos enseñados:
    - Recorrido de listas con contador
    - Filtrado por condiciones
    - Función de consulta
    """
    contador = 0
    for tesoro in tesoros:
        if tesoro['visible']:
            contador += 1
    return contador

def contar_tesoros_recogidos(tesoros):
    """
    Cuenta cuántos tesoros han sido recogidos
    
    Args:
        tesoros (list): Lista de tesoros
        
    Returns:
        int: Número de tesoros recogidos
        
    Conceptos enseñados:
    - Contadores con condiciones
    - Reutilización de lógica de conteo
    """
    contador = 0
    for tesoro in tesoros:
        if tesoro['recogido']:
            contador += 1
    return contador

# ============================================================================
# FUNCIONES DE RENDERIZADO DE TESOROS
# ============================================================================

def dibujar_tesoros(pantalla, sprite_tesoro, tesoros):
    """
    Dibuja todos los tesoros visibles en la pantalla
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        sprite_tesoro (pygame.Surface): Imagen del tesoro
        tesoros (list): Lista de tesoros
        
    Conceptos enseñados:
    - Bucle de renderizado
    - Renderizado condicional
    - Reutilización de sprites
    """
    if not sprite_tesoro:
        return
    
    for tesoro in tesoros:
        if tesoro['visible']:  # Solo dibujar tesoros visibles
            pantalla.blit(sprite_tesoro, (tesoro['x'], tesoro['y']))

# ============================================================================
# FUNCIONES DE UTILIDAD PARA TESOROS
# ============================================================================

def reiniciar_tesoros(tesoros):
    """
    Reinicia todos los tesoros a su estado inicial (visibles)
    
    Args:
        tesoros (list): Lista de tesoros a reiniciar
        
    Conceptos enseñados:
    - Modificación de todos los elementos de una lista
    - Restablecimiento de estado masivo
    - Reutilización de objetos existentes
    """
    for tesoro in tesoros:
        tesoro['visible'] = True
        tesoro['recogido'] = False

def obtener_tesoros_visibles(tesoros):
    """
    Retorna una lista de solo los tesoros que están visibles
    
    Args:
        tesoros (list): Lista completa de tesoros
        
    Returns:
        list: Lista filtrada con solo tesoros visibles
        
    Conceptos enseñados:
    - Filtrado de listas
    - Creación de sublistas
    - Comprensión de listas básica
    """
    tesoros_visibles = []
    for tesoro in tesoros:
        if tesoro['visible']:
            tesoros_visibles.append(tesoro)
    return tesoros_visibles

def obtener_posiciones_tesoros(tesoros):
    """
    Extrae solo las posiciones de todos los tesoros visibles
    
    Args:
        tesoros (list): Lista de tesoros
        
    Returns:
        list: Lista de tuplas con posiciones (x, y)
        
    Conceptos enseñados:
    - Extracción de datos específicos
    - Transformación de estructuras de datos
    - Creación de tuplas
    """
    posiciones = []
    for tesoro in tesoros:
        if tesoro['visible']:
            posicion = (tesoro['x'], tesoro['y'])
            posiciones.append(posicion)
    return posiciones

# ============================================================================
# FUNCIONES DE INFORMACIÓN Y ESTADÍSTICAS
# ============================================================================

def tesoro_mas_cercano(tesoros, x, y):
    """
    Encuentra el tesoro visible más cercano a una posición dada
    
    Args:
        tesoros (list): Lista de tesoros
        x, y (int): Posición de referencia
        
    Returns:
        dict or None: Tesoro más cercano o None si no hay tesoros visibles
        
    Conceptos enseñados:
    - Algoritmo de búsqueda del mínimo
    - Cálculo de distancias
    - Manejo de casos especiales (lista vacía)
    """
    tesoro_cercano = None
    distancia_minima = float('inf')  # Infinito como valor inicial
    
    for tesoro in tesoros:
        if tesoro['visible']:
            # Calcular distancia (sin raíz cuadrada para eficiencia)
            dx = tesoro['x'] - x
            dy = tesoro['y'] - y
            distancia = dx * dx + dy * dy
            
            if distancia < distancia_minima:
                distancia_minima = distancia
                tesoro_cercano = tesoro
    
    return tesoro_cercano

def todos_tesoros_recogidos(tesoros):
    """
    Verifica si todos los tesoros han sido recogidos
    
    Args:
        tesoros (list): Lista de tesoros
        
    Returns:
        bool: True si todos fueron recogidos, False si falta alguno
        
    Conceptos enseñados:
    - Verificación de condiciones en listas
    - Funciones que retornan booleanos
    - Lógica de finalización de objetivos
    """
    for tesoro in tesoros:
        if tesoro['visible']:  # Si hay alguno visible, no están todos recogidos
            return False
    return True  # Si llegamos aquí, todos están recogidos