usuarios = [
    {"nombre": "Ana", "edad": 17, "activo": True},
    {"nombre": "Luis", "edad": 24, "activo": True},
    {"nombre": "Marta", "edad": 31, "activo": False},
    {"nombre": "Pablo", "edad": 16, "activo": True},
    {"nombre": "Laura", "edad": 22, "activo": True},
    {"nombre": "Carlos", "edad": 35, "activo": False}
]

def promedio_edad_adultos_activos(usuarios):
    suma_adultos = 0
    contador = 0

    for usuario in usuarios:
        if usuario["activo"] and usuario["edad"] >= 18:
            contador += 1
            suma_adultos += usuario["edad"]

    if contador > 0:
        promedio = suma_adultos / contador
        return promedio

    return None

print(promedio_edad_adultos_activos(usuarios))