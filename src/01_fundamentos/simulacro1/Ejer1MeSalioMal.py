def total_vendido_cliente(ventas):
    totales = {}
    for venta in ventas:
        cliente = venta["cliente"]
        importe = venta["importe"]

        if cliente in totales:
            totales[cliente] = totales[cliente] + importe
        else:
            totales["importe"] = importe
    return totales