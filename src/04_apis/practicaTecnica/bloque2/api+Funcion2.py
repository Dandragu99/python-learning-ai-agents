import requests

url = "https://jsonplaceholder.typicode.com/users"

def filtrar_email(usuarios):
    resultado = []

    for usuario in usuarios:
        if ".org" in usuario["email"]:
            resultado.append(usuario)
    return resultado

response = requests.get(url)

if response.status_code == 200:
    print("Respuesta correcta")

    usuarios = response.json()

    usuarios_filtrados = filtrar_email(usuarios)

    for usuario in usuarios_filtrados:
        print(f'{usuario["name"]} - {usuario["email"]}')

else:
    print("Respuesta incorrecta")