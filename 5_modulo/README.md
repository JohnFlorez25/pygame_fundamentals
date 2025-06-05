# Juego Atrapa las Estrellas - Tutorial de Archivos con Pygame

Un juego educativo desarrollado en Python con Pygame que demuestra el manejo de archivos planos mientras te diviertes atrapando estrellas.

## Descripción

Este juego combina entretenimiento con aprendizaje, mostrando cómo integrar el manejo de archivos JSON en una aplicación interactiva. El jugador controla un cuadrado verde que debe atrapar estrellas amarillas que caen desde la parte superior de la pantalla, mientras el sistema guarda automáticamente las puntuaciones en un archivo JSON.

## Características del Juego

### Mecánicas Principales
- **Movimiento del jugador**: Controla un cuadrado verde usando las flechas izquierda y derecha
- **Estrellas en caída**: Las estrellas aparecen cada segundo en posiciones aleatorias
- **Sistema de puntuación**: Cada estrella atrapada otorga 10 puntos
- **Detección de colisiones**: Sistema preciso para detectar cuando el jugador toca una estrella
- **Interfaz en tiempo real**: Las puntuaciones se muestran durante el juego

### Sistema de Archivos
- **Persistencia de datos**: Las puntuaciones se guardan automáticamente en `puntuaciones.json`
- **Ranking histórico**: Mantiene las 5 mejores puntuaciones de todos los tiempos
- **Visualización en vivo**: Muestra las top 3 puntuaciones durante el juego
- **Manejo de errores**: Crea el archivo automáticamente si no existe

## Requisitos del Sistema

### Dependencias
```bash
pip install pygame
```

### Versiones Recomendadas
- Python 3.7+
- Pygame 2.0+

## Estructura de Archivos

```
proyecto/
│
├── juego_estrellas.py      # Archivo principal del juego
├── puntuaciones.json       # Archivo de puntuaciones (se crea automáticamente)
└── README.md              # Este archivo
```

## Instalación y Ejecución

```bash
pip install pygame
```

### Ejecutar el juego
```bash
python juego_estrellas.py
```

## Controles del Juego

| Tecla | Acción |
|-------|--------|
| ← (Flecha Izquierda) | Mover jugador hacia la izquierda |
| → (Flecha Derecha) | Mover jugador hacia la derecha |
| ❌ (Cerrar ventana) | Salir del juego y guardar puntuación |

## Sistema de Puntuaciones

### Formato del Archivo JSON
```json
[
  {
    "nombre": "Jugador",
    "puntuacion": 150,
    "fecha": "2024-06-04 15:30:25"
  },
  {
    "nombre": "Jugador",
    "puntuacion": 120,
    "fecha": "2024-06-04 14:20:10"
  }
]
```

### Características del Sistema
- **Guardado automático**: Se guarda al cerrar el juego
- **Top 5 histórico**: Solo conserva las 5 mejores puntuaciones
- **Ordenamiento**: Las puntuaciones se ordenan de mayor a menor
- **Timestamps**: Cada puntuación incluye fecha y hora
- **Encoding UTF-8**: Soporte completo para caracteres especiales

## Arquitectura del Código

### Clase Principal: `JuegoConArchivos`

#### Métodos de Archivos
```python
def cargar_puntuaciones(self):
    """Carga las puntuaciones desde el archivo JSON"""
    
def guardar_puntuacion(self, nombre, puntuacion):
    """Guarda una nueva puntuación en el archivo JSON"""
```

#### Métodos de Juego
```python
def crear_estrella(self):
    """Crea una nueva estrella en posición aleatoria"""
    
def actualizar_estrellas(self):
    """Actualiza posiciones y detecta colisiones"""
    
def dibujar(self):
    """Renderiza todos los elementos visuales"""
    
def ejecutar(self):
    """Bucle principal del juego"""
```

### Parámetros Configurables

