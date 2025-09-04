# 🏴‍☠️ Cazador de Tesoros - Juego Educativo en Pygame

## 📋 Descripción del Proyecto

**Cazador de Tesoros** es un videojuego educativo desarrollado en Python usando la librería Pygame.

### 🎯 Objetivo del Juego
Controlar a un explorador que debe encontrar un cofre del tesoro escondido en la selva. Cuando el explorador toca el tesoro, el jugador gana y puede reiniciar para jugar nuevamente.

### 🎓 Propósito Educativo
Este proyecto demuestra de manera práctica:
- Uso de **funciones** como bloques de código reutilizable
- Implementación de **condicionales** para la lógica del juego
- Estructura básica de un **videojuego** (game loop)
- **Manejo de eventos** del usuario
- **Detección de colisiones** entre objetos

---

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.7 o superior
- Pygame 2.0 o superior

### Instalación de Dependencias
```bash
pip install pygame
```

### Archivos Necesarios
Asegúrate de tener estos archivos en la misma carpeta:
- `juego_tesoro.py` - Código principal del juego
- `fondo_selva.png` - Imagen de fondo (800x600 px)
- `explorador.png` - Sprite del jugador (64x64 px)
- `tesoro.png` - Sprite del tesoro (48x48 px)

### Ejecutar el Juego
```bash
python juego_tesoro.py
```

---

## 🎮 Controles del Juego

| Tecla | Acción |
|-------|--------|
| `↑` | Mover explorador hacia arriba |
| `↓` | Mover explorador hacia abajo |
| `←` | Mover explorador hacia la izquierda |
| `→` | Mover explorador hacia la derecha |
| `ESPACIO` | Reiniciar juego (solo en pantalla de victoria) |
| `ESC` | Salir del juego (solo en pantalla de victoria) |
| `❌` | Cerrar ventana para salir |

---

## 🏗️ Arquitectura del Código

### Estructura Principal

```
juego_tesoro.py
├── Importaciones y Configuración
├── Constantes Globales
├── Funciones del Juego
│   ├── cargar_imagenes()
│   ├── detectar_colision()
│   ├── mover_jugador()
│   ├── mostrar_mensaje_victoria()
│   └── reiniciar_juego()
├── Función Principal (main)
│   ├── Inicialización
│   ├── Game Loop
│   │   ├── Manejo de Eventos
│   │   ├── Actualización de Lógica
│   │   └── Renderizado
│   └── Finalización
└── Punto de Entrada
```

### 🔧 Funciones Principales

#### `cargar_imagenes()`
```python
def cargar_imagenes():
    """Carga y escala todas las imágenes del juego"""
```
- **Propósito**: Centralizar la carga de recursos gráficos
- **Conceptos**: Manejo de excepciones, escalado de imágenes
- **Retorna**: Tupla con las imágenes cargadas

#### `detectar_colision(rect1, rect2)`
```python
def detectar_colision(rect1, rect2):
    """Detecta si dos rectángulos se superponen"""
```
- **Propósito**: Verificar cuando el jugador toca el tesoro
- **Conceptos**: Función con parámetros, detección de colisiones
- **Retorna**: Boolean (True si hay colisión)

#### `mover_jugador(pos_x, pos_y, teclas)`
```python
def mover_jugador(pos_x, pos_y, teclas):
    """Mueve al jugador según input del teclado"""
```
- **Propósito**: Actualizar posición del jugador
- **Conceptos**: Condicionales múltiples, límites de pantalla
- **Retorna**: Nueva posición (x, y)

#### `main()`
```python
def main():
    """Función principal con el game loop"""
```
- **Propósito**: Controlar todo el flujo del juego
- **Conceptos**: Bucle principal, estados del juego, renderizado

---

## 🎯 Conceptos de Programación Enseñados

### 1. **Funciones** 🔧
```python
def nombre_funcion(parametros):
    """Documentación de la función"""
    # Código de la función
    return valor
```
- **Definición**: Bloques de código reutilizable
- **Parámetros**: Datos que recibe la función
- **Retorno**: Valor que devuelve la función
- **Documentación**: Descripción del propósito

### 2. **Condicionales** 🤔
```python
# Condicional simple
if condicion:
    # hacer algo

# Condicional múltiple
if condicion1 and condicion2:
    # hacer algo
elif otra_condicion:
    # hacer otra cosa
else:
    # hacer esto por defecto
```
- **if/elif/else**: Toma de decisiones
- **Operadores**: `and`, `or`, `not`, `>`, `<`, `==`
- **Límites**: Verificar que el jugador no salga de pantalla

### 3. **Variables y Constantes** 📊
```python
# Constantes (no cambian)
ANCHO = 800
ALTO = 600

# Variables (pueden cambiar)
jugador_x = 50
juego_terminado = False
```

