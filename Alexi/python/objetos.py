class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

usuario = Usuario('Alexi', 13)

print(usuario.nombre, usuario.edad)