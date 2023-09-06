from nuevo_instrumento import *
t= Guardar()
t.agregar_instrumento(InstrumentoAfinar('Guitarra', 'Jose'))
t.agregar_instrumento(InstrumentoAfinar('Violin','Sergio'))
t.agregar_instrumento(InstrumentoAfinar('Violonchelo', 'Sebastian'))
t.agregar_instrumento(InstrumentoNA('Flauta','Nicolas'))
t.agregar_instrumento(InstrumentoNA('Trompeta','Martin'))
t.agregar_instrumento(InstrumentoNA('Piano', 'Kevin'))

for i in range(3):
 a=t.imprimir_instrumento()
 print(a.Afinar(), a.mostrar_informacion())