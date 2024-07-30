# Indica una funcion para comprobar si el usuario es mayor de edad.

def calcularEdad(calc):
    if calc < 18:
        print('Eres menor, no puedes pasar')
    else:
        print('Dale pasa')

    return calc

calcular = calcularEdad(19)