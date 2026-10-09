ventas = [
    {"cliente": "Ana", "importe": 120.5},
    {"cliente": "Luis", "importe": 80},
    {"cliente": "Ana", "importe": 40},
]
# Resultado esperado: {"Ana": 160.5, "Luis": 80}

# Escribe una función que reciba una lista de diccionarios como esta y devuelva el total vendido por cada cliente

def total_vendido_cliente(ventas):
    totales = {}
    for venta in ventas:
        cliente = venta["cliente"]
        totales[cliente] = totales.get(cliente, 0) + venta["importe"]
    return totales

print(total_vendido_cliente(ventas))