| Parámetro | Valor por Defecto | Descripción |
|-----------|-------------------|-------------|
| `ancho` | 800 | Ancho de la ventana en píxeles |
| `alto` | 600 | Alto de la ventana en píxeles |
| `velocidad_jugador` | 5 | Velocidad de movimiento del jugador |
| `velocidad_estrella` | 3 | Velocidad de caída de las estrellas |
| `puntos_por_estrella` | 10 | Puntos otorgados por cada estrella |
| `intervalo_estrellas` | 1000ms | Tiempo entre aparición de estrellas |

## Elementos Visuales

### Paleta de Colores
- **Fondo**: Negro (0, 0, 0)
- **Jugador**: Verde (0, 255, 0)
- **Estrellas**: Amarillo (255, 255, 0)
- **Texto**: Blanco (255, 255, 255)

### Dimensiones
- **Jugador**: Cuadrado de 30x30 píxeles
- **Estrellas**: Círculos de radio 10 píxeles
- **Zona de colisión**: 30 píxeles de tolerancia

## Personalización

### Modificar Dificultad
```python
# En el método __init__
self.velocidad_estrella = 5  # Estrellas más rápidas
tiempo_entre_estrellas = 500  # Estrellas más frecuentes
```

### Cambiar Puntuaciones
```python
# En el método actualizar_estrellas
self.puntuacion += 20  # Más puntos por estrella
```

### Ajustar Ranking
```python
# En el método guardar_puntuacion
self.mejores_puntuaciones = self.mejores_puntuaciones[:10]  # Top 10
```

## Solución de Problemas

### Error: "No module named 'pygame'"
```bash
pip install pygame
```

### Error: "Permission denied" al guardar archivo
- Verifica permisos de escritura en el directorio
- Ejecuta como administrador si es necesario

### El archivo JSON se corrompe
- El juego recrea automáticamente el archivo
- Elimina `puntuaciones.json` para reset completo

### Rendimiento lento
- Reduce el número de estrellas en pantalla
- Ajusta `self.reloj.tick(30)` para menos FPS

## Conceptos Abordados

### Manejo de Archivos
1. **Lectura segura**: Uso de `try/except` para manejar archivos inexistentes
2. **Escritura JSON**: Serialización de datos complejos
3. **Context managers**: Uso de `with` para manejo automático de recursos
4. **Encoding**: Especificación de UTF-8 para caracteres especiales

### Programación Orientada a Objetos
1. **Encapsulación**: Métodos privados y públicos bien definidos
2. **Organización**: Separación clara de responsabilidades
3. **Estado**: Manejo de variables de instancia

### Algoritmos y Estructuras
1. **Detección de colisiones**: Cálculo de distancias
2. **Ordenamiento**: Algoritmo de ordenamiento de puntuaciones
3. **Listas**: Manipulación dinámica de elementos

## Ejercicios Propuestos

### Nivel Básico
1. Cambia los colores del juego
2. Modifica la velocidad de las estrellas
3. Ajusta el tamaño del jugador

### Nivel Intermedio
1. Añade diferentes tipos de estrellas con puntuaciones distintas
2. Implementa un sistema de vidas
3. Crea power-ups especiales

### Nivel Avanzado
1. Añade un menú principal con opciones
2. Implementa diferentes niveles de dificultad
3. Crea un sistema de logros guardado en archivo
4. Añade efectos sonoros y música

## Extensiones Sugeridas

### Sistema de Configuración
```python
# config.json
{
  "dificultad": "normal",
  "sonido": true,
  "controles": {
    "izquierda": "LEFT",
    "derecha": "RIGHT"
  }
}
```

### Múltiples Jugadores
```python
# jugadores.json
{
  "jugador_actual": "Ana",
  "jugadores": ["Ana", "Carlos", "Luis"]
}
```

### Estadísticas Detalladas
```python
# estadisticas.json
{
  "partidas_jugadas": 25,
  "tiempo_total": 1800,
  "estrellas_atrapadas": 340
}
```