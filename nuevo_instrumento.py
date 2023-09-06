from nueva_serenata import *
from random import *
class Guardar :
    def __init__(self):
        self.nombres_instrumentos = []
    
    def agregar_instrumento (self, instrumento):
        self.nombres_instrumentos.append(instrumento)
    
    def imprimir_instrumento(self):
        return choice(self.nombres_instrumentos)