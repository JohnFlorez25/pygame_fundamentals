"""
JUEGO CAZADOR DE TESOROS - VERSIÓN MODULAR
==========================================
Archivo principal que integra todos los módulos del juego.

Conceptos enseñados:
- Arquitectura modular de software
- Importación y uso de módulos personalizados
- Separación de responsabilidades
- Game loop integrado con múltiples sistemas
"""

import pygame
import sys

# Importar todos los módulos del juego
from configuracion import *
import jugador
import enemigo  
import tesoros
import colisiones
import interfaz
import utilidades

# ============================================================================
# INICIALIZACIÓN DEL JUEGO
# ============================================================================

def inicializar_pygame():
    """
    Inicializa Pygame y crea la ventana principal
    
    Returns:
        tuple: (pantalla, reloj) para el juego
        
    Conceptos enseñados:
    - Inicialización centralizada
    - Configuración de ventana
    - Creación de objetos principales
    """
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(TITULO)
    reloj = pygame.time.Clock()
    
    return pantalla, reloj

def cargar_recursos():
    """
    Carga todos los recursos del juego usando el módulo de utilidades
    
    Returns:
        tuple: (imagenes, fuentes) cargadas
        
    Conceptos enseñados:
    - Carga centralizada de recursos
    - Uso de módulos auxiliares
    - Manejo de errores en recursos
    """
    # Verificar que los recursos existan
    if not utilidades.verificar_recursos():
        print("Advertencia: Algunos recursos no están disponibles")
        print("El juego usará placeholders para imágenes faltantes")
    
    # Cargar imágenes
    imagenes = utilidades.cargar_todas_las_imagenes()
    
    # Cargar fuentes
    fuentes = interfaz.inicializar_fuentes()
    
    return imagenes, fuentes

def crear_estado_inicial():
    """
    Crea el estado inicial de todos los elementos del juego
    
    Returns:
        dict: Diccionario con todo el estado del juego
        
    Conceptos enseñados:
    - Inicialización de estado completo
    - Organización de datos del juego
    - Uso coordinado de módulos
    """
    estado = {
        'jugador': jugador.crear_jugador(),
        'enemigo': enemigo.crear_enemigo(),
        'tesoros': tesoros.crear_lista_tesoros(NUMERO_TESOROS),
        'juego_terminado': False,
        'tipo_final': None,  # 'victoria' o 'derrota'
        'running': True,
        'pausa': False
    }
    
    return estado

# ============================================================================
# FUNCIONES DE MANEJO DE EVENTOS
# ============================================================================

def manejar_eventos(estado):
    """
    Procesa todos los eventos de entrada del usuario
    
    Args:
        estado (dict): Estado actual del juego
        
    Conceptos enseñados:
    - Manejo centralizado de eventos
    - Estados diferentes de la aplicación
    - Control de flujo por eventos
    """
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            estado['running'] = False
            
        elif evento.type == pygame.KEYDOWN:
            # Manejar teclas según el estado del juego
            if estado['juego_terminado']:
                manejar_eventos_fin_juego(evento, estado)
            else:
                manejar_eventos_juego_activo(evento, estado)

def manejar_eventos_fin_juego(evento, estado):
    """
    Maneja eventos cuando el juego ha terminado
    
    Args:
        evento (pygame.Event): Evento a procesar
        estado (dict): Estado del juego
        
    Conceptos enseñados:
    - Manejo de eventos por estado
    - Reinicio de juego
    - Navegación entre estados
    """
    if evento.key == pygame.K_SPACE:
        # Reiniciar juego
        reiniciar_juego_completo(estado)
    elif evento.key == pygame.K_ESCAPE:
        # Salir del juego
        estado['running'] = False

def manejar_eventos_juego_activo(evento, estado):
    """
    Maneja eventos durante el juego activo
    
    Args:
        evento (pygame.Event): Evento a procesar  
        estado (dict): Estado del juego
        
    Conceptos enseñados:
    - Eventos durante gameplay
    - Sistema de pausa
    - Controles de desarrollo
    """
    if evento.key == pygame.K_p:
        # Alternar pausa
        estado['pausa'] = not estado['pausa']
    elif evento.key == pygame.K_r:
        # Reinicio rápido (para desarrollo)
        reiniciar_juego_completo(estado)
    elif evento.key == pygame.K_F1:
        # Mostrar estado en consola (debug)
        utilidades.imprimir_estado_juego(
            estado['jugador'], 
            estado['enemigo'], 
            estado['tesoros']
        )

# ============================================================================
# FUNCIONES DE ACTUALIZACIÓN DE LÓGICA
# ============================================================================

