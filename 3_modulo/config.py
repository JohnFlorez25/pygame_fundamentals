"""
Módulo de configuración del juego.
Contiene todas las constantes y configuración inicial.
"""

# Configuración de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TITULO_JUEGO = "Aventura Pygame - Versión Modular"
FPS = 60

# Colores RGB
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_ROJO = (255, 0, 0)
COLOR_VERDE = (0, 255, 0)
COLOR_AZUL = (0, 0, 255)
COLOR_AMARILLO = (255, 255, 0)

# Configuración del jugador
JUGADOR_TAMANIO = 50
JUGADOR_X_INICIAL = 100
JUGADOR_Y_INICIAL = 100
JUGADOR_VELOCIDAD_NORMAL = 5
JUGADOR_VELOCIDAD_BOOST = 10
JUGADOR_VIDAS_INICIAL = 3

# Configuración de objetivos
OBJETIVO_TAMANIO = 20
OBJETIVO_VALOR = 10
PUNTOS_PARA_NIVEL = 50

# Configuración de obstáculos
OBSTACULO_TAMANIO = 30
OBSTACULO_VELOCIDAD_INICIAL = 3
OBSTACULO_INCREMENTO_VELOCIDAD = 1
CANTIDAD_OBSTACULOS = 3  # Nuevo: más obstáculos

# Configuración de power-ups
POWERUP_TAMANIO = 25
POWERUP_DURACION = 5000  # 5 segundos en milisegundos
POWERUP_PROBABILIDAD = 20  # % de probabilidad de aparecer al recolectar objetivo
