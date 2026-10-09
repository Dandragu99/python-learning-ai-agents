import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    print("Respuesta correcta")

    users = response.json()

    for user in users:
        if user["id"] > 5:
            print(f'{user["name"]} - {user["email"]}')