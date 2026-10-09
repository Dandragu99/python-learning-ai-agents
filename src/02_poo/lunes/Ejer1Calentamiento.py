usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Luis", "edad": 17, "activo": True},
    {"nombre": "Marta", "edad": 32, "activo": False},
    {"nombre": "Pedro", "edad": 41, "activo": True},
    {"nombre": "Lucía", "edad": 16, "activo": False}
]

def analizar_usuarios(usuarios):
    adultos_activos = 0
    edad_total_adultos_activos = 0
    mayor = None

    for usuario in usuarios:
        if usuario["activo"] and usuario["edad"] >= 18:
            adultos_activos += 1
            edad_total_adultos_activos += usuario["edad"]

            if mayor == None or usuario["edad"] > mayor["edad"]:
                mayor = usuario

    return {"adultos_activos": adultos_activos, "edad_total_adultos_activos": edad_total_adultos_activos, "mayor": mayor["nombre"]}

print(analizar_usuarios(usuarios))