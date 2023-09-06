class Musico:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento

    def imprimir (self):
        print(f"{self.nombre} tiene el {self.instrumento}.")

    def afinar(self):
        instrumentos_afinables = ["Guitarra", "Violin", "Violonchelo"]
        if self.instrumento in instrumentos_afinables:
            print(f"{self.nombre} esta afinando su {self.instrumento}.")
        else:
            print(f"{self.nombre} con su {self.instrumento} esta esperando.")

    def tocar(self):
        print(f"{self.nombre} esta tocando el {self.instrumento}.")

nombres = ["Jose", "Sergio", "Nicolas", "Sebastian", "Kevin", "Martin"]
instrumentos = ["Guitarra", "Violin", "Violonchelo", "Flauta", "Trompeta", "Piano"]





