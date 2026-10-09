respuesta = {
    "status": 200,
    "usuario": {
        "nombre": "Ana",
        "email": "ana@gmail.com"
    }
}

print(respuesta["status"])
print(respuesta["usuario"])
print(respuesta["usuario"]["nombre"])
print(respuesta["usuario"]["email"])

try:
    print(respuesta["edad"])
except KeyError:
    print("Ese dato no existe")

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

    except KeyError:
        return "Email no encontrado"

print(obtener_email(respuesta))