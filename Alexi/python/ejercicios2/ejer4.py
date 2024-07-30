# Escribir una funcion que devuelva el volumen de una esfera por su ratio.

from cmath import pi

def calcVol(r):
    return 4 / 3 * pi * r ** 3

resultado = calcVol(13)
print(resultado)