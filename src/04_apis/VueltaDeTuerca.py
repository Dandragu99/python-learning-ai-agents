respuesta = {
    "status": 200,
    "usuario": {
        "nombre": "Luis",
        "email": "luis@gmail.com",
        "activo": True,
        "rol": "admin"
    }
}

# La función debe devolver Luis - admin

def buscar_admin(respuesta):
    if respuesta.get("status") != 200:
        return "Datos incompletos"

    usuario = respuesta.get("usuario")
    if not usuario:
        return "Usuario no existe"
    if not usuario.get("activo"):
        return "Usuario inactivo"
    nombre = usuario.get("nombre")
    rol = usuario.get("rol")

    if not nombre or not rol:
        return "Datos incompletos"
    return f'{nombre} - {rol}'

print(buscar_admin(respuesta))