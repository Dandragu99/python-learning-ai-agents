import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    print(f'Respuesta correcta {response.status_code}')
    usuarios = response.json()

    for usuario in usuarios:
        if usuario["id"] > 5:
            print(f'{usuario["name"]} - {usuario["email"]}')

else:
    print("Respuesta incorrecta")