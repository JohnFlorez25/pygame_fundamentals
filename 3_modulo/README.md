# Juego Educativo en Pygame - Versión Modular

## 📝 Descripción
Este es un juego educativo desarrollado en Pygame, diseñado para enseñar conceptos básicos de programación y desarrollo de videojuegos. El jugador controla un cuadrado rojo que debe recolectar objetivos mientras evita obstáculos móviles.

## 🆕 Mejoras Implementadas

### 1. Estructura Modular
El código ha sido reorganizado en módulos para mejor organización y mantenimiento:
- `config.py`: Centraliza todas las constantes y configuraciones
- `utilidades.py`: Contiene funciones de uso común
- `jugador.py`: Maneja la lógica del jugador
- `obstaculos.py`: Controla los obstáculos y su movimiento
- `powerups.py`: Sistema de power-ups y bonus
- `main.py`: Integra todos los módulos y ejecuta el juego

### 2. Mecánicas de Juego Mejoradas

#### Control del Jugador
- Movimiento diagonal suavizado usando normalización vectorial
- Soporte para WASD además de flechas direccionales
- Sistema de velocidad variable (normal/boost)

#### Sistema de Obstáculos
- Movimiento en 2D (diagonal) en lugar de solo horizontal
- Cantidad configurable de obstáculos
- Rebote mejorado en los bordes
- Aumento progresivo de velocidad

#### Power-ups
- Sistema de power-ups aleatorios:
  - Velocidad aumentada
  - Inmunidad temporal
  - Puntos dobles
- Probabilidad configurable de aparición

#### Sistema de Progresión
- Niveles basados en puntuación
- Dificultad progresiva
- Multiplicadores de puntuación
- Sistema de vidas mejorado

## 🎮 Características de Pygame Utilizadas

### 1. Sistema de Eventos
```python
for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        corriendo = False
```
- `pygame.event.get()`: Captura todos los eventos del sistema
- `evento.type`: Identifica tipos específicos de eventos

### 2. Control de Input
```python
teclas = pygame.key.get_pressed()
if teclas[pygame.K_SPACE]:
    # Acción al presionar espacio
```
- `pygame.key.get_pressed()`: Estado actual de todas las teclas
- Constantes de teclas (K_SPACE, K_LEFT, etc.)

### 3. Sistema de Renderizado
```python
ventana.fill(COLOR_NEGRO)  # Limpia la pantalla
pygame.draw.rect()  # Dibuja formas geométricas
pygame.display.flip()  # Actualiza la pantalla
```
- Surface principal (ventana)
- Primitivas de dibujo
- Double buffering

### 4. Control de Tiempo
```python
reloj = pygame.time.Clock()
reloj.tick(FPS)  # Mantiene FPS constantes
```
- FPS consistentes
- Temporización precisa
- `pygame.time.get_ticks()` para eventos temporales

### 5. Sistema de Texto
```python
fuente = pygame.font.Font(None, 36)
superficie = fuente.render(texto, True, color)
```
- Renderizado de texto
- Múltiples fuentes
- Anti-aliasing

## 🛠️ Conceptos de Programación Utilizados

### 1. Estructuras de Control
- Bucles while para el game loop
- Bucles for para eventos y colisiones
- Condicionales para lógica del juego

### 2. Funciones
- Funciones puras para cálculos
- Funciones de utilidad reutilizables
- Parámetros y retorno de valores

### 3. Variables y Tipos de Datos
- Números (int, float) para posiciones
- Booleanos para estados
- Tuplas para colores y coordenadas

### 4. Matemáticas Básicas
- Cálculos de colisiones
- Normalización de vectores
- Aleatoriedad controlada

## 🎯 Objetivos Educativos

1. **Fundamentos de Programación**
   - Estructuras de control
   - Funciones y modularidad
   - Variables y tipos de datos

2. **Conceptos de Videojuegos**
   - Game loop
   - Input handling
   - Colisiones
   - Estados de juego

3. **Buenas Prácticas**
   - Código modular
   - Funciones reutilizables
   - Constantes configurables
   - Documentación clara

## 📚 Guía de Uso para Estudiantes

### Ejecutar el Juego
1. Asegurarse de tener Python y Pygame instalados
2. Ejecutar `main.py`
3. Usar flechas o WASD para moverse

### Modificar el Juego
1. Ajustar constantes en `config.py`
2. Modificar comportamientos en módulos específicos
3. Experimentar con nuevas funcionalidades

### Sugerencias de Modificaciones
- Añadir nuevos tipos de power-ups
- Modificar el sistema de puntuación
- Crear nuevos obstáculos
- Implementar efectos de sonido
- Añadir animaciones simples

## 🔍 Notas Técnicas

### Requisitos
- Python 3.x
- Pygame

### Instalación
```bash
pip install pygame
```

### Estructura de Archivos
```
juego/
│
├── main.py           # Archivo principal
├── config.py         # Configuraciones
├── utilidades.py     # Funciones útiles
├── jugador.py        # Lógica del jugador
├── obstaculos.py     # Lógica de obstáculos
└── powerups.py       # Sistema de power-ups
```