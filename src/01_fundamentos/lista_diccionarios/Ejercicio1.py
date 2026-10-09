
usuarios = [
    {"nombre": "Ana", "edad": 24},
    {"nombre": "Luis", "edad": 31},
    {"nombre": "Pedro", "edad": 19},
]
# Escrbe código que recorra usuario e imprima:
# Ana tiene 24 años ...

for usuario in usuarios:
    print(f'{usuario["nombre"]} tiene {usuario["edad"]} años')

# Imprimir solos los uusairo smayores de 20 años con formato

for usuario in usuarios:
    if usuario["edad"] > 25:
        print(f'{usuario["nombre"]} - {usuario["edad"]}')

# Cuenta cuántos usuarios tienen 20 años o más e imprime.

contador = 0;
for usuario in usuarios:
    if usuario["edad"] >= 20:
        contador += 1
print(f'Hay {contador} usuarios mayores de 20 años')

# Suma todas las edades y al final imprime -> La suma de edades es X

sumaEdades = 0;
for usuario in usuarios:
    sumaEdades += usuario["edad"]

print(f'La suma de edades es {sumaEdades}')

# Calcula la edad media de todos los usuarios

sumaEdades = 0
for usuario in usuarios:
    sumaEdades += usuario["edad"]

mediaEdades = sumaEdades / len(usuarios)
print(f'La media de las edades de todos los usuarios es {mediaEdades}')

# Encuentra el usuario de mayor edad sin usar max()

edadMaxima = 0
usuarioMayor = None

for usuario in usuarios:
    if usuario["edad"] > edadMaxima:
        edadMaxima = usuario["edad"]
        usuarioMayor = usuario

print(f'El usuario con la edad máxima es {usuarioMayor["nombre"]} con {edadMaxima} años')


