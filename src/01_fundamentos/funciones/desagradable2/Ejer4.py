productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Portátil", "precio": 850},
    {"nombre": "Webcam", "precio": 70}
]

def resumen_caros(productos):
    contador = 0
    total = 0
    for producto in productos:
        if producto["precio"] >= 100:
            contador += 1
            total += producto["precio"]

    return {"cantidad": contador, "total": total}

print(resumen_caros(productos))