### 4. **Game Loop (Bucle del Juego)** 🔄
```python
while running:
    # 1. Procesar eventos
    # 2. Actualizar lógica
    # 3. Dibujar en pantalla
```
- **Estructura básica** de cualquier videojuego
- **60 FPS**: 60 actualizaciones por segundo
- **Estados**: El juego puede estar "jugando" o "terminado"

---

## 🎨 Recursos Gráficos

### Especificaciones de Imágenes

| Archivo | Dimensiones | Formato | Descripción |
|---------|-------------|---------|-------------|
| `fondo_selva.png` | 800x600 px | PNG/JPG | Paisaje de selva con árboles y camino |
| `explorador.png` | 64x64 px | PNG/JPG | Personaje con sombrero de aventurero |
| `tesoro.png` | 48x48 px | PNG/JPG | Cofre dorado con monedas brillando |

### Paleta de Colores
- **Fondo**: Verdes naturales (#228B22, #32CD32)
- **Personaje**: Tonos tierra (#8B4513, #F4A460)
- **Tesoro**: Dorados (#FFD700, #FFA500)
- **UI**: Blanco y verde para texto

---

## ⚙️ Configuraciones Técnicas

### Parámetros del Juego
```python
# Ventana
ANCHO = 800          # Ancho en píxeles
ALTO = 600           # Alto en píxeles

# Velocidad
FPS = 60            # Cuadros por segundo
VELOCIDAD = 5       # Píxeles por movimiento

# Tamaños de sprites
JUGADOR_SIZE = 64   # 64x64 píxeles
TESORO_SIZE = 48    # 48x48 píxeles
```

### Sistema de Coordenadas
- **Origen (0,0)**: Esquina superior izquierda
- **Eje X**: Aumenta hacia la derecha
- **Eje Y**: Aumenta hacia abajo
- **Límites**: Jugador no puede salir de pantalla

### Detección de Colisiones
```python
# Se crean rectángulos para cada sprite
rect_jugador = pygame.Rect(x, y, ancho, alto)
rect_tesoro = pygame.Rect(x, y, ancho, alto)

# Se verifica superposición
if rect_jugador.colliderect(rect_tesoro):
    # ¡Colisión detectada!
```

---

## 🐛 Manejo de Errores

### Errores Comunes y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `pygame.error: No such file` | Imágenes no encontradas | Verificar nombres y ubicación de archivos |
| `ModuleNotFoundError: pygame` | Pygame no instalado | Ejecutar `pip install pygame` |
| `Surface size is 0` | Imagen corrupta o vacía | Verificar integridad de los archivos PNG/JPG |

### Sistema de Excepciones
```python
try:
    # Cargar imagen
    imagen = pygame.image.load("archivo.png")
except pygame.error:
    # Mostrar error y salir graciosamente
    print("Error: No se pudo cargar la imagen")
    sys.exit()
```

---

## 📚 Ejercicios Propuestos para Estudiantes

### Nivel Básico 🟢
1. **Cambiar velocidad**: Modificar la velocidad del explorador
2. **Nuevos colores**: Cambiar los colores de los mensajes
3. **Posición inicial**: Cambiar dónde aparece el explorador
4. **Tamaño de ventana**: Modificar las dimensiones del juego

### Nivel Intermedio 🟡
1. **Múltiples tesoros**: Agregar más tesoros para recoger
2. **Contador**: Mostrar cuántos tesoros se han encontrado
3. **Tiempo límite**: Agregar un cronómetro
4. **Obstáculos**: Crear objetos que impidan el movimiento

### Nivel Avanzado 🔴
1. **Enemigos**: Agregar personajes que persigan al jugador
2. **Niveles**: Crear múltiples pantallas de juego
3. **Puntuación**: Sistema de puntos y high scores
4. **Sonidos**: Agregar efectos sonoros con pygame.mixer

---

## 🤝 Contribuciones y Extensiones

### Ideas para Mejorar el Juego
- **Animaciones**: Sprites animados para el personaje
- **Música de fondo**: Ambiente sonoro inmersivo
- **Partículas**: Efectos visuales cuando se encuentra el tesoro
- **Menú principal**: Pantalla de inicio con opciones
- **Guardado**: Sistema para guardar puntuaciones

### Estructura para Nuevas Funciones
```python
def nueva_funcion(parametros):
    """
    Descripción de qué hace la función
    
    Args:
        parametro1 (tipo): Descripción
        
    Returns:
        tipo: Descripción del valor retornado
        
    Conceptos enseñados:
    - Concepto 1
    - Concepto 2
    """
    # Código aquí
    return resultado
```

---

## 📖 Recursos Adicionales

### Documentación Oficial
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)

### Tutoriales Recomendados
- [Real Python - Pygame Tutorial](https://realpython.com/pygame-a-primer/)
- [Pygame Tutorials - Game Development](https://www.pygame.org/wiki/tutorials)

### Libros Sugeridos
- "Making Games with Python & Pygame" - Al Sweigart
- "Python Crash Course" - Eric Matthes