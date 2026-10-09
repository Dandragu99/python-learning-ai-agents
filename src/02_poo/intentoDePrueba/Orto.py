usuarios = [
    {"nombre": "Ana", "edad": 24, "activo": True},
    {"nombre": "Luis", "edad": 17, "activo": True},
    {"nombre": "Marta", "edad": 31, "activo": False},
    {"nombre": "Carlos", "edad": 22, "activo": True},
    {"nombre": "Sara", "edad": 16, "activo": False}
]
# Debe devolver una lista con los nombres de los usuarios que:
#- sean mayores de edad
#- estén activos
def obtener_usuarios_activos_mayores(usuarios):
    lista = []

    for usuario in usuarios:
        if usuario["edad"] >= 18 and usuario["activo"]:
            lista.append(usuario["nombre"])

    return lista

print(obtener_usuarios_activos_mayores(usuarios))