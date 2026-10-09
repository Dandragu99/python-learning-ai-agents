usuarios = [
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Luis", "edad": 24},
    {"nombre": "Marta", "edad": 31},
    {"nombre": "Laura", "edad": 22}
]

def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            return usuario

    return None

print(buscar_usuario(usuarios,"Luis"))