productos = [
    {"nombre": "Teclado", "precio": 25, "stock": 4},
    {"nombre": "Monitor", "precio": 180, "stock": 0},
    {"nombre": "Ratón", "precio": 15, "stock": 8},
    {"nombre": "Portátil", "precio": 850, "stock": 2},
    {"nombre": "Webcam", "precio": 70, "stock": 0}
]

def resumen_disponibles(productos):
    # productos disponibles
    cantidad = 0
    # precio de la suma de los tres productos con stock
    precio_total = 0
    # producto más caro en la lista
    mas_caro = None

    for producto in productos:
        if producto["stock"] > 0:
            cantidad +=1
            precio_total += producto["precio"]

            if mas_caro is None or producto["precio"] > mas_caro["precio"]:
                mas_caro = producto

    return cantidad, precio_total, mas_caro["nombre"]

print(resumen_disponibles(productos))