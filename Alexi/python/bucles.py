# Esto es un bucle while.

i = 1

while i <= 30:
    if i == 20:
        break # <-- si se cumple la condicional para el conteo.
    i += 1
    print(i)

usuarios = ['juan', 'juen', 'juin', 'juon', 'juun']
j = 0

while j < len(usuarios):
    print(usuarios[j])
    j += 1