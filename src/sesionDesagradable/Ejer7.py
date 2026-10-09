productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Portátil", "precio": 850},
    {"nombre": "Webcam", "precio": 70}
]

def sumar_productos_baratos(productos):
    suma = 0

    for producto in productos:
        if producto["precio"] < 100:
            suma += producto["precio"]

    return suma
print(sumar_productos_baratos(productos))