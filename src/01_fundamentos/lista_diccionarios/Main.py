
#Diccionario
usuarios = [
    {"nombre": "Ana", "edad": 24},
    {"nombre": "Luis", "edad": 31},
]

mayores = [u for u in usuarios if u["edad"] >= 25]

for usuario in mayores:
    print(usuario["nombre"])
