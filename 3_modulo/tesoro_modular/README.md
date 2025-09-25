# Cazador de Tesoros - Versión Modular

## Estructura del Proyecto

Esta versión modular del juego aplica los principios de **divide y vencerás** y **responsabilidad única**, organizando el código en múltiples archivos especializados.

```
proyecto_tesoro_modular/
├── main.py                # Archivo principal y game loop
├── configuracion.py       # Constantes y configuraciones
├── jugador.py             # Gestión del explorador
├── enemigo.py             # IA del perseguidor
├── tesoros.py             # Sistema de tesoros
├── colisiones.py          # Detección de colisiones
├── interfaz.py            # Sistema de UI
├── utilidades.py          # Funciones auxiliares
└── imagenes/              # Recursos gráficos
    ├── fondo_selva.png
    ├── explorador.png
    ├── tesoro.png
    └── enemigo.png       
```

## Nuevas Características

### **Enemigo Perseguidor**
- **Sprite único**: Personaje oscuro con ojos rojos brillantes
- **IA básica**: Persigue al jugador automáticamente
- **Velocidad controlada**: Más lento que el jugador (estrategia posible)
- **Condición de derrota**: Si te atrapa, pierdes el juego

### **Arquitectura Modular**
- **8 módulos especializados** cada uno con responsabilidad única
- **Código organizado** por funcionalidad
- **Fácil mantenimiento** y extensión
- **Conceptos escalables** para proyectos más grandes

## Conceptos de Programación Enseñados

### **1. Modularización** 
```python
# Cada módulo tiene responsabilidad específica
import jugador          # Todo sobre el explorador
import enemigo          # Todo sobre el perseguidor  
import tesoros          # Gestión de múltiples tesoros
import colisiones       # Sistema centralizado de colisiones
```

### **2. Separación de Responsabilidades** 
- **configuracion.py**: Solo constantes y configuraciones
- **jugador.py**: Solo funciones del explorador
- **enemigo.py**: Solo lógica del perseguidor
- **colisiones.py**: Solo detección de impactos
- **interfaz.py**: Solo elementos visuales de UI

### **3. Importación de Módulos** 
```python
# Importación específica
from configuracion import ANCHO, ALTO, FPS

# Importación de módulo completo
import jugador

# Uso de funciones del módulo
estado_jugador = jugador.crear_jugador()
jugador.mover_jugador(estado_jugador, teclas)
```

### **4. Coordinación de Sistemas** 
```python
def actualizar_juego(estado):
    # Orden de actualización importante
    actualizar_movimiento_jugador(estado)    # 1º
    actualizar_enemigo_completo(estado)      # 2º
    procesar_todas_las_colisiones(estado)   # 3º
    verificar_final_juego(estado)            # 4º
```

## Guía de Cada Módulo

### **configuracion.py** 
**Responsabilidad**: Centralizar todas las constantes del juego.

**Conceptos clave**:
- Constantes globales
- Configuración centralizada
- Separación de valores configurables

**Funciones principales**: Solo constantes (sin funciones)

---

### **jugador.py** 
**Responsabilidad**: Todo lo relacionado con el explorador.

**Conceptos clave**:
- Estado del jugador como diccionario
- Funciones de movimiento con validación de límites
- Manejo de estado de vida/muerte
- Contadores de progreso

**Funciones principales**:
```python
crear_jugador()              # Inicialización
mover_jugador()             # Movimiento con teclas
obtener_rect_jugador()      # Para colisiones
agregar_tesoro_jugador()    # Incrementar contador
jugador_ha_ganado()         # Condición de victoria
```

---

### **enemigo.py**
**Responsabilidad**: IA y comportamiento del perseguidor.

**Conceptos clave**:
- Inteligencia artificial básica
- Algoritmo de persecución simple
- Cálculo de distancias
- Movimiento automático hacia objetivo

**Funciones principales**:
```python
crear_enemigo()             # Inicialización del enemigo
actualizar_enemigo()        # IA de persecución
mover_hacia_objetivo()      # Algoritmo de movimiento
calcular_distancia()        # Matemática básica
```

---

### **tesoros.py**
**Responsabilidad**: Generación y gestión de múltiples tesoros.

**Conceptos clave**:
- Generación procedural básica
- Posicionamiento aleatorio con validación
- Gestión de colecciones de objetos
- Estados de objetos (visible/recogido)

**Funciones principales**:
```python
crear_lista_tesoros()       # Generación aleatoria
verificar_distancia_minima() # Evitar solapamiento
contar_tesoros_visibles()   # Estadísticas
recoger_tesoro()            # Cambio de estado
```

---

### **colisiones.py**
**Responsabilidad**: Detección centralizada de todas las colisiones.

**Conceptos clave**:
- Sistema centralizado de colisiones
- Diferentes tipos de colisión
- Procesamiento masivo de interacciones
- Funciones especializadas por tipo de objeto

**Funciones principales**:
```python
detectar_colision_rectangulos()        # Básica
procesar_colisiones_jugador_tesoros()  # Múltiples objetos
procesar_colision_jugador_enemigo()    # Detección de derrota
obtener_lado_colision()                # Análisis detallado
```

---

