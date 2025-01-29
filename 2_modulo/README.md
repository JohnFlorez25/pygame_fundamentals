# Explicación del Juego en Pygame

## Descripción General
Este juego es una aplicación simple desarrollada con Pygame donde el jugador controla un cuadrado rojo que debe recolectar objetivos (cuadrados verdes) mientras evita obstáculos móviles (cuadrados azules).

## Estructura del Código

### 1. Configuración Inicial
```python
def configurar_ventana():
    ancho_ventana = 800
    alto_ventana = 600
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
```
Esta función establece la ventana del juego con dimensiones de 800x600 píxeles.

### 2. Mecánicas Principales

#### Control del Jugador
El jugador se controla con las siguientes mecánicas:
- Flechas de dirección para mover el cuadrado
- Barra espaciadora para un impulso de velocidad temporal
- El jugador no puede salir de los límites de la ventana

```python
def mover_jugador(x, y, velocidad, teclas, ancho_ventana, alto_ventana, tamanio):
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
```

#### Sistema de Obstáculos
Los obstáculos tienen las siguientes características:
- Se mueven horizontalmente de forma automática
- Rebotan en los bordes de la pantalla
- Al chocar con ellos, el jugador pierde una vida

```python
def mover_obstaculo(obstaculo_x, velocidad, direccion, ancho_ventana, tamanio):
    obstaculo_x += velocidad * direccion
    if obstaculo_x <= 0 or obstaculo_x >= ancho_ventana - tamanio:
        direccion *= -1
```

#### Sistema de Puntuación
El sistema de puntuación funciona así:
- Cada objetivo recolectado vale 10 puntos
- Cada 50 puntos, la velocidad de los obstáculos aumenta
- El juego termina cuando el jugador pierde todas sus vidas

### 3. Funciones Auxiliares

#### Detección de Colisiones
```python
def hay_colision(x1, y1, tamanio1, x2, y2, tamanio2):
    return (x1 < x2 + tamanio2 and
            x1 + tamanio1 > x2 and
            y1 < y2 + tamanio2 and
            y1 + tamanio1 > y2)
```
Esta función verifica si dos objetos están en contacto comparando sus posiciones y tamaños.

#### Generación de Posiciones Aleatorias
```python
def generar_posicion_aleatoria(ancho_ventana, alto_ventana, tamanio):
    x = random.randint(0, ancho_ventana - tamanio)
    y = random.randint(0, alto_ventana - tamanio)
```
Se usa para colocar objetivos y obstáculos en posiciones aleatorias dentro de la ventana.

### 4. Variables Principales

#### Variables del Jugador
- `jugador_x, jugador_y`: Posición del jugador
- `velocidad`: Velocidad de movimiento
- `vidas`: Número de vidas restantes
- `puntos`: Puntuación actual

#### Variables de Obstáculos
- `obstaculo_x, obstaculo_y`: Posición de cada obstáculo
- `obstaculo_velocidad`: Velocidad de movimiento
- `direccion`: Dirección del movimiento (1 o -1)

#### Variables del Objetivo
- `objetivo_x, objetivo_y`: Posición del objetivo actual
- `objetivo_tamanio`: Tamaño del objetivo

### 5. Bucle Principal del Juego

El bucle principal del juego realiza las siguientes operaciones en cada frame:

1. Procesa los eventos (teclas presionadas, cierre de ventana)
2. Actualiza las posiciones de los objetos
3. Verifica colisiones
4. Actualiza la puntuación y las vidas
5. Dibuja todos los elementos en la pantalla
6. Actualiza la pantalla

### 6. Sistema de Dificultad Progresiva

El juego se vuelve más difícil de la siguiente manera:
- La velocidad de los obstáculos aumenta cada 50 puntos
- Los obstáculos se mueven de forma independiente en direcciones opuestas
- El jugador debe gestionar múltiples amenazas simultáneamente

### 7. Interfaz de Usuario

La interfaz muestra:
- Puntuación actual
- Vidas restantes
- Pantalla de fin de juego cuando se pierden todas las vidas

## Consejos para Jugar

1. **Movimiento Estratégico**:
   - Usa la barra espaciadora para movimientos rápidos cuando sea necesario
   - Planifica tu ruta considerando el movimiento de los obstáculos

2. **Gestión de Riesgos**:
   - Evita quedar atrapado entre obstáculos
   - Prioriza la supervivencia sobre la recolección de puntos cuando la velocidad sea alta

3. **Puntuación Alta**:
   - Intenta recolectar objetivos de manera eficiente
   - Usa los bordes de la pantalla como zonas seguras
   - Aprende los patrones de movimiento de los obstáculos