def actualizar_juego(estado):
    """
    Actualiza toda la lógica del juego
    
    Args:
        estado (dict): Estado actual del juego
        
    Conceptos enseñados:
    - Actualización coordinada de sistemas
    - Lógica de juego modular
    - Orden de actualización importante
    """
    # No actualizar si está en pausa o terminado
    if estado['pausa'] or estado['juego_terminado']:
        return
    
    # 1. Actualizar movimiento del jugador
    actualizar_movimiento_jugador(estado)
    
    # 2. Actualizar enemigo (IA)
    actualizar_enemigo_completo(estado)
    
    # 3. Procesar colisiones
    procesar_todas_las_colisiones(estado)
    
    # 4. Verificar condiciones de final de juego
    verificar_final_juego(estado)

def actualizar_movimiento_jugador(estado):
    """
    Actualiza el movimiento del jugador basado en input
    
    Args:
        estado (dict): Estado del juego
        
    Conceptos enseñados:
    - Separación de input y lógica
    - Movimiento basado en estado continuo de teclas
    """
    if estado['jugador']['vivo']:
        teclas = pygame.key.get_pressed()
        jugador.mover_jugador(estado['jugador'], teclas)

def actualizar_enemigo_completo(estado):
    """
    Actualiza el comportamiento del enemigo
    
    Args:
        estado (dict): Estado del juego
        
    Conceptos enseñados:
    - Actualización de IA
    - Integración de sistemas de enemigos
    """
    enemigo.actualizar_enemigo(estado['enemigo'], estado['jugador'])

def procesar_todas_las_colisiones(estado):
    """
    Procesa todas las colisiones del juego
    
    Args:
        estado (dict): Estado del juego
        
    Conceptos enseñados:
    - Procesamiento masivo de colisiones
    - Integración de sistemas de colisión
    - Modificación de estado por colisiones
    """
    # Colisiones jugador-tesoros
    colisiones.procesar_colisiones_jugador_tesoros(
        estado['jugador'], 
        estado['tesoros']
    )
    
    # Colisión jugador-enemigo
    if colisiones.procesar_colision_jugador_enemigo(
        estado['jugador'], 
        estado['enemigo']
    ):
        # El jugador fue capturado
        estado['juego_terminado'] = True
        estado['tipo_final'] = 'derrota'

def verificar_final_juego(estado):
    """
    Verifica las condiciones de victoria
    
    Args:
        estado (dict): Estado del juego
        
    Conceptos enseñados:
    - Condiciones de victoria
    - Cambio de estado del juego
    - Lógica de finalización
    """
    if jugador.jugador_ha_ganado(estado['jugador']):
        estado['juego_terminado'] = True
        estado['tipo_final'] = 'victoria'

# ============================================================================
# FUNCIONES DE RENDERIZADO
# ============================================================================

def renderizar_juego(pantalla, imagenes, fuentes, estado):
    """
    Renderiza todos los elementos del juego
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        imagenes (dict): Diccionario con imágenes cargadas
        fuentes (dict): Diccionario con fuentes
        estado (dict): Estado actual del juego
        
    Conceptos enseñados:
    - Renderizado por capas
    - Orden de dibujado importante
    - Renderizado condicional por estado
    """
    # 1. Dibujar fondo
    pantalla.blit(imagenes['fondo'], (0, 0))
    
    # 2. Dibujar tesoros
    tesoros.dibujar_tesoros(pantalla, imagenes['tesoro'], estado['tesoros'])
    
    # 3. Dibujar jugador
    jugador.dibujar_jugador(pantalla, imagenes['jugador'], estado['jugador'])
    
    # 4. Dibujar enemigo
    enemigo.dibujar_enemigo(pantalla, imagenes['enemigo'], estado['enemigo'])
    
    # 5. Dibujar interfaz de usuario
    renderizar_interfaz(pantalla, fuentes, estado)
    
    # 6. Dibujar overlays si es necesario
    renderizar_overlays(pantalla, fuentes, estado)

def renderizar_interfaz(pantalla, fuentes, estado):
    """
    Renderiza elementos de la interfaz de usuario
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Fuentes cargadas
        estado (dict): Estado del juego
        
    Conceptos enseñados:
    - Renderizado de UI modular
    - Elementos de información para el jugador
    """
    if not estado['juego_terminado'] and not estado['pausa']:
        # HUD normal del juego
        interfaz.dibujar_contador_tesoros(
            pantalla, fuentes, estado['jugador'], NUMERO_TESOROS
        )
        
        interfaz.dibujar_instrucciones(pantalla, fuentes, estado['jugador'])
        
        interfaz.dibujar_estado_jugador(pantalla, fuentes, estado['jugador'])
        
        # Opcional: mostrar distancia al enemigo
        interfaz.mostrar_distancia_enemigo(
            pantalla, fuentes, estado['jugador'], estado['enemigo']
        )

