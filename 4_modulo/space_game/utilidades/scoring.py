# === utilidades/scoring.py ===
"""
Gestión de puntuaciones y records
"""
class SistemaScore:
    def __init__(self):
        self.high_scores = []
        self.current_score = 0
        self.records = {}
        
    def agregar_puntos(self, cantidad):
        self.current_score += cantidad
        
    def actualizar_records(self, nombre):
        self.records[nombre] = max(self.records.get(nombre, 0), self.current_score)
        self.high_scores.append((nombre, self.current_score))
        self.high_scores.sort(key=lambda x: x[1], reverse=True)
        self.high_scores = self.high_scores[:5]  # Mantener solo top 5
        
    def obtener_mejores_puntuaciones(self):
        return self.high_scores