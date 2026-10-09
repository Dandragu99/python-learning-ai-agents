import requests

url = "https://jsonplaceholder.typicode.com/posts"

def obtener_posts_usuario(posts, user_id):
    resultado = []

    for post in posts:
        if post["userId"] == user_id:
            resultado.append(post)
    return resultado


response = requests.get(url)

if response.status_code == 200:
    print("Respuesta correcta")

    posts = response.json()
    posts_usuario = obtener_posts_usuario(posts, 3)

    for post in posts_usuario:
        print(post["title"])

else:
    print(f"Respuesta incorrecta {response.status_code}")