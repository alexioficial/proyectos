import nombres as n

numeroElementos = int(input('Cuantos elementos quieres agregar a la lista: '))

i = 0

while i < numeroElementos:
    j = input('Agregar el elemento: ')
    n.listaNombres.append(j)
    i += 1
    if i >= numeroElementos:
        break

if i >= numeroElementos:
    print(n.listaNombres)