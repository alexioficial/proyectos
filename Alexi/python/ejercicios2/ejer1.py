# En este ejercicio se tiene que realizar una multiplicacion sin el signo de multiplicar

num1 = int(input('primer numero pa multiplicar: '))
num2 = int(input('segundo numero pa multiplicar: '))

resultado = 0

for i in range(num1):
    resultado += num2

print(resultado)