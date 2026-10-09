respuesta = {
    "status": 200,
    "usuario": {
        "nombre": "Ana",
        "email": "ana@gmail.com"
    }
}


def obtener_email(respuesta):
    try:
        if respuesta["status"] == 200:
            return respuesta["usuario"]["email"]
        elif respuesta["status"] == 404:
            return "Email no encontrado"
        else:
            return "Error en la petición"

    except KeyError:
        return "Datos incompletos"

print(obtener_email(respuesta))