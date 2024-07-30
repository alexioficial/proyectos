operacion = input("que operacion quieres hacer: ")
if operacion == "suma":
    num1 = float(input("Escoge un numero para sumar: "))
    num2 = float(input("Escoge otro numero para sumar: "))
    resultado = (num1 + num2)
    print("El resultado de tu suma es: ", resultado)
elif operacion == "resta":
    num1 = float(input("Escoge un numero para restar: "))
    num2 = float(input("Escoge otro numero para restar: "))
    resultado = (num1 - num2)
    print("El resultado de tu resta es: ", resultado)
elif operacion == "multiplicacion":
    num1 = float(input("Escoge un numero para multiplicar: "))
    num2 = float(input("Escoge otro numero para multiplicar: "))
    resultado = (num1 * num2)
    print("El resultado de tu multiplicacion es: ", resultado)
elif operacion == "division":
    num1 = float(input("Escoge un numero para dividir: "))
    num2 = float(input("Escoge otro numero para dividir: "))
    resultado = (num1 / num2)
    print("El resultado de tu division es: ", resultado)
else:
    print("no se puede")