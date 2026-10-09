productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Portátil", "precio": 850}
]
# debe devolver precio > 100 si no encuentra devolver None
def buscar_primer_caro(productos):
    for pro in productos:
        if pro["precio"] > 100:
            return pro

    return None

print(buscar_primer_caro(productos))