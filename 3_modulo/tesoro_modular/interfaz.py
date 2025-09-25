"""
MÓDULO DE INTERFAZ - CAZADOR DE TESOROS
======================================
Este módulo maneja toda la interfaz de usuario: contadores, mensajes, HUD.

Conceptos enseñados:
- Separación de lógica de UI
- Renderizado de texto e interfaces
- Modularización de elementos visuales
"""

import pygame
from configuracion import *

# ============================================================================
# INICIALIZACIÓN DE FUENTES
# ============================================================================

def inicializar_fuentes():
    """
    Inicializa las fuentes necesarias para el juego
    
    Returns:
        dict: Diccionario con diferentes tamaños de fuente
        
    Conceptos enseñados:
    - Carga de recursos de UI
    - Organización de fuentes por tamaño
    - Centralización de recursos de texto
    """
    fuentes = {
        'grande': pygame.font.Font(None, 72),      # Para títulos
        'mediana': pygame.font.Font(None, 48),     # Para mensajes importantes
        'normal': pygame.font.Font(None, 36),      # Para texto regular
        'pequeña': pygame.font.Font(None, 28)      # Para instrucciones
    }
    return fuentes

# ============================================================================
# FUNCIONES DE HUD (Heads-Up Display)
# ============================================================================

def dibujar_contador_tesoros(pantalla, fuentes, jugador, total_tesoros):
    """
    Dibuja el contador de tesoros recogidos
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        jugador (dict): Estado del jugador
        total_tesoros (int): Número total de tesoros en el juego
        
    Conceptos enseñados:
    - Renderizado de HUD
    - Formateo de strings dinámico
    - Posicionamiento en esquinas
    - Fondos para legibilidad
    """
    fuente = fuentes['mediana']
    
    # Crear el texto del contador
    texto_contador = f"Tesoros: {jugador['tesoros_recogidos']}/{total_tesoros}"
    superficie_texto = fuente.render(texto_contador, True, AMARILLO)
    
    # Calcular posición (esquina superior derecha)
    x = ANCHO - superficie_texto.get_width() - 20
    y = 20
    
    # Dibujar fondo semi-transparente
    ancho_fondo = superficie_texto.get_width() + 20
    alto_fondo = superficie_texto.get_height() + 10
    rect_fondo = pygame.Rect(x - 10, y - 5, ancho_fondo, alto_fondo)
    
    # Fondo oscuro
    pygame.draw.rect(pantalla, NEGRO, rect_fondo)
    # Borde amarillo
    pygame.draw.rect(pantalla, AMARILLO, rect_fondo, 2)
    
    # Dibujar el texto
    pantalla.blit(superficie_texto, (x, y))

def dibujar_estado_jugador(pantalla, fuentes, jugador):
    """
    Muestra el estado actual del jugador (vivo/capturado)
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        jugador (dict): Estado del jugador
        
    Conceptos enseñados:
    - Indicadores de estado visual
    - Renderizado condicional por estado
    - Colores para transmitir información
    """
    if not jugador['vivo']:
        fuente = fuentes['mediana']
        texto_estado = "¡CAPTURADO!"
        superficie_texto = fuente.render(texto_estado, True, ROJO)
        
        # Centrar en la parte superior
        x = (ANCHO - superficie_texto.get_width()) // 2
        y = 80
        
        # Fondo para destacar
        rect_fondo = pygame.Rect(x - 10, y - 5, 
                               superficie_texto.get_width() + 20, 
                               superficie_texto.get_height() + 10)
        pygame.draw.rect(pantalla, NEGRO, rect_fondo)
        pygame.draw.rect(pantalla, ROJO, rect_fondo, 3)
        
        pantalla.blit(superficie_texto, (x, y))

def dibujar_instrucciones(pantalla, fuentes, jugador):
    """
    Muestra las instrucciones de control en pantalla
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        jugador (dict): Estado del jugador
        
    Conceptos enseñados:
    - Texto de ayuda en pantalla
    - Instrucciones contextuales
    - Renderizado múltiple de líneas
    """
    if jugador['vivo']:  # Solo mostrar si el jugador está vivo
        fuente = fuentes['pequeña']
        
        # Instrucciones de movimiento
        instrucciones = [
            "Usa las flechas para mover al explorador",
            "Recoge todos los tesoros",
            "¡Evita al enemigo!"
        ]
        
        y_inicial = 10
        for i, instruccion in enumerate(instrucciones):
            superficie_texto = fuente.render(instruccion, True, BLANCO)
            pantalla.blit(superficie_texto, (10, y_inicial + i * 25))

