usuarios = [
    {"nombre": "Ana", "edad": 17, "activo": True},
    {"nombre": "Luis", "edad": 24, "activo": True},
    {"nombre": "Marta", "edad": 31, "activo": False},
    {"nombre": "Pablo", "edad": 16, "activo": True},
    {"nombre": "Laura", "edad": 22, "activo": True},
    {"nombre": "Carlos", "edad": 35, "activo": True}
]

def contar_activos_entre_18_y_30(usuarios):
    contador = 0

    for usuario in usuarios:
        if usuario["edad"] >= 18 and usuario["edad"] <= 30 and usuario["activo"]:
            contador += 1
    return contador

print(contar_activos_entre_18_y_30(usuarios))