import pygame
import random

# Inicializar Pygame
pygame.init()

def configurar_ventana():
    """Configura y retorna la ventana del juego y sus dimensiones"""
    ancho_ventana = 800
    alto_ventana = 600
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("Version 2 - Juego en Pygame")
    return ventana, ancho_ventana, alto_ventana

def mover_jugador(x, y, velocidad, teclas, ancho_ventana, alto_ventana, tamanio):
    """Actualiza la posición del jugador según las teclas presionadas"""
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Mantener al jugador dentro de la ventana
    if x < 0:
        x = 0
    if x > ancho_ventana - tamanio:
        x = ancho_ventana - tamanio
    if y < 0:
        y = 0
    if y > alto_ventana - tamanio:
        y = alto_ventana - tamanio

    return x, y

def mover_obstaculo(obstaculo_x, velocidad, direccion, ancho_ventana, tamanio):
    """Mueve el obstáculo y retorna su nueva posición y dirección"""
    obstaculo_x += velocidad * direccion
    
    if obstaculo_x <= 0 or obstaculo_x >= ancho_ventana - tamanio:
        direccion *= -1
        
    return obstaculo_x, direccion

def hay_colision(x1, y1, tamanio1, x2, y2, tamanio2):
    """Verifica si hay colisión entre dos objetos"""
    return (x1 < x2 + tamanio2 and
            x1 + tamanio1 > x2 and
            y1 < y2 + tamanio2 and
            y1 + tamanio1 > y2)

def generar_posicion_aleatoria(ancho_ventana, alto_ventana, tamanio):
    """Genera una posición aleatoria dentro de la ventana"""
    x = random.randint(0, ancho_ventana - tamanio)
    y = random.randint(0, alto_ventana - tamanio)
    return x, y

def dibujar_rectangulo(ventana, x, y, tamanio, color):
    """Dibuja un rectángulo en la ventana"""
    pygame.draw.rect(ventana, color, (x, y, tamanio, tamanio))

def mostrar_texto(ventana, texto, x, y, color=(255, 255, 255)):
    """Muestra texto en la ventana"""
    fuente = pygame.font.Font(None, 36)
    superficie = fuente.render(texto, True, color)
    ventana.blit(superficie, (x, y))

def main():
    # Configuración inicial
    ventana, ancho_ventana, alto_ventana = configurar_ventana()
    
    # Variables del jugador
    jugador_x = 100
    jugador_y = 100
    jugador_tamanio = 50
    velocidad_normal = 5
    velocidad = velocidad_normal
    vidas = 3
    puntos = 0
    
    # Variables del objetivo
    objetivo_tamanio = 20
    objetivo_x, objetivo_y = generar_posicion_aleatoria(ancho_ventana, alto_ventana, objetivo_tamanio)
    
    # Variables de los obstáculos
    obstaculo_tamanio = 30
    obstaculo1_x, obstaculo1_y = generar_posicion_aleatoria(ancho_ventana, alto_ventana, obstaculo_tamanio)
    obstaculo2_x, obstaculo2_y = generar_posicion_aleatoria(ancho_ventana, alto_ventana, obstaculo_tamanio)
    obstaculo_velocidad = 3
    direccion1 = 1
    direccion2 = -1
    
    # Colores
    COLOR_NEGRO = (0, 0, 0)
    COLOR_ROJO = (255, 0, 0)
    COLOR_VERDE = (0, 255, 0)
    COLOR_AZUL = (0, 0, 255)
    
    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo and vidas > 0:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    velocidad = 10
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_SPACE:
                    velocidad = velocidad_normal

        # Mover jugador
        teclas = pygame.key.get_pressed()
        jugador_x, jugador_y = mover_jugador(jugador_x, jugador_y, velocidad, teclas, 
                                           ancho_ventana, alto_ventana, jugador_tamanio)
        
        # Mover obstáculos
        obstaculo1_x, direccion1 = mover_obstaculo(obstaculo1_x, obstaculo_velocidad, 
                                                  direccion1, ancho_ventana, obstaculo_tamanio)
        obstaculo2_x, direccion2 = mover_obstaculo(obstaculo2_x, obstaculo_velocidad, 
                                                  direccion2, ancho_ventana, obstaculo_tamanio)
            
        # Verificar colisiones con obstáculos
        if hay_colision(jugador_x, jugador_y, jugador_tamanio, 
                       obstaculo1_x, obstaculo1_y, obstaculo_tamanio) or \
           hay_colision(jugador_x, jugador_y, jugador_tamanio, 
                       obstaculo2_x, obstaculo2_y, obstaculo_tamanio):
            vidas -= 1
            jugador_x = 100
            jugador_y = 100

        # Verificar colisión con objetivo
        if hay_colision(jugador_x, jugador_y, jugador_tamanio, 
                       objetivo_x, objetivo_y, objetivo_tamanio):
            puntos += 10
            objetivo_x, objetivo_y = generar_posicion_aleatoria(ancho_ventana, alto_ventana, 
                                                              objetivo_tamanio)
            
            # Aumentar dificultad cada 50 puntos
            if puntos % 50 == 0:
                obstaculo_velocidad += 1

        # Dibujar
        ventana.fill(COLOR_NEGRO)
        dibujar_rectangulo(ventana, jugador_x, jugador_y, jugador_tamanio, COLOR_ROJO)
        dibujar_rectangulo(ventana, objetivo_x, objetivo_y, objetivo_tamanio, COLOR_VERDE)
        dibujar_rectangulo(ventana, obstaculo1_x, obstaculo1_y, obstaculo_tamanio, COLOR_AZUL)
        dibujar_rectangulo(ventana, obstaculo2_x, obstaculo2_y, obstaculo_tamanio, COLOR_AZUL)

        # Mostrar información
        mostrar_texto(ventana, f"Puntos: {puntos}", 10, 10)
        mostrar_texto(ventana, f"Vidas: {vidas}", 10, 50)

        pygame.display.flip()
        reloj.tick(60)

    # Pantalla de fin de juego
    if vidas <= 0:
        ventana.fill(COLOR_NEGRO)
        mostrar_texto(ventana, "¡Juego Terminado!", ancho_ventana//3, alto_ventana//2)
        mostrar_texto(ventana, f"Puntuación final: {puntos}", 
                     ancho_ventana//3, alto_ventana//2 + 50)
        pygame.display.flip()
        pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()