# ============================================================================
# FUNCIONES DE MENSAJES DE ESTADO
# ============================================================================

def mostrar_mensaje_victoria(pantalla, fuentes, jugador):
    """
    Muestra la pantalla de victoria cuando se completa el objetivo
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        jugador (dict): Estado del jugador
        
    Conceptos enseñados:
    - Pantallas de estado completas
    - Superposición (overlay) semi-transparente
    - Múltiples elementos de texto centrados
    - Mensajes de felicitación dinámicos
    """
    # Crear fondo semi-transparente
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(180)  # Más opaco que antes
    overlay.fill(NEGRO)
    pantalla.blit(overlay, (0, 0))
    
    # Título principal
    fuente_titulo = fuentes['grande']
    titulo = "¡MISIÓN COMPLETADA!"
    superficie_titulo = fuente_titulo.render(titulo, True, VERDE)
    rect_titulo = superficie_titulo.get_rect(center=(ANCHO//2, ALTO//2 - 80))
    pantalla.blit(superficie_titulo, rect_titulo)
    
    # Mensaje de puntuación
    fuente_puntos = fuentes['mediana']
    mensaje_puntos = f"Recogiste {jugador['tesoros_recogidos']} tesoros"
    superficie_puntos = fuente_puntos.render(mensaje_puntos, True, AMARILLO)
    rect_puntos = superficie_puntos.get_rect(center=(ANCHO//2, ALTO//2 - 20))
    pantalla.blit(superficie_puntos, rect_puntos)
    
    # Mensaje de felicitación adicional
    felicitacion = "¡Eres un gran explorador!"
    superficie_felicitacion = fuentes['normal'].render(felicitacion, True, BLANCO)
    rect_felicitacion = superficie_felicitacion.get_rect(center=(ANCHO//2, ALTO//2 + 20))
    pantalla.blit(superficie_felicitacion, rect_felicitacion)
    
    # Instrucciones para continuar
    instrucciones = "Presiona ESPACIO para jugar de nuevo o ESC para salir"
    superficie_instrucciones = fuentes['pequeña'].render(instrucciones, True, BLANCO)
    rect_instrucciones = superficie_instrucciones.get_rect(center=(ANCHO//2, ALTO//2 + 60))
    pantalla.blit(superficie_instrucciones, rect_instrucciones)

def mostrar_mensaje_derrota(pantalla, fuentes, jugador):
    """
    Muestra la pantalla de derrota cuando el enemigo atrapa al jugador
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        jugador (dict): Estado del jugador
        
    Conceptos enseñados:
    - Pantallas de derrota
    - Diferentes tipos de mensaje final
    - Colores para transmitir emociones (rojo = peligro)
    """
    # Crear fondo semi-transparente rojo
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(160)
    overlay.fill((50, 0, 0))  # Rojo oscuro
    pantalla.blit(overlay, (0, 0))
    
    # Título de derrota
    fuente_titulo = fuentes['grande']
    titulo = "¡TE ATRAPARON!"
    superficie_titulo = fuente_titulo.render(titulo, True, ROJO)
    rect_titulo = superficie_titulo.get_rect(center=(ANCHO//2, ALTO//2 - 80))
    pantalla.blit(superficie_titulo, rect_titulo)
    
    # Mensaje con progreso
    fuente_progreso = fuentes['mediana']
    mensaje_progreso = f"Recogiste {jugador['tesoros_recogidos']} de {TESOROS_PARA_GANAR} tesoros"
    superficie_progreso = fuente_progreso.render(mensaje_progreso, True, AMARILLO)
    rect_progreso = superficie_progreso.get_rect(center=(ANCHO//2, ALTO//2 - 20))
    pantalla.blit(superficie_progreso, rect_progreso)
    
    # Mensaje de ánimo
    mensaje_animo = "¡Inténtalo de nuevo!"
    superficie_animo = fuentes['normal'].render(mensaje_animo, True, BLANCO)
    rect_animo = superficie_animo.get_rect(center=(ANCHO//2, ALTO//2 + 20))
    pantalla.blit(superficie_animo, rect_animo)
    
    # Instrucciones para continuar
    instrucciones = "Presiona ESPACIO para jugar de nuevo o ESC para salir"
    superficie_instrucciones = fuentes['pequeña'].render(instrucciones, True, BLANCO)
    rect_instrucciones = superficie_instrucciones.get_rect(center=(ANCHO//2, ALTO//2 + 60))
    pantalla.blit(superficie_instrucciones, rect_instrucciones)

# ============================================================================
# FUNCIONES DE FEEDBACK VISUAL
# ============================================================================

def mostrar_tesoro_recogido(pantalla, fuentes, x, y, tiempo_restante):
    """
    Muestra un mensaje flotante cuando se recoge un tesoro
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        x, y (int): Posición donde mostrar el mensaje
        tiempo_restante (int): Frames restantes para mostrar el mensaje
        
    Conceptos enseñados:
    - Feedback visual inmediato
    - Mensajes temporales
    - Animación básica (desvanecimiento)
    """
    if tiempo_restante <= 0:
        return
    
    # Calcular alpha basado en tiempo restante
    alpha = min(255, tiempo_restante * 8)  # Se desvanece gradualmente
    
    # Crear superficie con transparencia
    fuente = fuentes['normal']
    mensaje = "+1 TESORO!"
    superficie_texto = fuente.render(mensaje, True, AMARILLO)
    
    # Aplicar transparencia
    superficie_texto.set_alpha(alpha)
    
    # Posición que sube gradualmente
    y_animado = y - (30 - tiempo_restante // 2)  # Sube mientras se desvanece
    
    pantalla.blit(superficie_texto, (x, y_animado))

def mostrar_distancia_enemigo(pantalla, fuentes, jugador, enemigo):
    """
    Muestra la distancia al enemigo como indicador de peligro
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        jugador (dict): Estado del jugador
        enemigo (dict): Estado del enemigo
        
    Conceptos enseñados:
    - Indicadores de peligro
    - Cálculo de distancias para UI
    - Colores dinámicos basados en valores
    """
    if not jugador['vivo'] or not enemigo['activo']:
        return
    
    from colisiones import distancia_entre_objetos
    distancia = int(distancia_entre_objetos(jugador, enemigo))
    
    # Determinar color basado en distancia (rojo = cerca, amarillo = lejos)
    if distancia < 100:
        color = ROJO
    elif distancia < 200:
        color = AMARILLO
    else:
        color = VERDE
    
    # Mostrar distancia
    fuente = fuentes['pequeña']
    texto_distancia = f"Enemigo: {distancia}px"
    superficie_texto = fuente.render(texto_distancia, True, color)
    
    # Posición en esquina inferior izquierda
    pantalla.blit(superficie_texto, (10, ALTO - 30))

# ============================================================================
# FUNCIONES DE MENÚ Y PANTALLA DE INICIO
# ============================================================================

def mostrar_pantalla_inicio(pantalla, fuentes):
    """
    Muestra una pantalla de inicio antes de comenzar el juego
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        
    Returns:
        bool: True si se debe iniciar el juego
        
    Conceptos enseñados:
    - Pantallas de menú básicas
    - Manejo de eventos en pantallas específicas
    - Estados de aplicación
    """
    pantalla.fill(NEGRO)
    
    # Título del juego
    titulo = "CAZADOR DE TESOROS"
    superficie_titulo = fuentes['grande'].render(titulo, True, AMARILLO)
    rect_titulo = superficie_titulo.get_rect(center=(ANCHO//2, 150))
    pantalla.blit(superficie_titulo, rect_titulo)
    
    # Subtítulo
    subtitulo = "Versión Modular"
    superficie_subtitulo = fuentes['mediana'].render(subtitulo, True, BLANCO)
    rect_subtitulo = superficie_subtitulo.get_rect(center=(ANCHO//2, 200))
    pantalla.blit(superficie_subtitulo, rect_subtitulo)
    
    # Instrucciones del juego
    instrucciones_juego = [
        "• Recoge todos los tesoros",
        "• Evita al enemigo perseguidor", 
        "• Usa las flechas para moverte",
        "",
        "Presiona ESPACIO para empezar"
    ]
    
    y_inicial = 280
    for i, instruccion in enumerate(instrucciones_juego):
        color = VERDE if instruccion.startswith("Presiona") else BLANCO
        superficie_instruccion = fuentes['normal'].render(instruccion, True, color)
        rect_instruccion = superficie_instruccion.get_rect(center=(ANCHO//2, y_inicial + i * 35))
        pantalla.blit(superficie_instruccion, rect_instruccion)

def mostrar_pausa(pantalla, fuentes):
    """
    Muestra una pantalla de pausa semi-transparente
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        
    Conceptos enseñados:
    - Sistemas de pausa
    - Overlays transparentes
    - Estados de juego adicionales
    """
    # Overlay semi-transparente
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(128)
    overlay.fill(NEGRO)
    pantalla.blit(overlay, (0, 0))
    
    # Mensaje de pausa
    mensaje_pausa = "JUEGO PAUSADO"
    superficie_pausa = fuentes['grande'].render(mensaje_pausa, True, BLANCO)
    rect_pausa = superficie_pausa.get_rect(center=(ANCHO//2, ALTO//2 - 30))
    pantalla.blit(superficie_pausa, rect_pausa)
    
    # Instrucción para continuar
    instruccion = "Presiona P para continuar"
    superficie_instruccion = fuentes['normal'].render(instruccion, True, AMARILLO)
    rect_instruccion = superficie_instruccion.get_rect(center=(ANCHO//2, ALTO//2 + 20))
    pantalla.blit(superficie_instruccion, rect_instruccion)

# ============================================================================
# FUNCIONES DE UTILIDAD PARA UI
# ============================================================================

def centrar_texto(superficie_texto, y):
    """
    Calcula la posición x para centrar texto horizontalmente
    
    Args:
        superficie_texto (pygame.Surface): Superficie del texto renderizado
        y (int): Posición Y donde colocar el texto
        
    Returns:
        tuple: Coordenadas (x, y) para centrar el texto
        
    Conceptos enseñados:
    - Cálculos de centrado
    - Funciones auxiliares para UI
    - Reutilización de lógica de posicionamiento
    """
    x = (ANCHO - superficie_texto.get_width()) // 2
    return (x, y)

def crear_boton_texto(fuente, texto, color_texto, color_fondo, x, y):
    """
    Crea un botón básico con texto y fondo
    
    Args:
        fuente (pygame.Font): Fuente para el texto
        texto (str): Texto del botón
        color_texto (tuple): Color RGB del texto
        color_fondo (tuple): Color RGB del fondo
        x, y (int): Posición del botón
        
    Returns:
        dict: Información del botón (superficie, rect, etc.)
        
    Conceptos enseñados:
    - Creación de elementos UI complejos
    - Botones básicos sin eventos
    - Combinación de texto y gráficos
    """
    # Renderizar texto
    superficie_texto = fuente.render(texto, True, color_texto)
    
    # Crear rectángulo de fondo con padding
    padding = 10
    ancho_boton = superficie_texto.get_width() + padding * 2
    alto_boton = superficie_texto.get_height() + padding
    
    rect_boton = pygame.Rect(x, y, ancho_boton, alto_boton)
    
    # Calcular posición del texto dentro del botón
    texto_x = x + padding
    texto_y = y + padding // 2
    
    boton = {
        'rect': rect_boton,
        'superficie_texto': superficie_texto,
        'posicion_texto': (texto_x, texto_y),
        'color_fondo': color_fondo,
        'activo': True
    }
    
    return boton

def dibujar_boton(pantalla, boton):
    """
    Dibuja un botón creado con crear_boton_texto
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        boton (dict): Información del botón
        
    Conceptos enseñados:
    - Renderizado de elementos UI complejos
    - Separación entre creación y renderizado
    - Reutilización de componentes UI
    """
    if boton['activo']:
        # Dibujar fondo del botón
        pygame.draw.rect(pantalla, boton['color_fondo'], boton['rect'])
        pygame.draw.rect(pantalla, BLANCO, boton['rect'], 2)  # Borde
        
        # Dibujar texto
        pantalla.blit(boton['superficie_texto'], boton['posicion_texto'])

# ============================================================================
# FUNCIONES DE DEBUG (OPCIONAL PARA DESARROLLO)
# ============================================================================

def mostrar_info_debug(pantalla, fuentes, jugador, enemigo, fps_actual):
    """
    Muestra información de debug en la esquina (opcional para desarrollo)
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Diccionario de fuentes
        jugador (dict): Estado del jugador
        enemigo (dict): Estado del enemigo
        fps_actual (int): FPS actuales del juego
        
    Conceptos enseñados:
    - Información de debug para desarrolladores
    - Monitoreo de rendimiento
    - Herramientas de desarrollo
    """
    fuente = fuentes['pequeña']
    
    info_debug = [
        f"FPS: {fps_actual}",
        f"Jugador: ({jugador['x']}, {jugador['y']})",
        f"Enemigo: ({enemigo['x']}, {enemigo['y']})",
        f"Estado: {'Vivo' if jugador['vivo'] else 'Muerto'}"
    ]
    
    # Fondo para legibilidad
    rect_debug = pygame.Rect(ANCHO - 200, ALTO - 120, 190, 110)
    pygame.draw.rect(pantalla, NEGRO, rect_debug)
    pygame.draw.rect(pantalla, BLANCO, rect_debug, 1)
    
    # Mostrar cada línea
    for i, info in enumerate(info_debug):
        superficie_info = fuente.render(info, True, BLANCO)
        pantalla.blit(superficie_info, (ANCHO - 190, ALTO - 110 + i * 20))