import requests


try:

    response = requests.get("https://api.example.com/usuarios", timeout = 10)
    response.raise_for_status()

    usuarios = response.json()
    for usuario in usuarios:
        print(usuario)

except requests.exceptions.RequestException as e:
    print(f"Error:{e}")