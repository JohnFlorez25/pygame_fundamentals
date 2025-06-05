import pygame
import json
import random
from datetime import datetime

class JuegoConArchivos:
    def __init__(self):
        pygame.init()
        self.ancho = 800
        self.alto = 600
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Juego con Archivos - Atrapa las Estrellas")
        
        # Colores
        self.NEGRO = (0, 0, 0)
        self.BLANCO = (255, 255, 255)
        self.AMARILLO = (255, 255, 0)
        self.VERDE = (0, 255, 0)
        self.ROJO = (255, 0, 0)
        
        # Fuente
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_pequeña = pygame.font.Font(None, 24)
        
        # Jugador
        self.jugador_x = self.ancho // 2
        self.jugador_y = self.alto - 50
        self.velocidad_jugador = 5
        
        # Estrellas
        self.estrellas = []
        self.velocidad_estrella = 3
        
        # Puntuación
        self.puntuacion = 0
        
        # Archivo de puntuaciones
        self.archivo_puntuaciones = 'puntuaciones.json'
        self.mejores_puntuaciones = self.cargar_puntuaciones()
        
        # Control de tiempo
        self.reloj = pygame.time.Clock()
        self.tiempo_ultima_estrella = 0
        
    def cargar_puntuaciones(self):
        """Cargar mejores puntuaciones desde archivo JSON"""
        try:
            with open(self.archivo_puntuaciones, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []
    
    def guardar_puntuacion(self, nombre, puntuacion):
        """Guardar nueva puntuación"""
        nueva_puntuacion = {
            'nombre': nombre,
            'puntuacion': puntuacion,
            'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.mejores_puntuaciones.append(nueva_puntuacion)
        # Ordenar por puntuación descendente y mantener solo top 5
        self.mejores_puntuaciones.sort(key=lambda x: x['puntuacion'], reverse=True)
        self.mejores_puntuaciones = self.mejores_puntuaciones[:5]
        
        with open(self.archivo_puntuaciones, 'w', encoding='utf-8') as archivo:
            json.dump(self.mejores_puntuaciones, archivo, indent=2, ensure_ascii=False)
    
    def crear_estrella(self):
        """Crear nueva estrella en posición aleatoria"""
        x = random.randint(20, self.ancho - 20)
        y = -20
        self.estrellas.append([x, y])
    
    def actualizar_estrellas(self):
        """Actualizar posición de estrellas y detectar colisiones"""
        for estrella in self.estrellas[:]:  # Copia de la lista para modificar durante iteración
            estrella[1] += self.velocidad_estrella
            
            # Eliminar estrellas que salen de pantalla
            if estrella[1] > self.alto:
                self.estrellas.remove(estrella)
            
            # Detectar colisión con jugador
            elif (abs(estrella[0] - self.jugador_x) < 30 and 
                  abs(estrella[1] - self.jugador_y) < 30):
                self.estrellas.remove(estrella)
                self.puntuacion += 10
    
    def dibujar(self):
        """Dibujar todos los elementos del juego"""
        self.pantalla.fill(self.NEGRO)
        
        # Dibujar jugador (rectángulo verde)
        pygame.draw.rect(self.pantalla, self.VERDE, 
                        (self.jugador_x - 15, self.jugador_y - 15, 30, 30))
        
        # Dibujar estrellas
        for estrella in self.estrellas:
            pygame.draw.circle(self.pantalla, self.AMARILLO, 
                             (int(estrella[0]), int(estrella[1])), 10)
        
        # Dibujar puntuación
        texto_puntuacion = self.fuente.render(f"Puntuación: {self.puntuacion}", 
                                            True, self.BLANCO)
        self.pantalla.blit(texto_puntuacion, (10, 10))
        
        # Dibujar mejores puntuaciones
        y_offset = 60
        self.pantalla.blit(self.fuente_pequeña.render("Mejores Puntuaciones:", True, self.BLANCO), 
                          (10, y_offset))
        for i, record in enumerate(self.mejores_puntuaciones[:3]):
            y_offset += 25
            texto = f"{i+1}. {record['nombre']}: {record['puntuacion']}"
            self.pantalla.blit(self.fuente_pequeña.render(texto, True, self.BLANCO), 
                              (10, y_offset))
        
        pygame.display.flip()
    
    def ejecutar(self):
        """Bucle principal del juego"""
        ejecutando = True
        
        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    # Guardar puntuación al salir
                    if self.puntuacion > 0:
                        self.guardar_puntuacion("Jugador", self.puntuacion)
                    ejecutando = False
            
            # Control del jugador
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] and self.jugador_x > 15:
                self.jugador_x -= self.velocidad_jugador
            if teclas[pygame.K_RIGHT] and self.jugador_x < self.ancho - 15:
                self.jugador_x += self.velocidad_jugador
            
            # Crear estrellas periódicamente
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultima_estrella > 1000:  # Cada segundo
                self.crear_estrella()
                self.tiempo_ultima_estrella = tiempo_actual
            
            # Actualizar estrellas
            self.actualizar_estrellas()
            
            # Dibujar todo
            self.dibujar()
            self.reloj.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
     juego = JuegoConArchivos()
     juego.ejecutar()