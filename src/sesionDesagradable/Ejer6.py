productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Portátil", "precio": 850},
    {"nombre": "Webcam", "precio": 70}
]

def obtener_nombres_baratos(productos):
    lista = []

    for producto in productos:
        if producto["precio"] < 100:
            lista.append(producto["nombre"])
    return lista

print(obtener_nombres_baratos(productos))