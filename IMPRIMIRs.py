from tkinter import *
from BANDA import *
class Interfaz():

    


    def __init__ (self,ventana):
        def afinar():
           t=Banda()
           crear =t.crear_banda()
           res.set("El resultado de: " + str(crear) )
        def tocar():
           t=Banda()
           crear =t.tocar_banda()
           res.set("El resultado de: " + str(crear) )
        def salir():
            ventana.destroy()
        #Ventana
        self.ventana = ventana
        self.ventana.geometry("600x500")
        self.ventana.title("Instrumentos")
        self.ventana.config(bg="Green")
        res = StringVar()
        #Imagenes
        self.imagen1 = PhotoImage(file="bombomod.png")
        Label(self.ventana, image=self.imagen1).place (x=10, y=10)
        self.imagen2 = PhotoImage(file="flautamod.png")
        Label(self.ventana, image=self.imagen2).place (x=150, y=10)
        self.imagen3 = PhotoImage(file="guitarramod.png")
        Label(self.ventana, image=self.imagen3).place (x=300, y=20)
        self.imagen4 = PhotoImage(file="violinmod.png")
        Label(self.ventana, image=self.imagen4).place (x=520, y=10)
        #Botones
        self.boton1 = Button(ventana, text= "Afinar", command= afinar)
        self.boton1.place(x=20, y=100)
        self.boton2=Button(ventana, text= "Tocar", command= tocar)
        self.boton2.place (x=245, y = 100)
        self.boton3= Button(ventana, text="Salir",command= salir)
        self.boton3.place (x=550, y=100) 
        #Texto 
        textoR = Label(ventana,textvariable=res)
        textoR.place(x=150,y=140)
        
       


obj = Interfaz(Tk())
obj.ventana.mainloop()