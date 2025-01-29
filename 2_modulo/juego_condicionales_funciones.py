"""
Juego simple desarrollado con Pygame donde un jugador (cuadrado rojo) debe recolectar
objetivos (cuadrados verdes) mientras evita obstáculos móviles (cuadrados azules).

Métodos principales de Pygame utilizados:
- pygame.init(): Inicializa todos los módulos de Pygame
- pygame.display.set_mode(): Crea la ventana del juego
- pygame.display.set_caption(): Establece el título de la ventana
- pygame.event.get(): Obtiene todos los eventos (teclado, mouse, etc.)
- pygame.key.get_pressed(): Obtiene el estado de todas las teclas
- pygame.draw.rect(): Dibuja rectángulos en la pantalla
- pygame.display.flip(): Actualiza toda la pantalla
- pygame.time.Clock(): Controla la velocidad del juego
- pygame.quit(): Finaliza Pygame
"""

import pygame
import random

# Inicializar todos los módulos de Pygame necesarios para el juego
pygame.init()

def configurar_ventana():
    """
    Configura la ventana principal del juego.
    
    Métodos Pygame utilizados:
    - pygame.display.set_mode(): Crea la ventana con las dimensiones especificadas
    - pygame.display.set_caption(): Establece el título que aparecerá en la ventana

    Returns:
        tuple: Retorna una tupla con:
            - ventana: Superficie principal de dibujo
            - ancho_ventana: Ancho en píxeles
            - alto_ventana: Alto en píxeles
    """
    ancho_ventana = 800
    alto_ventana = 600
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("Version 2 - Juego en Pygame")
    return ventana, ancho_ventana, alto_ventana

def mover_jugador(x, y, velocidad, teclas, ancho_ventana, alto_ventana, tamanio):
    """
    Actualiza la posición del jugador basado en las teclas presionadas.
    
    Métodos Pygame utilizados:
    - pygame.K_LEFT, K_RIGHT, K_UP, K_DOWN: Constantes que representan las teclas de flecha

    Args:
        x (int): Posición actual en X
        y (int): Posición actual en Y
        velocidad (int): Velocidad de movimiento en píxeles
        teclas (pygame.key.ScancodeWrapper): Estado de todas las teclas
        ancho_ventana (int): Ancho de la ventana para límites
        alto_ventana (int): Alto de la ventana para límites
        tamanio (int): Tamaño del jugador para límites

    Returns:
        tuple: Nueva posición (x, y) del jugador
    """
    # Mover según las teclas presionadas
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Mantener al jugador dentro de los límites de la ventana
    x = max(0, min(x, ancho_ventana - tamanio))
    y = max(0, min(y, alto_ventana - tamanio))

    return x, y

def mover_obstaculo(obstaculo_x, velocidad, direccion, ancho_ventana, tamanio):
    """
    Actualiza la posición de un obstáculo y maneja los rebotes en los bordes.
    
    Args:
        obstaculo_x (int): Posición actual en X
        velocidad (int): Velocidad de movimiento
        direccion (int): Dirección del movimiento (1 o -1)
        ancho_ventana (int): Ancho de la ventana para límites
        tamanio (int): Tamaño del obstáculo

    Returns:
        tuple: Nueva posición X y nueva dirección
    """
    obstaculo_x += velocidad * direccion
    
    # Cambiar dirección al tocar los bordes
    if obstaculo_x <= 0 or obstaculo_x >= ancho_ventana - tamanio:
        direccion *= -1
        
    return obstaculo_x, direccion

def hay_colision(x1, y1, tamanio1, x2, y2, tamanio2):
    """
    Detecta si hay colisión entre dos objetos rectangulares.
    Utiliza el método de detección de colisiones AABB (Axis-Aligned Bounding Box).

    Args:
        x1, y1 (int): Posición del primer objeto
        tamanio1 (int): Tamaño del primer objeto
        x2, y2 (int): Posición del segundo objeto
        tamanio2 (int): Tamaño del segundo objeto

    Returns:
        bool: True si hay colisión, False si no
    """
    return (x1 < x2 + tamanio2 and
            x1 + tamanio1 > x2 and
            y1 < y2 + tamanio2 and
            y1 + tamanio1 > y2)

