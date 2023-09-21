
class Instrumentos:
     def afinar(self,instrumento):
          self.afinar= instrumento
          
     def tocar(self,instrumento):
          self.tocar = instrumento

     def presentar(self,instrumento):
          self.presentar = instrumento
          


class guitarra(Instrumentos):
     def afinar():
          return (f"la guitarra se esta afinando" )
     def tocar():
          return("tocando la Guitarra")
     def presentar():
          return("Una Guitarra")
     

class violin(Instrumentos):
     def afinar():
          return (f"El violin se esta afinando ")
     def tocar():
          return ("tocando el Violin")
     def presentar():
          return("Un Violin")

class bombo(Instrumentos):
     def afinar():
          return (f"el Bombo no se afina ")
     def tocar():
          return("tocando el Bombo")
     def presentar():
          return("Un Bombo")
     

class flauta(Instrumentos):
     def afinar():
          return (f"la flauta no se afina ")
     def tocar():
          return ("tocando la Flauta")
     def presentar():
          return("Una Flauta")