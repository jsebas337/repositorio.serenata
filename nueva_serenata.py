class SerenataXd:
    def __init___ (self,nombres,instrumentos):
        self.nombre = nombres
        self.instrumento = instrumentos
        
    def Afinar(self):
        pass

    def mostrar_informacion(self):
        return (self.instrumento, self.nombre)
    

class InstrumentoAfinar(SerenataXd):
    def Afinar(self):
     return (f' {self.nombre} esta afinando el/la{self.instrumento}')

class InstrumentoNA(SerenataXd):
    def Afinar(self):
     return (f' {self.nombre} esta esperando :(')
