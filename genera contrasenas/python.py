import random as rnd

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!@#$%^&*()_+-=[];:.,<>?/~`|'

unidos = f'{letras}{numeros}{simbolos}'

contrasena = ''.join(rnd.sample(unidos, 25))

print('Su contrasena es:')
print(contrasena)