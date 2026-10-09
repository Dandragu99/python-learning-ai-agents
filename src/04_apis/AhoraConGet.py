respuesta = {
    "status": 200,
    "usuario": {
        "nombre": "Ana",
        "email": "ana@gmail.com"
    }
}

# El keyError con .get no hace falta
def obtener_nombre(respuesta):
    if respuesta.get("status") == 200:
        usuario = respuesta.get("usuario")

        if usuario:
            nombre = usuario.get("nombre")

            if nombre:
                return nombre

    return "Nombre no disponible"


print(obtener_nombre(respuesta))