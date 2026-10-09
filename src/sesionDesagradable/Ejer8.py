productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Portátil", "precio": 850},
    {"nombre": "Webcam", "precio": 70}
]

def obtener_producto_mas_caro(productos):
    producto_caro = productos[0]

    for producto in productos:
        if producto["precio"] > producto_caro["precio"]:
            producto_caro = producto

    return producto_caro

print(obtener_producto_mas_caro(productos))
