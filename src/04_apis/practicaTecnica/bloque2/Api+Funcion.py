import requests

url = "https://jsonplaceholder.typicode.com/users"
# Recibe los usarios que tengan id mayor a 5
def filtrar_usuarios(usuarios):
    resultado = []

    for usuario in usuarios:
        if usuario["id"] > 5:
            resultado.append(usuario)
    return resultado

response = requests.get(url)

if response.status_code == 200:
    print("Respuesta correcta")

    usuarios = response.json()

    ususarios_filtrados = filtrar_usuarios(usuarios)
    # Recorre el resultado e imprimes name - email
    for usuario in ususarios_filtrados:
        print(f'{usuario["name"]} - {usuario["email"]}')

else:
    print(f'Respuesta incorrecta {response.status_code}')