"""
MÓDULO DE UTILIDADES - CAZADOR DE TESOROS
========================================
Este módulo contiene funciones auxiliares y utilidades generales.

Conceptos enseñados:
- Funciones auxiliares reutilizables
- Carga de recursos centralizada
- Manejo de errores común
"""

import pygame
import os
from configuracion import *

# ============================================================================
# FUNCIONES DE CARGA DE RECURSOS
# ============================================================================

def cargar_imagen(ruta_archivo, tamano=None):
    """
    Carga una imagen desde archivo con manejo de errores
    
    Args:
        ruta_archivo (str): Ruta del archivo de imagen
        tamano (tuple, optional): Tupla (ancho, alto) para redimensionar
        
    Returns:
        pygame.Surface or None: Imagen cargada o None si hubo error
        
    Conceptos enseñados:
    - Carga de imágenes centralizada
    - Manejo de errores robusto
    - Parámetros opcionales
    - Escalado condicional
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(ruta_archivo):
            print(f"Advertencia: No se encontró el archivo {ruta_archivo}")
            return None
        
        # Cargar la imagen
        imagen = pygame.image.load(ruta_archivo)
        
        # Redimensionar si se especifica tamaño
        if tamano:
            imagen = pygame.transform.scale(imagen, tamano)
        
        return imagen
        
    except pygame.error as e:
        print(f"Error al cargar imagen {ruta_archivo}: {e}")
        return None

def cargar_todas_las_imagenes():
    """
    Carga todas las imágenes del juego de una vez
    
    Returns:
        dict: Diccionario con todas las imágenes cargadas
        
    Conceptos enseñados:
    - Carga masiva de recursos
    - Organización en diccionarios
    - Centralización de recursos
    - Validación de recursos críticos
    """
    imagenes = {}
    
    # Definir imágenes y sus tamaños
    recursos_imagenes = {
        'fondo': (ARCHIVO_FONDO, (ANCHO, ALTO)),
        'jugador': (ARCHIVO_JUGADOR, (TAMANO_JUGADOR, TAMANO_JUGADOR)),
        'tesoro': (ARCHIVO_TESORO, (TAMANO_TESORO, TAMANO_TESORO)),
        'enemigo': (ARCHIVO_ENEMIGO, (TAMANO_ENEMIGO, TAMANO_ENEMIGO))
    }
    
    # Cargar cada imagen
    for nombre, (archivo, tamano) in recursos_imagenes.items():
        imagen = cargar_imagen(archivo, tamano)
        if imagen:
            imagenes[nombre] = imagen
        else:
            print(f"Error crítico: No se pudo cargar {nombre}")
            # En caso de error, crear una imagen de placeholder
            imagenes[nombre] = crear_imagen_placeholder(tamano)
    
    return imagenes

def crear_imagen_placeholder(tamano, color=(255, 0, 255)):
    """
    Crea una imagen de placeholder cuando no se puede cargar la original
    
    Args:
        tamano (tuple): Tupla (ancho, alto) del placeholder
        color (tuple): Color RGB del placeholder (magenta por defecto)
        
    Returns:
        pygame.Surface: Imagen de placeholder
        
    Conceptos enseñados:
    - Manejo de recursos faltantes
    - Creación de superficies dinámicas
    - Fallbacks para errores de recursos
    """
    superficie = pygame.Surface(tamano)
    superficie.fill(color)
    
    # Agregar una X para indicar que es un placeholder
    pygame.draw.line(superficie, BLANCO, (0, 0), tamano, 2)
    pygame.draw.line(superficie, BLANCO, (0, tamano[1]), (tamano[0], 0), 2)
    
    return superficie

# ============================================================================
# FUNCIONES MATEMÁTICAS Y GEOMETRÍA
# ============================================================================

def distancia_euclidiana(x1, y1, x2, y2):
    """
    Calcula la distancia euclidiana entre dos puntos
    
    Args:
        x1, y1 (float): Coordenadas del primer punto
        x2, y2 (float): Coordenadas del segundo punto
        
    Returns:
        float: Distancia entre los puntos
        
    Conceptos enseñados:
    - Teorema de Pitágoras
    - Funciones matemáticas básicas
    - Cálculos de distancia
    """
    import math
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def normalizar_vector(x, y):
    """
    Normaliza un vector a longitud unitaria
    
    Args:
        x, y (float): Componentes del vector
        
    Returns:
        tuple: Vector normalizado (x, y)
        
    Conceptos enseñados:
    - Normalización de vectores
    - División por magnitud
    - Manejo de vector cero
    """
    import math
    
    magnitud = math.sqrt(x * x + y * y)
    
    # Evitar división por cero
    if magnitud == 0:
        return (0, 0)
    
    return (x / magnitud, y / magnitud)

def punto_en_rectangulo(x, y, rect_x, rect_y, rect_ancho, rect_alto):
    """
    Verifica si un punto está dentro de un rectángulo
    
    Args:
        x, y (int): Coordenadas del punto
        rect_x, rect_y (int): Esquina superior izquierda del rectángulo
        rect_ancho, rect_alto (int): Dimensiones del rectángulo
        
    Returns:
        bool: True si el punto está dentro del rectángulo
        
    Conceptos enseñados:
    - Detección punto en rectángulo
    - Comparaciones múltiples
    - Lógica geométrica básica
    """
    return (rect_x <= x <= rect_x + rect_ancho and 
            rect_y <= y <= rect_y + rect_alto)

def clamp(valor, minimo, maximo):
    """
    Limita un valor entre un mínimo y máximo
    
    Args:
        valor (float): Valor a limitar
        minimo (float): Valor mínimo permitido
        maximo (float): Valor máximo permitido
        
    Returns:
        float: Valor limitado entre minimo y maximo
        
    Conceptos enseñados:
    - Funciones de utilidad matemática
    - Limitación de rangos
    - Funciones min/max combinadas
    """
    return max(minimo, min(valor, maximo))

# ============================================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================================

def validar_posicion(x, y, ancho_objeto=0, alto_objeto=0):
    """
    Valida si una posición está dentro de los límites de la pantalla
    
    Args:
        x, y (int): Posición a validar
        ancho_objeto, alto_objeto (int): Dimensiones del objeto en esa posición
        
    Returns:
        bool: True si la posición es válida
        
    Conceptos enseñados:
    - Validación de límites
    - Consideración de dimensiones de objetos
    - Prevención de errores de posicionamiento
    """
    return (0 <= x <= ANCHO - ancho_objeto and 
            0 <= y <= ALTO - alto_objeto)

def validar_configuracion():
    """
    Valida que la configuración del juego sea coherente
    
    Returns:
        list: Lista de errores encontrados (vacía si todo está bien)
        
    Conceptos enseñados:
    - Validación de configuración
    - Detección temprana de errores
    - Listas de mensajes de error
    """
    errores = []
    
    # Validar dimensiones de pantalla
    if ANCHO <= 0 or ALTO <= 0:
        errores.append("Las dimensiones de pantalla deben ser positivas")
    
    # Validar tamaños de sprites
    if TAMANO_JUGADOR <= 0 or TAMANO_TESORO <= 0 or TAMANO_ENEMIGO <= 0:
        errores.append("Los tamaños de sprites deben ser positivos")
    
    # Validar velocidades
    if VELOCIDAD_JUGADOR <= 0 or VELOCIDAD_ENEMIGO <= 0:
        errores.append("Las velocidades deben ser positivas")
    
    # Validar número de tesoros
    if NUMERO_TESOROS <= 0 or TESOROS_PARA_GANAR <= 0:
        errores.append("El número de tesoros debe ser positivo")
    
    if TESOROS_PARA_GANAR > NUMERO_TESOROS:
        errores.append("No se pueden requerir más tesoros de los que existen")
    
    # Validar FPS
    if FPS <= 0:
        errores.append("Los FPS deben ser positivos")
    
    return errores

# ============================================================================
# FUNCIONES DE TIEMPO Y ANIMACIÓN
# ============================================================================

def crear_temporizador(duracion_frames):
    """
    Crea un temporizador simple basado en frames
    
    Args:
        duracion_frames (int): Duración en frames del temporizador
        
    Returns:
        dict: Diccionario con información del temporizador
        
    Conceptos enseñados:
    - Temporizadores basados en frames
    - Estructuras de datos para tiempo
    - Inicialización de objetos temporales
    """
    return {
        'duracion_total': duracion_frames,
        'tiempo_restante': duracion_frames,
        'activo': True,
        'terminado': False
    }

def actualizar_temporizador(temporizador):
    """
    Actualiza un temporizador y verifica si ha terminado
    
    Args:
        temporizador (dict): Temporizador a actualizar
        
    Returns:
        bool: True si el temporizador acaba de terminar
        
    Conceptos enseñados:
    - Actualización de temporizadores
    - Detección de eventos temporales
    - Modificación de estado temporal
    """
    if not temporizador['activo']:
        return False
    
    temporizador['tiempo_restante'] -= 1
    
    if temporizador['tiempo_restante'] <= 0:
        temporizador['activo'] = False
        temporizador['terminado'] = True
        return True
    
    return False

def reiniciar_temporizador(temporizador):
    """
    Reinicia un temporizador a su estado inicial
    
    Args:
        temporizador (dict): Temporizador a reiniciar
        
    Conceptos enseñados:
    - Reutilización de temporizadores
    - Restablecimiento de estado temporal
    """
    temporizador['tiempo_restante'] = temporizador['duracion_total']
    temporizador['activo'] = True
    temporizador['terminado'] = False

# ============================================================================
# FUNCIONES DE DEBUG Y DESARROLLO
# ============================================================================

def imprimir_estado_juego(jugador, enemigo, tesoros):
    """
    Imprime el estado actual del juego en la consola (para debug)
    
    Args:
        jugador (dict): Estado del jugador
        enemigo (dict): Estado del enemigo
        tesoros (list): Lista de tesoros
        
    Conceptos enseñados:
    - Funciones de debug
    - Formateo de información de estado
    - Herramientas de desarrollo
    """
    from tesoros import contar_tesoros_recogidos, contar_tesoros_visibles
    
    print("=== ESTADO DEL JUEGO ===")
    print(f"Jugador: ({jugador['x']}, {jugador['y']}) - Vivo: {jugador['vivo']}")
    print(f"Enemigo: ({enemigo['x']}, {enemigo['y']}) - Activo: {enemigo['activo']}")
    print(f"Tesoros recogidos: {contar_tesoros_recogidos(tesoros)}")
    print(f"Tesoros restantes: {contar_tesoros_visibles(tesoros)}")
    print("========================")

def verificar_recursos():
    """
    Verifica que todos los archivos de recursos existan
    
    Returns:
        bool: True si todos los recursos están disponibles
        
    Conceptos enseñados:
    - Verificación de recursos
    - Validación de archivos
    - Prevención de errores de ejecución
    """
    archivos_requeridos = [
        ARCHIVO_FONDO,
        ARCHIVO_JUGADOR,
        ARCHIVO_TESORO,
        ARCHIVO_ENEMIGO
    ]
    
    recursos_disponibles = True
    
    for archivo in archivos_requeridos:
        if not os.path.exists(archivo):
            print(f"Recurso faltante: {archivo}")
            recursos_disponibles = False
        else:
            print(f"Recurso OK: {archivo}")
    
    return recursos_disponibles

# ============================================================================
# FUNCIONES DE CONVERSIÓN Y FORMATEO
# ============================================================================

def frames_a_segundos(frames, fps=FPS):
    """
    Convierte frames a segundos
    
    Args:
        frames (int): Número de frames
        fps (int): Frames por segundo
        
    Returns:
        float: Tiempo en segundos
        
    Conceptos enseñados:
    - Conversión de unidades de tiempo
    - Cálculos de tiempo en juegos
    """
    return frames / fps

def segundos_a_frames(segundos, fps=FPS):
    """
    Convierte segundos a frames
    
    Args:
        segundos (float): Tiempo en segundos
        fps (int): Frames por segundo
        
    Returns:
        int: Número de frames
        
    Conceptos enseñados:
    - Conversión inversa de tiempo
    - Redondeo para frames enteros
    """
    return int(segundos * fps)

def formatear_tiempo(frames, fps=FPS):
    """
    Formatea tiempo en frames a string legible
    
    Args:
        frames (int): Tiempo en frames
        fps (int): Frames por segundo
        
    Returns:
        str: Tiempo formateado como "MM:SS"
        
    Conceptos enseñados:
    - Formateo de tiempo para UI
    - Conversión a formato legible
    - Strings con formato específico
    """
    segundos_totales = frames // fps
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60
    
    return f"{minutos:02d}:{segundos:02d}"