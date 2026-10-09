respuesta = {
    "status": 200,
    "usuario": {
        "nombre": "Ana",
        "email": "ana@gmail.com"
    }
}

def procesar_usuario(respuesta):
    try:
        if respuesta["status"] == 200:
            nombre = respuesta["usuario"]["nombre"]
            email = respuesta["usuario"]["email"]

            return f"Usuario: {nombre} - {email}"
        elif respuesta["status"] == 404:
            return "Usuario no encontrado"

        else:
            return "Error en la petición"

    except KeyError:
        print("Faltan datos del usuario")

print(procesar_usuario(respuesta))