from MUSICO import *
from SERENATA import *

print("¡Bienvenido a la serenata!")
for musico in musicos:
            musico.imprimir()
        

while True:
    accion = input("¿Que desea hacer? (afinar/comenzar): ").lower()
    if accion == "afinar":
        print("Afinando los instrumentos:")
        for musico in musicos:
            musico.afinar()
    elif accion == "comenzar":
        print("\nLa serenata comienza:")
        for musico in musicos:
            musico.tocar()
        break    
    else:
        print("Por favor, seleccione 'afinar' o 'comenzar'.")
