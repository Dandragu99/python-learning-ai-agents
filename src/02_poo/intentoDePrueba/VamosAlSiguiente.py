ventas = [
    {"producto": "Teclado", "precio": 25, "cantidad": 2},
    {"producto": "Monitor", "precio": 180, "cantidad": 1},
    {"producto": "Ratón", "precio": 15, "cantidad": 3},
    {"producto": "Webcam", "precio": 70, "cantidad": 2}
]

# Calcular las ventas

def calcular_ventas(ventas):
    cantidadVendida = 0
    precioTotal = 0
    producto_mas_vendido = None

    for venta in ventas:
        if venta["precio"] > 0:
            precioTotal += venta["precio"] * venta["cantidad"]

            if venta["cantidad"] > 0:
                cantidadVendida += venta["cantidad"]

                if producto_mas_vendido == None or venta["cantidad"] > producto_mas_vendido["cantidad"]:
                    producto_mas_vendido = venta

    return {"unidades_totales": cantidadVendida, "ingresos_totales": precioTotal, "producto_mas_vendido": producto_mas_vendido["producto"]}

print(calcular_ventas(ventas))