usuarios = [
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Luis", "edad": 24},
    {"nombre": "Marta", "edad": 31},
    {"nombre": "Pablo", "edad": 16},
    {"nombre": "Laura", "edad": 22}
]

def obtener_adultos(usuarios):
    lista = []
    for usuario in usuarios:
        if usuario["edad"] >= 18:
            lista.append(usuario)

    return lista

print(obtener_adultos(usuarios))