def generar_posicion_aleatoria(ancho_ventana, alto_ventana, tamanio):
    """
    Genera una posición aleatoria dentro de los límites de la ventana.
    
    Args:
        ancho_ventana (int): Ancho de la ventana
        alto_ventana (int): Alto de la ventana
        tamanio (int): Tamaño del objeto para ajustar límites

    Returns:
        tuple: Coordenadas (x, y) aleatorias
    """
    x = random.randint(0, ancho_ventana - tamanio)
    y = random.randint(0, alto_ventana - tamanio)
    return x, y

def dibujar_rectangulo(ventana, x, y, tamanio, color):
    """
    Dibuja un rectángulo en la ventana.
    
    Métodos Pygame utilizados:
    - pygame.draw.rect(): Dibuja un rectángulo en una superficie

    Args:
        ventana (pygame.Surface): Superficie donde dibujar
        x, y (int): Posición del rectángulo
        tamanio (int): Tamaño del rectángulo
        color (tuple): Color RGB del rectángulo
    """
    pygame.draw.rect(ventana, color, (x, y, tamanio, tamanio))

def mostrar_texto(ventana, texto, x, y, color=(255, 255, 255)):
    """
    Muestra texto en la ventana.
    
    Métodos Pygame utilizados:
    - pygame.font.Font(): Crea un objeto fuente para renderizar texto
    - font.render(): Renderiza el texto en una superficie
    - surface.blit(): Dibuja una superficie sobre otra

    Args:
        ventana (pygame.Surface): Superficie donde dibujar
        texto (str): Texto a mostrar
        x, y (int): Posición del texto
        color (tuple): Color RGB del texto
    """
    fuente = pygame.font.Font(None, 36)
    superficie = fuente.render(texto, True, color)
    ventana.blit(superficie, (x, y))

