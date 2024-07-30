# Hacer una app donde puedes escribir la cantidad de numeros que quieras hasta que digas basta para que te devuelva la suma de esos numeros.

lista = []

print("ingrese numeros y para salir escriba basta")
while True:
    valor = input('ingrese el valor: ')
    if valor == 'basta':
        break
    else:
        try: 
            valor = int (valor)
            lista.append(valor)
        except:
            print('dato invalido')
            exit()
        resultado = 0
        for x in lista:
            resultado += x

print(resultado)