### **interfaz.py**
**Responsabilidad**: Toda la interfaz de usuario y elementos visuales.

**Conceptos clave**:
- Renderizado de texto dinámico
- Overlays y pantallas de estado
- HUD (Heads-Up Display)
- Feedback visual inmediato

**Funciones principales**:
```python
inicializar_fuentes()           # Carga de fuentes
dibujar_contador_tesoros()      # HUD principal
mostrar_mensaje_victoria()      # Pantalla de fin
mostrar_mensaje_derrota()       # Pantalla de pérdida
```

---

### **utilidades.py**
**Responsabilidad**: Funciones auxiliares y herramientas generales.

**Conceptos clave**:
- Carga centralizada de recursos
- Funciones matemáticas básicas
- Validación y verificación
- Herramientas de debug

**Funciones principales**:
```python
cargar_todas_las_imagenes()    # Carga masiva de recursos
validar_configuracion()        # Verificación de coherencia
crear_temporizador()           # Utilidades de tiempo
verificar_recursos()           # Debug de archivos
```

---

### **main.py**
**Responsabilidad**: Coordinación general y game loop principal.

**Conceptos clave**:
- Game loop integrado
- Coordinación de sistemas
- Manejo de estados de aplicación
- Integración modular

**Funciones principales**:
```python
main()                    # Función principal
actualizar_juego()        # Lógica coordinada
renderizar_juego()        # Renderizado por capas
manejar_eventos()         # Input del usuario
```

## Controles del Juego

| Tecla | Acción |
|-------|--------|
| `↑` `↓` `←` `→` | Mover explorador |
| `P` | Pausar/Reanudar juego |
| `R` | Reiniciar juego rápido |
| `F1` | Mostrar estado en consola (debug) |
| `ESPACIO` | Reiniciar (solo en fin de juego) |
| `ESC` | Salir (solo en fin de juego) |

##  Instalación y Ejecución

### 1. Preparar el Entorno
```bash
# Instalar pygame
pip install pygame

# Crear carpeta del proyecto
mkdir cazador_tesoros_modular
cd cazador_tesoros_modular
```

### 2. Organizar Archivos
```
Copiar todos los archivos .py a la carpeta principal
Crear carpeta "imagenes/"
Colocar todos los sprites en "imagenes/"
```

### 3. Ejecutar el Juego
```bash
python main.py
```

## 🔧 Configuración del Juego

Edita `configuracion.py` para modificar:

```python
# Gameplay
NUMERO_TESOROS = 5          # Cantidad de tesoros
TESOROS_PARA_GANAR = 5      # Tesoros necesarios para ganar
VELOCIDAD_JUGADOR = 5       # Velocidad del explorador
VELOCIDAD_ENEMIGO = 2       # Velocidad del perseguidor

# Pantalla
ANCHO = 800                 # Ancho de ventana
ALTO = 600                  # Alto de ventana
FPS = 60                    # Cuadros por segundo
```


## Comparación: Monolítico vs Modular

| Aspecto | Versión Monolítica | Versión Modular |
|---------|-------------------|-----------------|
| **Archivos** | 1 archivo grande | 8 archivos especializados |
| **Líneas por archivo** | ~400 líneas | ~100-150 líneas cada uno |
| **Navegación** | Buscar en archivo largo | Ir directamente al módulo |
| **Modificación** | Riesgo de romper otras partes | Cambios aislados |
| **Colaboración** | Difícil trabajo en paralelo | Múltiples personas pueden trabajar |
| **Testing** | Probar todo junto | Probar módulos independientemente |
| **Reutilización** | Copiar funciones manualmente | Importar módulos completos |

### Para Desarrolladores:
```python
# En cualquier módulo, agregar debug:
from utilidades import imprimir_estado_juego

# Usar en puntos clave:
imprimir_estado_juego(jugador, enemigo, tesoros)
```

## Ejercicios de Extensión

### **Nivel Básico** 
1. **Modificar configuración**: Cambiar velocidades, colores, tamaños
2. **Nuevo tipo de tesoro**: Crear tesoros que valgan más puntos
3. **Sonidos**: Agregar efectos sonoros usando pygame.mixer
4. **Animaciones básicas**: Hacer que los sprites se muevan suavemente

### **Nivel Intermedio** 
1. **Nuevo módulo**: Crear `sonidos.py` para efectos de audio
2. **Múltiples enemigos**: Extender el sistema para varios perseguidores
3. **Power-ups**: Crear objetos que den habilidades temporales
4. **Niveles**: Sistema de múltiples pantallas de juego

### **Nivel Avanzado**
1. **Sistema de partículas**: Módulo para efectos visuales
2. **IA avanzada**: Enemigos con diferentes comportamientos
3. **Guardado de datos**: Módulo para high scores y progreso
4. **Red multijugador**: Sistema para múltiples jugadores

## Recursos de Aprendizaje

### Conceptos de Programación Cubiertos:
- **Modularización** y arquitectura de software
- **Importación** de módulos personalizados
- **Separación de responsabilidades**
- **Coordinación de sistemas**
- **Estados de aplicación** complejos
- **IA básica** y algoritmos de persecución
- **Gestión de recursos** centralizada
- **Debugging** y herramientas de desarrollo