def main():
    """
    Función principal del juego que controla todo el flujo de ejecución.
    
    Esta función maneja:
    - Inicialización de todos los elementos del juego
    - Bucle principal de eventos y actualización
    - Lógica de colisiones y puntuación
    - Renderizado de gráficos
    - Finalización del juego
    """
    
    # === INICIALIZACIÓN DE VARIABLES ===
    # Configuración de la ventana del juego
    ventana, ancho_ventana, alto_ventana = configurar_ventana()
    
    # Configuración inicial del jugador
    jugador_x = 100              # Posición inicial X del jugador
    jugador_y = 100              # Posición inicial Y del jugador
    jugador_tamanio = 50         # Tamaño del cuadrado del jugador
    velocidad_normal = 5         # Velocidad base de movimiento
    velocidad = velocidad_normal # Velocidad actual (puede cambiar con boost)
    vidas = 3                    # Número inicial de vidas
    puntos = 0                   # Contador de puntuación
    
    # Configuración del objetivo (cuadrado verde)
    objetivo_tamanio = 20        # Tamaño del objetivo
    # Generar posición inicial aleatoria para el objetivo
    objetivo_x, objetivo_y = generar_posicion_aleatoria(ancho_ventana, alto_ventana, objetivo_tamanio)
    
    # Configuración de los obstáculos (cuadrados azules)
    obstaculo_tamanio = 30       # Tamaño de los obstáculos
    # Generar posiciones iniciales aleatorias para los obstáculos
    obstaculo1_x, obstaculo1_y = generar_posicion_aleatoria(ancho_ventana, alto_ventana, obstaculo_tamanio)
    obstaculo2_x, obstaculo2_y = generar_posicion_aleatoria(ancho_ventana, alto_ventana, obstaculo_tamanio)
    obstaculo_velocidad = 3      # Velocidad inicial de los obstáculos
    direccion1 = 1               # Dirección del primer obstáculo (1: derecha, -1: izquierda)
    direccion2 = -1              # Dirección del segundo obstáculo (comienza en dirección opuesta)
    
    # Definición de colores en formato RGB
    COLOR_NEGRO = (0, 0, 0)      # Color de fondo
    COLOR_ROJO = (255, 0, 0)     # Color del jugador
    COLOR_VERDE = (0, 255, 0)    # Color del objetivo
    COLOR_AZUL = (0, 0, 255)     # Color de los obstáculos
    
    # Configuración del control de FPS
    reloj = pygame.time.Clock()   # Reloj para controlar la velocidad del juego
    corriendo = True             # Variable de control del bucle principal

    # === BUCLE PRINCIPAL DEL JUEGO ===
    while corriendo and vidas > 0:
        # --- MANEJO DE EVENTOS ---
        # Procesar todos los eventos de Pygame
        for evento in pygame.event.get():
            # Verificar si se cerró la ventana
            if evento.type == pygame.QUIT:
                corriendo = False
            # Verificar si se presionó una tecla
            elif evento.type == pygame.KEYDOWN:
                # Activar boost de velocidad con la barra espaciadora
                if evento.key == pygame.K_SPACE:
                    velocidad = 10
            # Verificar si se soltó una tecla
            elif evento.type == pygame.KEYUP:
                # Desactivar boost de velocidad al soltar la barra espaciadora
                if evento.key == pygame.K_SPACE:
                    velocidad = velocidad_normal

        # --- ACTUALIZACIÓN DE ESTADO ---
        # Obtener estado actual de todas las teclas
        teclas = pygame.key.get_pressed()
        # Actualizar posición del jugador según las teclas presionadas
        jugador_x, jugador_y = mover_jugador(jugador_x, jugador_y, velocidad, teclas, 
                                           ancho_ventana, alto_ventana, jugador_tamanio)
        
        # Actualizar posición de los obstáculos
        obstaculo1_x, direccion1 = mover_obstaculo(obstaculo1_x, obstaculo_velocidad, 
                                                  direccion1, ancho_ventana, obstaculo_tamanio)
        obstaculo2_x, direccion2 = mover_obstaculo(obstaculo2_x, obstaculo_velocidad, 
                                                  direccion2, ancho_ventana, obstaculo_tamanio)
            
        # --- DETECCIÓN DE COLISIONES ---
        # Verificar si el jugador chocó con algún obstáculo
        if hay_colision(jugador_x, jugador_y, jugador_tamanio, 
                       obstaculo1_x, obstaculo1_y, obstaculo_tamanio) or \
           hay_colision(jugador_x, jugador_y, jugador_tamanio, 
                       obstaculo2_x, obstaculo2_y, obstaculo_tamanio):
            vidas -= 1  # Reducir una vida
            # Reposicionar al jugador en su punto inicial
            jugador_x = 100
            jugador_y = 100

        # Verificar si el jugador alcanzó el objetivo
        if hay_colision(jugador_x, jugador_y, jugador_tamanio, 
                       objetivo_x, objetivo_y, objetivo_tamanio):
            puntos += 10  # Aumentar puntuación
            # Generar nueva posición aleatoria para el objetivo
            objetivo_x, objetivo_y = generar_posicion_aleatoria(ancho_ventana, alto_ventana, 
                                                              objetivo_tamanio)
            
            # Sistema de dificultad progresiva
            if puntos % 50 == 0:  # Cada 50 puntos
                obstaculo_velocidad += 1  # Aumentar velocidad de los obstáculos

        # --- RENDERIZADO ---
        # Limpiar la pantalla con el color de fondo
        ventana.fill(COLOR_NEGRO)
        
        # Dibujar todos los elementos del juego
        dibujar_rectangulo(ventana, jugador_x, jugador_y, jugador_tamanio, COLOR_ROJO)
        dibujar_rectangulo(ventana, objetivo_x, objetivo_y, objetivo_tamanio, COLOR_VERDE)
        dibujar_rectangulo(ventana, obstaculo1_x, obstaculo1_y, obstaculo_tamanio, COLOR_AZUL)
        dibujar_rectangulo(ventana, obstaculo2_x, obstaculo2_y, obstaculo_tamanio, COLOR_AZUL)

        # Mostrar información del juego en pantalla
        mostrar_texto(ventana, f"Puntos: {puntos}", 10, 10)
        mostrar_texto(ventana, f"Vidas: {vidas}", 10, 50)

        # Actualizar la pantalla completa
        pygame.display.flip()
        # Mantener el juego a 60 FPS
        reloj.tick(60)

    # === PANTALLA DE FIN DE JUEGO ===
    if vidas <= 0:  # Si el jugador perdió todas las vidas
        # Limpiar pantalla y mostrar mensaje de fin de juego
        ventana.fill(COLOR_NEGRO)
        mostrar_texto(ventana, "¡Juego Terminado!", ancho_ventana//3, alto_ventana//2)
        mostrar_texto(ventana, f"Puntuación final: {puntos}", 
                     ancho_ventana//3, alto_ventana//2 + 50)
        pygame.display.flip()
        # Esperar 3 segundos antes de cerrar
        pygame.time.wait(3000)

    # Cerrar Pygame
    pygame.quit()

if __name__ == "__main__":
    main()