# Explicación del Código: Juego Básico en Pygame

### 1. **Inicialización de Pygame:**
   - Se importa y se inicializa Pygame con `pygame.init()`. Esto configura todos los módulos de Pygame necesarios para trabajar con gráficos, eventos y sonido.

### 2. **Creación de la ventana:**
   - La ventana de 800x600 píxeles se crea con `pygame.display.set_mode()`. Esto define el tamaño de la ventana en la que se dibujarán los elementos del juego.
   - Se asigna un título a la ventana utilizando `pygame.display.set_caption()`. En este caso, el título es "Primer Juego en Pygame".

### 3. **Variables:**
   - `x` y `y` controlan la posición del rectángulo en la pantalla. Se actualizan a medida que el jugador mueve el rectángulo con las teclas.
   - `velocidad` define cuántos píxeles se mueve el rectángulo con cada pulsación de tecla. Este valor determina la rapidez con la que el rectángulo se desplaza por la ventana.

### 4. **Bucle principal del juego:**
   - El bucle principal del juego continúa ejecutándose mientras la variable `corriendo` sea `True`. 
   - Dentro del bucle:
     - Se procesan los eventos (como el cierre de la ventana).
     - Se actualiza la posición del rectángulo según las teclas presionadas.
     - Se redibuja la pantalla con cada iteración para reflejar los cambios en la posición del rectángulo.

### 5. **Eventos:**
   - Se usa `pygame.event.get()` para obtener los eventos, que son acciones como cerrar la ventana o presionar una tecla.
   - Si se detecta el evento de cierre de la ventana (`pygame.QUIT`), la variable `corriendo` se establece en `False` y se termina el bucle principal del juego.

### 6. **Entrada del usuario:**
   - Las teclas de dirección (`K_LEFT`, `K_RIGHT`, `K_UP`, `K_DOWN`) se utilizan para mover el rectángulo en la pantalla.
   - El estado de las teclas presionadas se obtiene con `pygame.key.get_pressed()`, que devuelve una lista de las teclas que están siendo presionadas en ese momento.

### 7. **Limitación de movimiento:**
   - Se controlan las posiciones `x` y `y` del rectángulo para evitar que se mueva fuera de los límites de la ventana.
   - Si el rectángulo se acerca a los bordes de la ventana, se ajustan las coordenadas para que no se dibuje fuera de la pantalla.

### 8. **Dibujo en pantalla:**
   - Se usa `pygame.draw.rect()` para dibujar un rectángulo en la pantalla. 
   - El rectángulo tiene un color rojo (definido por `color_rectangulo`), y se dibuja en las coordenadas `x` y `y` con un tamaño de 50x50 píxeles.

### 9. **Control de la tasa de refresco:**
   - `pygame.time.Clock().tick(60)` limita la tasa de refresco del juego a 60 fotogramas por segundo (FPS).
   - Esto garantiza que el juego se ejecute a una velocidad constante, sin importar la potencia de la computadora que esté ejecutando el programa.
