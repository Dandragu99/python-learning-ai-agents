productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Portátil", "precio": 850}
]

# mayor > número mayor de la lista

def obtener_mas_caro(productos):
    mas_caro = productos[0]
    for p in productos:
        if mas_caro["precio"] < p["precio"]:
            mas_caro = p

    return mas_caro

print(obtener_mas_caro(productos))