# === config.py ===
"""
Configuraciones y constantes del juego
"""
# Configuración de la ventana
ANCHO = 800
ALTO = 600
FPS = 60

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Configuración del jugador
NAVE_VELOCIDAD = 5
NAVE_TAMAÑO = (50, 50)

# Configuración de los objetos
ENERGIA_TAMAÑO = (30, 30)
ASTEROIDE_TAMAÑO = (40, 40)
VELOCIDAD_OBJETOS = 3

# Estados del juego
ESTADO_MENU = "menu"
ESTADO_JUGANDO = "jugando"
ESTADO_GAMEOVER = "gameover"