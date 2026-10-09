productos = [
    {"nombre": "Teclado", "precio": 25, "stock": 4},
    {"nombre": "Monitor", "precio": 180, "stock": 0},
    {"nombre": "Ratón", "precio": 15, "stock": 8},
    {"nombre": "Portátil", "precio": 850, "stock": 2},
    {"nombre": "Webcam", "precio": 70, "stock": 3}
]

def analizar_stock(productos):
    productos_disponibles = 0
    unidades_totales = 0
    valor_total_stock = 0
    producto_mayor_valor = None

    for p in productos:
        if p["stock"] > 0:
            productos_disponibles += 1
            unidades_totales += p["stock"]
            valor_total_stock += p["stock"] * p["precio"]

            if producto_mayor_valor is None or p["precio"] > producto_mayor_valor["precio"]:
                producto_mayor_valor = p

    return {"productos_disponibles": productos_disponibles, "unidades_totales": unidades_totales, "valor_total_stock": valor_total_stock, "producto_mayor_valor": producto_mayor_valor["nombre"]}

print(analizar_stock(productos))