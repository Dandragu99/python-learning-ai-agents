productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Portátil", "precio": 850}
]

def obtener_productos_caros(productos, precio_minimo):
    productosCaros = []
    for producto in productos:
        if producto["precio"] > precio_minimo:
            productosCaros.append(producto["nombre"])

    return productosCaros

print(obtener_productos_caros(productos, 100))