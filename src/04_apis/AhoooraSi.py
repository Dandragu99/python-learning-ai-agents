respuesta = {
    "status": 200,
    "usuarios": [
        {
            "nombre": "Ana",
            "activo": True,
            "rol": "admin"
        },
        {
            "nombre": "Luis",
            "activo": False,
            "rol": "usuario"
        },
        {
            "nombre": "Pedro",
            "activo": True,
            "rol": "usuario"
        }
    ]
}


def obtener_activos(respuesta):
    if respuesta.get("status") != 200:
        return []

    usuarios = respuesta.get("usuarios")

    if not usuarios:
        return []

    usuarios_activos = []
    for usuario in usuarios:
        if usuario["activo"]:
            usuarios_activos.append(usuario["nombre"])

    return usuarios_activos

print(obtener_activos(respuesta))
