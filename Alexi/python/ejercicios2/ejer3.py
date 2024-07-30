# Imprimir el numero menor de una lista.

lista = []

numeroElementos = int(input('Cuantos elementos quieres agregar a la lista: '))

i = 0

while i < numeroElementos:
    j = int(input('Agregar el elemento: '))
    lista.append(j)
    i += 1
    if i >= numeroElementos:
        break

lista.sort()

if i >= numeroElementos:
    print(lista[0])