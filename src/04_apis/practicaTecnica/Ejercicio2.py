usuarios = [
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Luis", "edad": 17},
    {"nombre": "Marta", "edad": 30},
    {"nombre": "Pablo", "edad": 16}
]

def obtener_adultos(usuarios):
    resultado = []

    for usuario in usuarios:
        if usuario["edad"] >= 18:
            resultado.append(usuario)
    return resultado

print(obtener_adultos(usuarios))
