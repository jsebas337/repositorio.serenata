from BANDA import *
x = 0
cant= randint(1,3)
print ("Por favor digita la opcion que desees")
while x!= 4:

 print ("1. Para crear banda")
 print ("2. Para afinar banda")
 print ("3. Para tocar banda ")
 print ("4. Salir")
 x =int(input("Ingresa la opcion:" ))
 t=Banda()
 if x==1 :
        print (f'{t.crear_banda(cant,cant)}\n')

 elif x==2:
        print (f'{t.afinar_banda(cant)}\n')

 elif x==3:
        print (f'{t.tocar_banda(cant)}\n')

 elif x==4:
        print ("Gracias por usar mi programa")

 elif x!=1 or x!=2 or x!=3 or x!=4 :
        print("opcion invalida\n1")

 



   


