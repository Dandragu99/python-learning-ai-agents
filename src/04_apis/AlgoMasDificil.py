respuesta = {
    "status": 200,
    "usuario": {
        "nombre": "Ana",
        "email": "ana@gmail.com",
        "activo": True
    }
}

def procesar_usuario(respuesta):
    # 1. comprobar status
    if respuesta.get("status") != 200:
        return "Datos incompletos"

    # 2. sacar usuario
    usuario = respuesta.get("usuario")

    # 3. comprobar que usuario existe
    if not usuario:
        return "Datos incompletos"

    # 4. comprobar activo
    if not usuario.get("activo"):
        return "Usuario inactivo"

    # 5. sacar nombre y email
    nombre = usuario.get("nombre")
    email = usuario.get("email")

    # 6. comprobar que existen
    if not nombre or not email:
        return "Datos incompletos"

    # 7. devolver nombre - email
    return f"{nombre} - {email}"


print(procesar_usuario(respuesta))