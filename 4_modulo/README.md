# 🚀 Juego Espacial en Python

## Un Juego Educativo usando POO y Pygame

## 📖 Descripción del Proyecto

Este juego espacial es un proyecto educativo desarrollado en Python que demuestra los conceptos fundamentales de la Programación Orientada a Objetos (POO) y el uso de diferentes estructuras de datos. El jugador controla una nave espacial que debe recolectar energía mientras evita asteroides peligrosos, todo esto en un entorno espacial dinámico.

## 🎮 Mecánicas del Juego

En este juego, asumes el control de una nave espacial con las siguientes características:

- **Control de la Nave**: Usa las flechas direccionales para moverte
- **Recolección de Energía**: Captura los orbes azules para ganar puntos y energía
- **Evasión**: Evita los asteroides rojos que drenan tu energía y vidas
- **Sistema de Vidas**: Comienzas con 3 vidas
- **Puntuación**: Acumula puntos recolectando energía
- **Estados del Juego**: Menú principal, jugando y game over

## 🛠️ Estructura del Proyecto

```
space_game/
│
├── config.py           # Configuraciones globales
│
├── entidades/
│   ├── __init__.py
│   ├── jugador.py     # Clase de la nave espacial
│   └── objetos.py     # Clases de energía y asteroides
│
├── utilidades/
│   ├── __init__.py
│   ├── scoring.py     # Sistema de puntuación
│   └── colisiones.py  # Detección de colisiones
│
└── main.py            # Archivo principal del juego
```

## 🔧 Requisitos Técnicos

Para ejecutar el juego necesitas:

1. Python 3.8 o superior
2. Pygame instalado (`pip install pygame`)
3. Sistema operativo compatible (Windows/Linux/MacOS)
4. Ejecuta el juego:
   ```bash
   python main.py
   ```

## 🎯 Características Técnicas Principales

### Sistema de Clases

1. **Clase Jugador**
   ```python
   class Jugador(pygame.sprite.Sprite):
       """
       Maneja la nave del jugador y sus atributos:
       - Posición y movimiento
       - Energía y vidas
       - Puntuación
       """
   ```

2. **Clases de Objetos**
   ```python
   class Energia(pygame.sprite.Sprite):
       """
       Representa los orbes de energía recolectables:
       - Movimiento automático
       - Valor aleatorio
       - Reposicionamiento
       """

   class Asteroide(pygame.sprite.Sprite):
       """
       Representa los obstáculos:
       - Velocidad variable
       - Daño al jugador
       - Reposicionamiento automático
       """
   ```

### Estructuras de Datos Utilizadas

1. **Listas y Grupos de Sprites**
   ```python
   self.todos_sprites = pygame.sprite.Group()
   self.energias = pygame.sprite.Group()
   self.asteroides = pygame.sprite.Group()
   ```

2. **Tuplas para Constantes**
   ```python
   NAVE_TAMAÑO = (50, 50)
   COLOR_BLANCO = (255, 255, 255)
   ```

3. **Diccionarios para Estados**
   ```python
   self.records = {
       "jugador1": 1000,
       "jugador2": 850
   }
   ```

## 🎓 Conceptos de POO Implementados

### 1. Herencia
La mayoría de las entidades del juego heredan de `pygame.sprite.Sprite`, aprovechando la funcionalidad base de Pygame:

```python
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Herencia de Sprite
```

### 2. Encapsulamiento
Uso de atributos privados y métodos de acceso:

```python
class SistemaScore:
    def __init__(self):
        self.__high_scores = []  # Atributo privado
    
    def obtener_mejores_puntuaciones(self):
        return self.__high_scores.copy()  # Acceso controlado
```

### 3. Polimorfismo
Diferentes objetos responden de manera única a métodos comunes:

```python
def update(self):  # Método presente en todas las entidades
    # Cada clase lo implementa de forma diferente
    pass
```

## 🔍 Detalles de Implementación Importantes

### Control del Juego Principal

```python
class Juego:
    def ejecutar(self):
        """
        Bucle principal del juego que maneja:
        1. Procesamiento de eventos
        2. Actualización de estado
        3. Renderizado
        4. Control de FPS
        """
```

### Sistema de Colisiones

```python
def verificar_colisiones(jugador, grupo_energia, grupo_asteroides):
    """
    Sistema de detección de colisiones que:
    - Usa el sistema de sprites de Pygame
    - Maneja múltiples tipos de colisiones
    - Actualiza el estado del juego
    """
```

## 🐛 Solución de Problemas Comunes

1. **Control de FPS**
   ```python
   self.reloj.tick(FPS)  # Mantiene FPS consistente
   ```

2. **Manejo de Memoria**
   ```python
   # Limpieza de sprites fuera de pantalla
   if self.rect.top > ALTO:
       self.kill()  # Elimina el sprite
   ```

3. **Detección de Errores**
   ```python
   try:
       # Operaciones del juego
   except Exception as e:
       print(f"Error: {e}")
       # Manejo de recuperación
   ```

## 📚 Referencias y Recursos

1. **Documentación de Pygame**: https://www.pygame.org/docs/
2. **Tutorial de Sprites**: https://pygame.org/docs/ref/sprite.html
3. **Guía de Colisiones**: https://pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollide