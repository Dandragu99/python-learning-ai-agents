import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout= 10
    )

    response.raise_for_status()

    usuarios = response.json()

    for usuario in usuarios:
        print(usuario)

except requests.exceptions.RequestException as e:
    print(f'Error en la petición: {e}')