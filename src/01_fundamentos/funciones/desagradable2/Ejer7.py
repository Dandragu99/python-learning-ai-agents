usuarios = [
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Luis", "edad": 24},
    {"nombre": "Marta", "edad": 31},
    {"nombre": "Pablo", "edad": 16},
    {"nombre": "Laura", "edad": 22}
]

def promedio_edad_adultos(usuarios):
    contador = 0
    sumaEdades = 0

    for usuario in usuarios:
        if usuario["edad"] >= 18:
            contador += 1
            sumaEdades += usuario["edad"]

    promedio = sumaEdades/contador
    return promedio

print(promedio_edad_adultos(usuarios))