def renderizar_overlays(pantalla, fuentes, estado):
    """
    Renderiza overlays y pantallas especiales
    
    Args:
        pantalla (pygame.Surface): Superficie donde dibujar
        fuentes (dict): Fuentes cargadas
        estado (dict): Estado del juego
        
    Conceptos enseñados:
    - Overlays de estado
    - Pantallas de transición
    - Renderizado condicional complejo
    """
    if estado['pausa']:
        interfaz.mostrar_pausa(pantalla, fuentes)
    
    elif estado['juego_terminado']:
        if estado['tipo_final'] == 'victoria':
            interfaz.mostrar_mensaje_victoria(pantalla, fuentes, estado['jugador'])
        elif estado['tipo_final'] == 'derrota':
            interfaz.mostrar_mensaje_derrota(pantalla, fuentes, estado['jugador'])

# ============================================================================
# FUNCIONES DE GESTIÓN DE ESTADO
# ============================================================================

def reiniciar_juego_completo(estado):
    """
    Reinicia completamente el estado del juego
    
    Args:
        estado (dict): Estado del juego a reiniciar
        
    Conceptos enseñados:
    - Reinicio coordinado de todos los sistemas
    - Restablecimiento de estado completo
    - Reutilización de objetos existentes
    """
    # Reiniciar jugador
    jugador.reiniciar_jugador(estado['jugador'])
    
    # Reiniciar enemigo
    enemigo.reiniciar_enemigo(estado['enemigo'])
    
    # Reiniciar tesoros (mantener posiciones, pero hacerlos visibles)
    tesoros.reiniciar_tesoros(estado['tesoros'])
    
    # Reiniciar estado de juego
    estado['juego_terminado'] = False
    estado['tipo_final'] = None
    estado['pausa'] = False

def validar_estado_juego(estado):
    """
    Valida que el estado del juego sea coherente
    
    Args:
        estado (dict): Estado a validar
        
    Returns:
        bool: True si el estado es válido
        
    Conceptos enseñados:
    - Validación de estado complejo
    - Detección de estados inconsistentes
    - Debugging de estado de juego
    """
    # Verificar que existan todas las claves requeridas
    claves_requeridas = ['jugador', 'enemigo', 'tesoros', 'juego_terminado', 'running']
    for clave in claves_requeridas:
        if clave not in estado:
            print(f"Error: Falta clave {clave} en estado del juego")
            return False
    
    # Verificar coherencia de tesoros
    tesoros_recogidos = estado['jugador']['tesoros_recogidos']
    tesoros_visibles = tesoros.contar_tesoros_visibles(estado['tesoros'])
    
    if tesoros_recogidos + tesoros_visibles != NUMERO_TESOROS:
        print("Advertencia: Incoherencia en conteo de tesoros")
    
    return True

# ============================================================================
# FUNCIÓN PRINCIPAL DEL JUEGO
# ============================================================================

def main():
    """
    Función principal que ejecuta el juego completo
    
    Conceptos enseñados:
    - Game loop principal integrado
    - Coordinación de todos los sistemas
    - Manejo de errores a nivel de aplicación
    - Arquitectura modular completa
    """
    try:
        # Validar configuración antes de empezar
        errores_config = utilidades.validar_configuracion()
        if errores_config:
            print("Errores de configuración encontrados:")
            for error in errores_config:
                print(f"- {error}")
            print("Corrige estos errores antes de ejecutar el juego.")
            return
        
        # Inicializar Pygame
        pantalla, reloj = inicializar_pygame()
        
        # Cargar recursos
        imagenes, fuentes = cargar_recursos()
        
        # Crear estado inicial
        estado = crear_estado_inicial()
        
        # Validar estado inicial
        if not validar_estado_juego(estado):
            print("Error en estado inicial del juego")
            return
        
        print("=== CAZADOR DE TESOROS - VERSIÓN MODULAR ===")
        print("Controles:")
        print("- Flechas: Mover explorador")
        print("- P: Pausar/Reanudar")
        print("- R: Reiniciar juego")
        print("- F1: Mostrar estado en consola")
        print("- ESC: Salir (solo en pantalla de fin)")
        print("¡Recoge todos los tesoros y evita al enemigo!")
        print("=" * 45)
        
        # BUCLE PRINCIPAL DEL JUEGO
        while estado['running']:
            # 1. Manejar eventos
            manejar_eventos(estado)
            
            # 2. Actualizar lógica del juego
            actualizar_juego(estado)
            
            # 3. Renderizar todo
            renderizar_juego(pantalla, imagenes, fuentes, estado)
            
            # 4. Actualizar pantalla
            pygame.display.flip()
            
            # 5. Controlar FPS
            reloj.tick(FPS)
        
        print("¡Gracias por jugar Cazador de Tesoros!")
        
    except Exception as e:
        print(f"Error crítico en el juego: {e}")
        print("Verifica que todos los módulos y recursos estén disponibles")
        
    finally:
        # Limpiar y cerrar
        pygame.quit()
        sys.exit()

# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada del programa modular
    
    Conceptos enseñados:
    - Ejecución condicional del programa principal
    - Separación entre código de librería y ejecutable
    """
    main()