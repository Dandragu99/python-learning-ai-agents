productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Portátil", "precio": 850}
]

# contar cuantos productos cuestan más que precio_minimo y suánto suman entre todos
def analizar_productos(productos, precio_minimo):
    contador = 0
    sumaProductos = 0
    for producto in productos:
        if producto["precio"] > precio_minimo:
            contador += 1
            sumaProductos += producto["precio"]

    return contador, sumaProductos



print(analizar_productos(productos, 100))