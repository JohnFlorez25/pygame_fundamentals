"""
JUEGO DEL CAZADOR DE TESOROS - VERSIÓN MÚLTIPLES TESOROS
=========================================================
Juego educativo desarrollado en Python con Pygame para enseñar conceptos básicos de programación.
NUEVA CARACTERÍSTICA: Múltiples tesoros y sistema de puntuación

Autor: John Faber Flórez Vasco
Versión: 2.0
Propósito: Demostrar el uso de listas, bucles, funciones y condicionales
"""

import pygame  # Librería para crear videojuegos
import sys     # Librería del sistema para cerrar el programa
import random  # Librería para generar números aleatorios

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
pygame.display.set_caption("Cazador de Tesoros - Múltiples Tesoros")  # Título de la ventana

# Definir colores usando valores RGB (Rojo, Verde, Azul)
BLANCO = (255, 255, 255)  # Color blanco
NEGRO = (0, 0, 0)         # Color negro
VERDE = (0, 255, 0)       # Color verde
AMARILLO = (255, 255, 0)  # Color amarillo para el contador
AZUL = (0, 0, 255)        # Color azul

# Configuración del juego
NUMERO_TESOROS = 5        # Cantidad de tesoros en el juego
TESOROS_PARA_GANAR = 5    # Tesoros necesarios para ganar

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
        
    Conceptos enseñados:
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

def crear_tesoros(cantidad):
    """
    Función que crea una lista de tesoros en posiciones aleatorias
    
    Args:
        cantidad (int): Número de tesoros a crear
        
    Returns:
        list: Lista de diccionarios con información de cada tesoro
        
    Conceptos enseñados:
    - Listas en Python
    - Bucles for con range()
    - Números aleatorios
    - Diccionarios para almacenar datos
    """
    tesoros = []  # Lista vacía para almacenar los tesoros
    
    # Crear cada tesoro con un bucle
    for i in range(cantidad):
        # Generar posición aleatoria (evitando los bordes)
        x = random.randint(100, ANCHO - 148)   # 148 = 100 margen + 48 tamaño tesoro
        y = random.randint(100, ALTO - 148)    # Para que no aparezca muy cerca del borde
        
        # Crear un diccionario con la información del tesoro
        tesoro = {
            'x': x,           # Posición X
            'y': y,           # Posición Y
            'visible': True   # Si el tesoro está visible (no recogido)
        }
        
        # Agregar el tesoro a la lista
        tesoros.append(tesoro)
    
    return tesoros  # Retornar la lista completa

