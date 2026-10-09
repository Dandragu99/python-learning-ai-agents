usuarios = [
    {"nombre": "Ana", "edad": 17, "activo": True},
    {"nombre": "Luis", "edad": 24, "activo": True},
    {"nombre": "Marta", "edad": 31, "activo": False},
    {"nombre": "Pablo", "edad": 16, "activo": True},
    {"nombre": "Laura", "edad": 22, "activo": True}
]

def contar_adultos_activos(usuarios):
    contador = 0

    for usuario in usuarios:
        if usuario["activo"] == True and usuario["edad"] >= 18:
            contador += 1
    return contador
print(contar_adultos_activos(usuarios))