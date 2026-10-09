productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Portátil", "precio": 850}
]

def obtener_caros(productos):
    lista = []

    for producto in productos:
        if producto["precio"] > 100:
            lista.append(producto)
    return lista

print(obtener_caros(productos))