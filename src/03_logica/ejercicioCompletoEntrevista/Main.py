pedidos = [
    {"cliente": "Ana", "producto": "Portátil", "precio": 850, "cantidad": 1, "pagado": True},
    {"cliente": "Luis", "producto": "Ratón", "precio": 25, "cantidad": 2, "pagado": True},
    {"cliente": "Ana", "producto": "Teclado", "precio": 50, "cantidad": 1, "pagado": False},
    {"cliente": "Pedro", "producto": "Monitor", "precio": 180, "cantidad": 2, "pagado": True},
    {"cliente": "Luis", "producto": "Webcam", "precio": 70, "cantidad": 1, "pagado": False},
    {"cliente": "Ana", "producto": "Ratón", "precio": 25, "cantidad": 3, "pagado": True},
    {"cliente": "Marta", "producto": "Monitor", "precio": 180, "cantidad": 1, "pagado": True},
]


def analizar_pedidos(pedidos):
    numero_pedidos = 0
    unidades_vendidas = 0
    ingresos_totales = 0

    cliente_mayor_gasto = None
    producto_mas_vendido = None

    ventas_por_cliente = {}
    unidades_por_producto = {}

    mayor_gasto = 0
    mayor_unidades = 0

    for pedido in pedidos:

        if pedido["pagado"]:
            numero_pedidos += 1
            unidades_vendidas += pedido["cantidad"]

            importe = pedido["precio"] * pedido["cantidad"]
            ingresos_totales += importe

            cliente = pedido["cliente"]

            if cliente in ventas_por_cliente:
                ventas_por_cliente[cliente] += importe
            else:
                ventas_por_cliente[cliente] = importe

            producto = pedido["producto"]

            if producto in unidades_por_producto:
                unidades_por_producto[producto] += pedido["cantidad"]
            else:
                unidades_por_producto[producto] = pedido["cantidad"]

    # Ahora que ya tenemos todos los clientes acumulados,
    # buscamos quién ha gastado más
    for cliente, total in ventas_por_cliente.items():
        if total > mayor_gasto:
            mayor_gasto = total
            cliente_mayor_gasto = cliente

    # Y ahora buscamos el producto con más unidades vendidas
    for producto, unidades in unidades_por_producto.items():
        if unidades > mayor_unidades:
            mayor_unidades = unidades
            producto_mas_vendido = producto

    return (
        numero_pedidos,
        unidades_vendidas,
        ingresos_totales,
        cliente_mayor_gasto,
        producto_mas_vendido,
        ventas_por_cliente
    )


print(analizar_pedidos(pedidos))