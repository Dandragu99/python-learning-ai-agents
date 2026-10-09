import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

# 1. Si la respuesta es 200, convierte el JSON a python
# 2. Recorra los usuarios
# 3. Imprima el nombre de cada usuario.

if response.status_code == 200:
    usuarios = response.json()

    for usuario in usuarios:
        print(f'{usuario["name"]} - {usuario["email"]}')
else:
    print(response.status_code)

# Get /users/1
response1 = requests.get("https://jsonplaceholder.typicode.com/users/9999")
if response1.status_code == 200:
    usuario = response1.json()

    print(f'{usuario["name"]} - {usuario["id"]}')
else:
    print(response1.status_code)