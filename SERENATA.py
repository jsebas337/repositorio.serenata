from random import choice
from MUSICO import *

musicos = []

for i in range(len(nombres)):
    musico = Musico(choice(nombres), choice(instrumentos))
    nombres.remove(musico.nombre)
    instrumentos.remove(musico.instrumento)
    musicos.append(musico)