def detectar_colision(rect1, rect2):
    """
    Función que detecta si dos objetos rectangulares se superponen
    
    Args:
        rect1 (pygame.Rect): Primer rectángulo
        rect2 (pygame.Rect): Segundo rectángulo
        
    Returns:
        bool: True si hay colisión, False si no la hay
        
    Conceptos enseñados:
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
        
    Conceptos enseñados:
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

def verificar_colisiones_tesoros(jugador_x, jugador_y, tesoros):
    """
    Función que verifica colisiones entre el jugador y todos los tesoros visibles
    
    Args:
        jugador_x (int): Posición X del jugador
        jugador_y (int): Posición Y del jugador
        tesoros (list): Lista de tesoros
        
    Returns:
        int: Número de tesoros recogidos en este frame
        
    Conceptos enseñados:
    - Bucles for para recorrer listas
    - Modificación de elementos en listas
    - Condicionales dentro de bucles
    - Contador de eventos
    """
    tesoros_recogidos = 0  # Contador de tesoros recogidos en este frame
    
    # Crear el rectángulo del jugador
    rect_jugador = pygame.Rect(jugador_x, jugador_y, 64, 64)
    
    # Revisar cada tesoro en la lista
    for tesoro in tesoros:
        # Solo verificar tesoros que estén visibles
        if tesoro['visible']:
            # Crear rectángulo del tesoro
            rect_tesoro = pygame.Rect(tesoro['x'], tesoro['y'], 48, 48)
            
            # Verificar colisión
            if detectar_colision(rect_jugador, rect_tesoro):
                tesoro['visible'] = False  # Ocultar el tesoro (marcarlo como recogido)
                tesoros_recogidos += 1     # Incrementar contador
    
    return tesoros_recogidos

def contar_tesoros_restantes(tesoros):
    """
    Función que cuenta cuántos tesoros siguen visibles
    
    Args:
        tesoros (list): Lista de tesoros
        
    Returns:
        int: Número de tesoros que siguen visibles
        
    Conceptos enseñados:
    - Bucles for para recorrer listas
    - Condicionales para filtrar elementos
    - Contador acumulativo
    """
    contador = 0  # Inicializar contador
    
    # Revisar cada tesoro
    for tesoro in tesoros:
        if tesoro['visible']:  # Si el tesoro está visible
            contador += 1      # Incrementar contador
    
    return contador

def mostrar_contador(pantalla, tesoros_recogidos, total_tesoros):
    """
    Función que muestra el contador de tesoros en pantalla
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        tesoros_recogidos (int): Número de tesoros recogidos
        total_tesoros (int): Número total de tesoros
        
    Conceptos enseñados:
    - Renderizado de texto
    - Formateo de strings
    - Posicionamiento de elementos UI
    """
    fuente = pygame.font.Font(None, 48)
    
    # Crear el texto del contador
    texto_contador = f"Tesoros: {tesoros_recogidos}/{total_tesoros}"
    superficie_texto = fuente.render(texto_contador, True, AMARILLO)
    
    # Posicionar en la esquina superior derecha
    x = ANCHO - superficie_texto.get_width() - 20
    y = 20
    
    # Dibujar fondo semi-transparente para el contador
    rect_fondo = pygame.Rect(x - 10, y - 5, superficie_texto.get_width() + 20, superficie_texto.get_height() + 10)
    pygame.draw.rect(pantalla, NEGRO, rect_fondo)
    pygame.draw.rect(pantalla, AMARILLO, rect_fondo, 2)  # Borde amarillo
    
    # Dibujar el texto
    pantalla.blit(superficie_texto, (x, y))

def mostrar_mensaje_victoria(pantalla, tesoros_recogidos):
    """
    Función que muestra la pantalla de victoria cuando se recogen todos los tesoros
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        tesoros_recogidos (int): Cantidad de tesoros recogidos
        
    Conceptos enseñados:
    - Renderizado de texto
    - Transparencias
    - Centrado de elementos
    - Superposición de capas
    - Formateo de strings
    """
    # Crear fuente grande para el mensaje principal
    fuente_grande = pygame.font.Font(None, 74)
    fuente_mediana = pygame.font.Font(None, 48)
    fuente_pequena = pygame.font.Font(None, 36)
    
    # Crear un fondo semi-transparente
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(128)  # Transparencia (0=invisible, 255=opaco)
    overlay.fill(NEGRO)
    pantalla.blit(overlay, (0, 0))
    
    # Mensaje principal
    texto_principal = fuente_grande.render("¡MISIÓN COMPLETADA!", True, VERDE)
    rect_principal = texto_principal.get_rect(center=(ANCHO//2, ALTO//2 - 60))
    pantalla.blit(texto_principal, rect_principal)
    
    # Mensaje con puntuación
    mensaje_puntos = f"Has recogido {tesoros_recogidos} tesoros"
    texto_puntos = fuente_mediana.render(mensaje_puntos, True, AMARILLO)
    rect_puntos = texto_puntos.get_rect(center=(ANCHO//2, ALTO//2 - 10))
    pantalla.blit(texto_puntos, rect_puntos)
    
    # Instrucciones
    instruccion = fuente_pequena.render("Presiona ESPACIO para jugar de nuevo o ESC para salir", True, BLANCO)
    rect_instruccion = instruccion.get_rect(center=(ANCHO//2, ALTO//2 + 40))
    pantalla.blit(instruccion, rect_instruccion)

def reiniciar_juego():
    """
    Función que reinicia el estado del juego
    
    Returns:
        tuple: Estado inicial del juego (jugador_x, jugador_y, tesoros, contador)
        
    Conceptos enseñados:
    - Función de reinicio
    - Valores por defecto
    - Múltiples valores de retorno
    - Llamadas a otras funciones
    """
    jugador_x = 50   # Posición inicial X del jugador
    jugador_y = 300  # Posición inicial Y del jugador
    
    # Crear nueva lista de tesoros
    tesoros = crear_tesoros(NUMERO_TESOROS)
    
    # Resetear contador
    tesoros_recogidos = 0
    
    return jugador_x, jugador_y, tesoros, tesoros_recogidos

# ============================================================================
# PASO 3: FUNCIÓN PRINCIPAL DEL JUEGO (GAME LOOP)
# ============================================================================

def main():
    """
    Función principal que contiene el bucle del juego
    
    Conceptos enseñados:
    - Bucle principal de videojuego (game loop)
    - Estados del juego
    - Manejo de eventos
    - Actualización y renderizado
    - Trabajo con listas y contadores
    """
    
    # --- INICIALIZACIÓN ---
    # Cargar todas las imágenes del juego
    fondo_img, jugador_img, tesoro_img = cargar_imagenes()
    
    # Establecer estado inicial del juego
    jugador_x, jugador_y, tesoros, tesoros_recogidos = reiniciar_juego()
    
    # Variables de estado del juego
    juego_terminado = False  # ¿Se recogieron todos los tesoros?
    running = True           # ¿El juego sigue ejecutándose?
    
    # Crear fuentes para mostrar texto
    fuente_instrucciones = pygame.font.Font(None, 28)
    fuente_objetivo = pygame.font.Font(None, 32)
    
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
                        jugador_x, jugador_y, tesoros, tesoros_recogidos = reiniciar_juego()
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
            
            # Verificar colisiones con todos los tesoros
            nuevos_tesoros = verificar_colisiones_tesoros(jugador_x, jugador_y, tesoros)
            tesoros_recogidos += nuevos_tesoros  # Sumar tesoros recogidos
            
            # Verificar condición de victoria
            if tesoros_recogidos >= TESOROS_PARA_GANAR:
                juego_terminado = True  # ¡Victoria!
        
        # PASO 3.3: RENDERIZAR/DIBUJAR TODO EN PANTALLA
        # Dibujar el fondo (siempre primero)
        pantalla.blit(fondo_img, (0, 0))
        
        # Dibujar el jugador en su posición actual
        pantalla.blit(jugador_img, (jugador_x, jugador_y))
        
        if not juego_terminado:
            # Dibujar todos los tesoros que siguen visibles
            for tesoro in tesoros:
                if tesoro['visible']:  # Solo dibujar tesoros visibles
                    pantalla.blit(tesoro_img, (tesoro['x'], tesoro['y']))
            
            # Mostrar contador de tesoros
            mostrar_contador(pantalla, tesoros_recogidos, NUMERO_TESOROS)
            
            # Mostrar instrucciones en pantalla
            instrucciones = fuente_instrucciones.render("Usa las flechas para mover al explorador", True, BLANCO)
            pantalla.blit(instrucciones, (10, 10))
            
            # Mostrar objetivo
            tesoros_restantes = TESOROS_PARA_GANAR - tesoros_recogidos
            if tesoros_restantes > 0:
                objetivo = fuente_objetivo.render(f"¡Recoge {tesoros_restantes} tesoros más!", True, AMARILLO)
            else:
                objetivo = fuente_objetivo.render("¡Recoge el último tesoro!", True, VERDE)
            pantalla.blit(objetivo, (10, 40))
            
        else:
            # Si el juego terminó, mostrar pantalla de victoria
            mostrar_mensaje_victoria(pantalla, tesoros_recogidos)
        
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
NUEVOS CONCEPTOS DE PROGRAMACIÓN DEMOSTRADOS:
============================================

1. LISTAS:
   - Creación de listas vacías: []
   - Agregar elementos: append()
   - Recorrer listas con for
   - Modificar elementos de listas

2. DICCIONARIOS:
   - Crear diccionarios: {'clave': valor}
   - Acceder a valores: dict['clave']
   - Modificar valores: dict['clave'] = nuevo_valor

3. BUCLES FOR:
   - for i in range(n): para repetir n veces
   - for elemento in lista: para recorrer listas
   - Uso de contadores dentro de bucles

4. NÚMEROS ALEATORIOS:
   - import random
   - random.randint(min, max)

5. MANEJO DE ESTADO:
   - Variables que cambian durante el juego
   - Contadores acumulativos
   - Estados booleanos (visible/invisible)

6. FORMATEO DE STRINGS:
   - f"Texto {variable}" (f-strings)
   - Mostrar información dinámica

CONCEPTOS PREVIOS REFORZADOS:
============================
- Funciones con múltiples parámetros y retornos
- Condicionales anidados
- Detección de colisiones
- Renderizado de elementos UI
- Game loop y estados del juego
"""
