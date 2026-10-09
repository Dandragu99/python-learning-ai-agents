productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15}
]

def buscar_producto(productos, nombre):
    for producto in productos:
        if producto["nombre"] == nombre:
            return producto

    return None
print(buscar_producto(productos, "Monitor"))