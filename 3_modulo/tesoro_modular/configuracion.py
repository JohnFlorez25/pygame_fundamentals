"""
CONFIGURACIÓN DEL JUEGO - CAZADOR DE TESOROS
===========================================
Este archivo centraliza todas las constantes y configuraciones del juego.

Conceptos enseñados:
- Separación de configuraciones
- Constantes globales
- Organización modular
"""

# ============================================================================
# CONFIGURACIÓN DE PANTALLA
# ============================================================================
ANCHO = 800                    # Ancho de la ventana en píxeles
ALTO = 600                     # Alto de la ventana en píxeles
TITULO = "Cazador de Tesoros - Versión Modular"
FPS = 60                       # Cuadros por segundo

# ============================================================================
# CONFIGURACIÓN DEL GAMEPLAY
# ============================================================================
NUMERO_TESOROS = 5             # Cantidad de tesoros en el mapa
TESOROS_PARA_GANAR = 5         # Tesoros necesarios para ganar
VELOCIDAD_JUGADOR = 5          # Velocidad del explorador
VELOCIDAD_ENEMIGO = 2          # Velocidad del perseguidor (más lento que jugador)

# ============================================================================
# TAMAÑOS DE SPRITES
# ============================================================================
TAMANO_JUGADOR = 64            # Tamaño del explorador (64x64 px)
TAMANO_TESORO = 48             # Tamaño de los tesoros (48x48 px)
TAMANO_ENEMIGO = 56            # Tamaño del enemigo (56x56 px)

# ============================================================================
# COLORES (RGB)
# ============================================================================
BLANCO = (255, 255, 255)       # Color blanco
NEGRO = (0, 0, 0)              # Color negro
VERDE = (0, 255, 0)            # Color verde
AMARILLO = (255, 255, 0)       # Color amarillo
ROJO = (255, 0, 0)             # Color rojo
AZUL = (0, 0, 255)             # Color azul

# ============================================================================
# RUTAS DE ARCHIVOS
# ============================================================================
RUTA_IMAGENES = "imagenes/"                           # Carpeta de imágenes
ARCHIVO_FONDO = RUTA_IMAGENES + "fondo_selva.png"    # Imagen de fondo
ARCHIVO_JUGADOR = RUTA_IMAGENES + "explorador.png"   # Sprite del jugador
ARCHIVO_TESORO = RUTA_IMAGENES + "tesoro.png"        # Sprite del tesoro
ARCHIVO_ENEMIGO = RUTA_IMAGENES + "enemigo.png"      # Sprite del enemigo

# ============================================================================
# POSICIONES INICIALES
# ============================================================================
JUGADOR_X_INICIAL = 50         # Posición X inicial del explorador
JUGADOR_Y_INICIAL = 300        # Posición Y inicial del explorador
ENEMIGO_X_INICIAL = 700        # Posición X inicial del enemigo
ENEMIGO_Y_INICIAL = 100        # Posición Y inicial del enemigo

# ============================================================================
# MARGENES PARA GENERACIÓN ALEATORIA
# ============================================================================
MARGEN_BORDE = 100             # Distancia mínima desde los bordes
MARGEN_TESORO = MARGEN_BORDE + TAMANO_TESORO  # Margen específico para tesoros