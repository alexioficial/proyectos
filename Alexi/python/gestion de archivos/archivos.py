'''
Permisos personalizar un archivo con python:
a: append, para agregar mas texto al final del archivo.
w: write, para escribir en el archivo.
x: para crear un nuevo archivo.
'''

c = open('ejemplo.txt', 'a')

c.write('hola, estoy modificando el archivo original')

c.close()