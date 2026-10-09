import requests

def obtener_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    if response.status_code == 200:

        usuarios = response.json()


        lista = []
        for usuario in usuarios:
            usuario_filtrado = {
                "id": usuario["id"],
                "name": usuario["name"],
                "email": usuario["email"]
            }
            lista.append(usuario_filtrado)

        return lista
    else:
        return {"error": "No se puedieron obtener los usuarios"}

print(obtener_usuarios())

def filtrar_usuarios_gmail():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        usuarios = response.json()
        usuario_filtrado = []
        for usuario in usuarios:

            if usuario["email"].endswith(".biz"):
                dic = {
                    "id": usuario["id"],
                    "name": usuario["name"],
                    "email": usuario["email"]
                }
                usuario_filtrado.append(dic)
        return usuario_filtrado

    else:
        return {"error": "Error al obtener usuarios"}

print(filtrar_usuarios_gmail())

def buscar_usuario_por_id(id_buscado):
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:

        usuarios = response.json()
        for usuario in usuarios:
            if usuario["id"] == id_buscado:
                return usuario

        return {"error": "Usuario no encontrado"}

print(buscar_usuario_por_id(9))

def filtrar_usuarios_por_dominio(dominio):
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        usuarios = response.json()
        lista_usuarios_filtrados = []
        for usuario in usuarios:
            usuario_filtrado = {
                "id": usuario["id"],
                "name": usuario["name"],
                "email": usuario["email"]
            }
            if usuario["email"].endswith(dominio):
                lista_usuarios_filtrados.append(usuario_filtrado)
        return lista_usuarios_filtrados
    else:
        {"error": "No se han encontrado usuarios"}

print(filtrar_usuarios_por_dominio(".org"))

