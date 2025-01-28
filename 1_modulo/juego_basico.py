# Importar la librería pygame que nos permite crear juegos y trabajar con gráficos, sonidos y eventos
import pygame

# Inicializar todos los módulos necesarios de Pygame
pygame.init()

# Definir las dimensiones de la ventana en píxeles
ancho_ventana = 800
alto_ventana = 600

# Crear la ventana del juego con el tamaño definido previamente
# pygame.display.set_mode() recibe una tupla con las dimensiones de la ventana
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))

# Establecer un título para la ventana
pygame.display.set_caption("Primer Juego en Pygame")

# Definir los colores a utilizar en el juego en formato RGB (Red, Green, Blue)
color_fondo = (0, 0, 0)  # Color de fondo negro (R=0, G=0, B=0)
color_rectangulo = (255, 0, 0)  # Color del rectángulo rojo (R=255, G=0, B=0)

# Inicializar las variables de posición y velocidad del rectángulo
# Estas variables controlan la ubicación y el movimiento del rectángulo en la ventana
x = 100  # Posición inicial en el eje X
y = 100  # Posición inicial en el eje Y
velocidad = 5  # Velocidad de movimiento del rectángulo en píxeles por cuadro

# Iniciar el bucle principal del juego. El juego continuará ejecutándose mientras la variable 'corriendo' sea True.
corriendo = True
while corriendo:
    # Procesar los eventos del juego
    # pygame.event.get() obtiene todos los eventos generados, como pulsaciones de teclas o clics del ratón
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Si el evento es el cierre de la ventana
            corriendo = False  # Detener el bucle y salir del juego

    # Obtener el estado de todas las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Comprobar las teclas de dirección (flechas) para mover el rectángulo
    if teclas[pygame.K_LEFT]:  # Si la flecha izquierda es presionada
        x -= velocidad  # Mover el rectángulo hacia la izquierda
    if teclas[pygame.K_RIGHT]:  # Si la flecha derecha es presionada
        x += velocidad  # Mover el rectángulo hacia la derecha
    if teclas[pygame.K_UP]:  # Si la flecha hacia arriba es presionada
        y -= velocidad  # Mover el rectángulo hacia arriba
    if teclas[pygame.K_DOWN]:  # Si la flecha hacia abajo es presionada
        y += velocidad  # Mover el rectángulo hacia abajo

    # Evitar que el rectángulo se salga de los límites de la ventana
    # Se utilizan condicionales para asegurar que el rectángulo se mantenga dentro de la ventana
    if x < 0:  # Si el rectángulo se sale por el borde izquierdo
        x = 0  # Colocarlo en el borde izquierdo
    elif x > ancho_ventana - 50:  # Si el rectángulo se sale por el borde derecho (tamaño de 50 píxeles)
        x = ancho_ventana - 50  # Colocarlo en el borde derecho
    if y < 0:  # Si el rectángulo se sale por el borde superior
        y = 0  # Colocarlo en el borde superior
    elif y > alto_ventana - 50:  # Si el rectángulo se sale por el borde inferior
        y = alto_ventana - 50  # Colocarlo en el borde inferior

    # Rellenar la ventana con el color de fondo antes de dibujar el rectángulo
    ventana.fill(color_fondo)

    # Dibujar el rectángulo rojo en las coordenadas (x, y) con un tamaño de 50x50 píxeles
    pygame.draw.rect(ventana, color_rectangulo, (x, y, 50, 50))

    # Actualizar la pantalla para reflejar los cambios realizados (dibujar el rectángulo en la nueva posición)
    pygame.display.flip()

    # Controlar la tasa de refresco del juego
    # pygame.time.Clock().tick(60) establece que el juego se ejecutará a 60 fotogramas por segundo (FPS)
    pygame.time.Clock().tick(60)

# Finalizar Pygame cuando se termine el bucle del juego
pygame.quit()
