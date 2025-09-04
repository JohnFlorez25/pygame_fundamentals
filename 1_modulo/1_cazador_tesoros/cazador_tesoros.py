"""
JUEGO DEL CAZADOR DE TESOROS
============================
Autor: John Faber Flórez Vasco
Versión: 1.0
Propósito: Demostrar el uso de funciones, condicionales y estructura básica de videojuegos
"""

import pygame  # Librería para crear videojuegos
import sys     # Librería del sistema para cerrar el programa

# ============================================================================
# PASO 1: INICIALIZACIÓN Y CONFIGURACIÓN INICIAL
# ============================================================================

# Inicializar todos los módulos de Pygame
pygame.init()

# Definir las dimensiones de la ventana del juego
ANCHO = 800    # Ancho en píxeles
ALTO = 600     # Alto en píxeles

# Crear la ventana del juego
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Cazador de Tesoros")  # Título de la ventana

# Definir colores usando valores RGB (Rojo, Verde, Azul)
BLANCO = (255, 255, 255)  # Color blanco
NEGRO = (0, 0, 0)         # Color negro
VERDE = (0, 255, 0)       # Color verde

# Crear un reloj para controlar la velocidad del juego (FPS)
reloj = pygame.time.Clock()

# ============================================================================
# PASO 2: FUNCIONES DEL JUEGO
# ============================================================================

def cargar_imagenes():
    """
    Función que carga todas las imágenes necesarias para el juego
    
    Returns:
        tuple: Tupla con las imágenes cargadas (fondo, jugador, tesoro)
        
    Conceptos claves:
    - Función con valor de retorno
    - Manejo de excepciones (try/except)
    - Escalado de imágenes
    """
    try:
        # Cargar imagen de fondo y ajustarla al tamaño de pantalla
        fondo = pygame.image.load("fondo_selva.png")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
        
        # Cargar imagen del jugador y ajustarla a 64x64 píxeles
        jugador = pygame.image.load("explorador.png")
        jugador = pygame.transform.scale(jugador, (64, 64))
        
        # Cargar imagen del tesoro y ajustarla a 48x48 píxeles
        tesoro = pygame.image.load("tesoro.png")
        tesoro = pygame.transform.scale(tesoro, (48, 48))
        
        # Retornar todas las imágenes como una tupla
        return fondo, jugador, tesoro
        
    except pygame.error:
        # Si hay error al cargar las imágenes, mostrar mensaje y cerrar
        print("Error: No se pudieron cargar las imágenes")
        print("Asegúrate de tener los archivos: fondo_selva.png, explorador.png, tesoro.png")
        sys.exit()  # Salir del programa

def detectar_colision(rect1, rect2):
    """
    Función que detecta si dos objetos rectangulares se superponen
    
    Args:
        rect1 (pygame.Rect): Primer rectángulo
        rect2 (pygame.Rect): Segundo rectángulo
        
    Returns:
        bool: True si hay colisión, False si no la hay
        
    Conceptos claves:
    - Función con parámetros
    - Función con valor de retorno booleano
    - Detección de colisiones en videojuegos
    """
    return rect1.colliderect(rect2)

def mover_jugador(pos_x, pos_y, teclas):
    """
    Función que mueve al jugador según las teclas presionadas
    
    Args:
        pos_x (int): Posición X actual del jugador
        pos_y (int): Posición Y actual del jugador
        teclas (pygame.key): Estado de las teclas del teclado
        
    Returns:
        tuple: Nueva posición (x, y) del jugador
        
    Conceptos claves:
    - Función con múltiples parámetros
    - Condicionales anidados (if)
    - Operadores lógicos (and)
    - Límites de pantalla
    """
    velocidad = 5  # Píxeles que se mueve por frame
    
    # Mover hacia la izquierda (verificar que no salga de pantalla)
    if teclas[pygame.K_LEFT] and pos_x > 0:
        pos_x -= velocidad
        
    # Mover hacia la derecha (verificar que no salga de pantalla)
    if teclas[pygame.K_RIGHT] and pos_x < ANCHO - 64:
        pos_x += velocidad
        
    # Mover hacia arriba (verificar que no salga de pantalla)
    if teclas[pygame.K_UP] and pos_y > 0:
        pos_y -= velocidad
        
    # Mover hacia abajo (verificar que no salga de pantalla)
    if teclas[pygame.K_DOWN] and pos_y < ALTO - 64:
        pos_y += velocidad
    
    # Retornar las nuevas posiciones
    return pos_x, pos_y

