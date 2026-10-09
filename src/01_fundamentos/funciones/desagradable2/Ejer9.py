productos = [
    {"nombre": "Teclado", "precio": 25, "stock": 4},
    {"nombre": "Monitor", "precio": 180, "stock": 0},
    {"nombre": "Ratón", "precio": 15, "stock": 8},
    {"nombre": "Portátil", "precio": 850, "stock": 2},
    {"nombre": "Webcam", "precio": 70, "stock": 0}
]

# averiguar cantidad, total(suma precios) y el mas caro
def resumen_disponibles(productos):
    cantidad = 0
    total = 0
    mas_caro = None

    for producto in productos:
        if producto["stock"] > 0:
            cantidad += 1
            total += producto["precio"]

            if mas_caro is None or producto["precio"] > mas_caro["precio"]:
                mas_caro = producto


    return {"cantidad": cantidad, "total": total, "mas_caro": mas_caro["nombre"]}


print(resumen_disponibles(productos))