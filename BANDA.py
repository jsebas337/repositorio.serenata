from INSTRUMENTOS import *
from MUSICOS import *
from random import *
class Banda : 
 def __init__(self) :
      self.instrumento_presentar = [guitarra.presentar(),violin.presentar(),flauta.presentar(),bombo.presentar()]
      self.instrumento_afinar = [guitarra.afinar(),violin.afinar(),flauta.afinar(),bombo.afinar()]
      self.instrumento_tocar = [guitarra.tocar(),violin.tocar(),flauta.tocar(),bombo.tocar()]
      self.banda=[] 
      self.musico = [] 
 
 
 def crear_banda(self):    
       
        for i in range (4) :
            banda = choice(self.instrumento_presentar[0:3])
            nom = choice(nombres[0:5])
            print (f'{nom} tiene {banda}' ) 

 def afinar_banda(self):
     for i in range (4) :
            banda = choice(self.instrumento_afinar[0:3])
            self.banda.append(banda)  
            print (banda)
            
             
 def tocar_banda(self):
     for i in range (4) :
            banda = choice(self.instrumento_tocar[0:3])
            self.banda.append(banda)  
            nom = choice(nombres[0:5])
            self.musico.append(nom) 
            print (f'{nom} esta  {banda}' )
            

     



        
        