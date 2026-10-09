edades = [18, 25, 14, 30, 17, 22]

def contar_mayores_edad(edades):
    mayores = 0
    for edad in edades:
        if edad >= 18:
            mayores += 1
    return mayores

print(contar_mayores_edad(edades))

precios = [12.5, 30, 8.75, 20]

def calcular_total(precios):
    total = 0

    for precio in precios:
        total += precio
    return total

print(calcular_total(precios))

usuarios = [
    {"nombre": "Ana", "edad": 24},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Marta", "edad": 21}
]

def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            return usuario

    return None

print(buscar_usuario(usuarios,"Ana"))