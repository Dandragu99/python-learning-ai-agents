nuevo_usuario = {
    "name" : "Danut",
    "email" : "danut@example.com"
}

import requests

response = requests.post("https://jsonplaceholder.typicode.com/users", json=nuevo_usuario)

if response.status_code == 201:
    print("Respuesta correcta")
    print(response.json())
else:
    print(f'La respuesta ha fallado {response.status_code}')


