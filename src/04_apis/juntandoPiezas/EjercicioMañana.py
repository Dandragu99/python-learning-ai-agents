import requests


def analizar_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None

    usuarios = obtener_usuarios()

def buscar_usuario_por_id(usuarios, id_buscado):
    for usuario in usuarios:
        if usuario["id"] == id_buscado:
            return {
                "id": usuario["id"],
                "name": usuario["name"],
                "email": usuario["email"]
            }

    return None


def contar_dominios(usuarios):
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    dominios = {}


    for usuario in usuarios:
        dominio = usuario["email"].split(".")[-1]
        if dominios in dominios:
            dominio[dominio] += 1
        else:
            dominio[dominio] = 1

    return dominio

def analizar_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        usuarios = response.json()
    else:
        ("error:" "La petición no existe")

    cantidad_usuarios = 0
    usuario_id3 = [2]
    for usuario in usuarios:
        if usuario["name"]:
            cantidad_usuarios += 1

        if usuario_id3 == usuario["id"][2]:
            usuario["name"]
        else:
            ("Usuario 3, no encontrado")

        dominio = usuario["email"].split(".")[-1]
        if dominios in dominios:
            dominio[dominio] += 1
        else:
            dominio[dominio] = 1




    return {
        "total_usuarios": cantidad_usuarios,
        "usuarios_gmail": dominio["gmail"],
        "usuario_buscado": usuario_id3,
        "dominios": dominio
    }

print(analizar_usuarios())