def mostrar_mensaje_victoria(pantalla):
    """
    Función que muestra la pantalla de victoria cuando se encuentra el tesoro
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        
    Conceptos claves:
    - Renderizado de texto
    - Transparencias
    - Centrado de elementos
    - Superposición de capas
    """
    # Crear fuente grande para el mensaje principal
    fuente = pygame.font.Font(None, 74)
    texto = fuente.render("¡TESORO ENCONTRADO!", True, VERDE)
    rect_texto = texto.get_rect(center=(ANCHO//2, ALTO//2))
    
    # Crear un fondo semi-transparente
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(128)  # Transparencia (0=invisible, 255=opaco)
    overlay.fill(NEGRO)
    pantalla.blit(overlay, (0, 0))
    
    # Dibujar el texto principal
    pantalla.blit(texto, rect_texto)
    
    # Crear y dibujar las instrucciones
    fuente_pequena = pygame.font.Font(None, 36)
    instruccion = fuente_pequena.render("Presiona ESPACIO para jugar de nuevo o ESC para salir", True, BLANCO)
    rect_instruccion = instruccion.get_rect(center=(ANCHO//2, ALTO//2 + 60))
    pantalla.blit(instruccion, rect_instruccion)

def reiniciar_juego():
    """
    Función que reinicia las posiciones del jugador y tesoro
    
    Returns:
        tuple: Posiciones iniciales (jugador_x, jugador_y, tesoro_x, tesoro_y)
        
    Conceptos claves:
    - Función de reinicio
    - Valores por defecto
    - Múltiples valores de retorno
    """
    jugador_x = 50   # Posición inicial X del jugador
    jugador_y = 500  # Posición inicial Y del jugador
    tesoro_x = 700   # Posición X del tesoro
    tesoro_y = 350   # Posición Y del tesoro
    
    return jugador_x, jugador_y, tesoro_x, tesoro_y

# ============================================================================
# PASO 3: FUNCIÓN PRINCIPAL DEL JUEGO (GAME LOOP)
# ============================================================================

def main():
    """
    Función principal que contiene el bucle del juego
    
    Conceptos claves:
    - Bucle principal de videojuego (game loop)
    - Estados del juego
    - Manejo de eventos
    - Actualización y renderizado
    """
    
    # --- INICIALIZACIÓN ---
    # Cargar todas las imágenes del juego
    fondo_img, jugador_img, tesoro_img = cargar_imagenes()
    
    # Establecer posiciones iniciales de los objetos
    jugador_x, jugador_y, tesoro_x, tesoro_y = reiniciar_juego()
    
    # Variables de estado del juego
    juego_terminado = False  # ¿Se encontró el tesoro?
    running = True           # ¿El juego sigue ejecutándose?
    
    # Crear fuente para mostrar instrucciones
    fuente = pygame.font.Font(None, 36)
    
    # --- BUCLE PRINCIPAL DEL JUEGO ---
    while running:
        
        # PASO 3.1: MANEJAR EVENTOS (Input del usuario)
        for evento in pygame.event.get():
            # Si el usuario cierra la ventana
            if evento.type == pygame.QUIT:
                running = False
                
            # Si se presiona una tecla
            elif evento.type == pygame.KEYDOWN:
                # Solo procesar estas teclas si el juego terminó
                if juego_terminado:
                    if evento.key == pygame.K_SPACE:
                        # Reiniciar el juego
                        jugador_x, jugador_y, tesoro_x, tesoro_y = reiniciar_juego()
                        juego_terminado = False
                    elif evento.key == pygame.K_ESCAPE:
                        # Salir del juego
                        running = False
        
        # PASO 3.2: ACTUALIZAR LÓGICA DEL JUEGO (Solo si no terminó)
        if not juego_terminado:
            # Obtener el estado actual de todas las teclas
            teclas = pygame.key.get_pressed()
            
            # Mover al jugador según las teclas presionadas
            jugador_x, jugador_y = mover_jugador(jugador_x, jugador_y, teclas)
            
            # Crear rectángulos para la detección de colisiones
            rect_jugador = pygame.Rect(jugador_x, jugador_y, 64, 64)
            rect_tesoro = pygame.Rect(tesoro_x, tesoro_y, 48, 48)
            
            # Verificar si hay colisión entre jugador y tesoro
            if detectar_colision(rect_jugador, rect_tesoro):
                juego_terminado = True  # ¡Victoria!
        
        # PASO 3.3: RENDERIZAR/DIBUJAR TODO EN PANTALLA
        # Dibujar el fondo (siempre primero)
        pantalla.blit(fondo_img, (0, 0))
        
        # Dibujar el jugador en su posición actual
        pantalla.blit(jugador_img, (jugador_x, jugador_y))
        
        # Solo dibujar el tesoro si el juego no ha terminado
        if not juego_terminado:
            pantalla.blit(tesoro_img, (tesoro_x, tesoro_y))
            
            # Mostrar instrucciones en pantalla
            instrucciones = fuente.render("Usa las flechas para mover al explorador", True, BLANCO)
            pantalla.blit(instrucciones, (10, 10))
            
            objetivo = fuente.render("¡Encuentra el tesoro!", True, BLANCO)
            pantalla.blit(objetivo, (10, 50))
        else:
            # Si el juego terminó, mostrar pantalla de victoria
            mostrar_mensaje_victoria(pantalla)
        
        # Actualizar la pantalla para mostrar todos los cambios
        pygame.display.flip()
        
        # Controlar la velocidad del juego (60 FPS)
        reloj.tick(60)
    
    # --- FINALIZACIÓN ---
    # Cerrar Pygame y salir del programa
    pygame.quit()
    sys.exit()

# ============================================================================
# PASO 4: PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

# Esta línea asegura que main() solo se ejecute si este archivo 
# se ejecuta directamente (no si se importa desde otro archivo)
if __name__ == "__main__":
    main()  # Iniciar el juego

"""
CONCEPTOS DE PROGRAMACIÓN DEMOSTRADOS EN ESTE CÓDIGO:
=====================================================

1. FUNCIONES:
   - Definición con 'def'
   - Parámetros y argumentos
   - Valores de retorno
   - Documentación con docstrings

2. CONDICIONALES:
   - if, elif, else
   - Operadores de comparación (>, <, ==)
   - Operadores lógicos (and, or, not)
   - Condicionales anidados

3. VARIABLES Y CONSTANTES:
   - Asignación de variables
   - Constantes en mayúsculas
   - Diferentes tipos de datos (int, bool, tuple)

4. ESTRUCTURAS DE CONTROL:
   - Bucle while
   - Bucle for (en manejo de eventos)
   - Control de flujo con break/continue implícito

5. MANEJO DE ERRORES:
   - try/except para captura de excepciones
   - Validación de entrada

6. MODULARIDAD:
   - Separación en funciones especializadas
   - Reutilización de código
"""