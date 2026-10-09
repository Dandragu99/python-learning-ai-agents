import requests

def buscar_usuario(id_usuario):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    usuarios = response.json()

    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            print(f'{usuario["name"]}')

    return print("Usuario no encontrado")


print(buscar_usuario(7))

class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

persona1 = Persona("Angel")
print(persona1.nombre)


class Animal:
    def __init__(self,nombre,tipo):
        self.nombre = nombre;
        self.tipo = tipo;

Perro = Animal("perro","pastor alemán")

print(f'Tengo un {Perro.nombre} y es un {Perro.tipo}')

















