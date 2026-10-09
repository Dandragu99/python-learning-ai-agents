usuarios = [
    {"nombre": "Ana", "edad": 17, "activo": False},
    {"nombre": "Luis", "edad": 24, "activo": False},
    {"nombre": "Marta", "edad": 31, "activo": True},
    {"nombre": "Pablo", "edad": 16, "activo": True},
    {"nombre": "Laura", "edad": 22, "activo": True}
]


def buscar_primer_adulto_activo(usuarios):
    for usu in usuarios:
        if usu["activo"] == True and usu["edad"] >= 18:
            return usu

    return None

print(buscar_primer_adulto_activo(usuarios))