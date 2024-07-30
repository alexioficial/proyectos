juan = {
    "nombre": "pan con queso",
    "raza": "NOSE",
    "edad": "*numero que no existe*"
}
juan["asdf"] = "asdf :>" # <-- crea un nuevo elemento
juan["nombre"] = "Alexi" # <-- cambia un valor del diccionario
del juan["raza"] # <-- elimina un valor del diccionario

print(juan)
print(juan["nombre"]) # <-- accede a un elemento del diccionario