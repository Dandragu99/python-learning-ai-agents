respuesta = {
    "status": 200,
    "tickets": [
        {
            "id": 101,
            "cliente": "Ana",
            "prioridad": "alta",
            "estado": "abierto",
            "categoria": "facturacion"
        },
        {
            "id": 102,
            "cliente": "Luis",
            "prioridad": "baja",
            "estado": "cerrado",
            "categoria": "tecnico"
        },
        {
            "id": 103,
            "cliente": "Pedro",
            "prioridad": "alta",
            "estado": "abierto",
            "categoria": "tecnico"
        },
        {
            "id": 104,
            "cliente": "Ana",
            "prioridad": "media",
            "estado": "abierto",
            "categoria": "facturacion"
        },
        {
            "id": 105,
            "cliente": "Marta",
            "prioridad": "alta",
            "estado": "cerrado",
            "categoria": "tecnico"
        },
        {
            "id": 106,
            "cliente": "Ana",
            "prioridad": "alta",
            "estado": "abierto",
            "categoria": "tecnico"
        }
    ]
}

# 1. Comprobar que:
# respuesta = 200
def analizar_tickets(respuesta):
    if respuesta["status"] == 200:
        if respuesta.get("tickets"):
            tickets = respuesta.get("tickets")
        else:
            return {"error": "No hay tickets"}
    else:
        return {"error": "Error en la API"}

    total_tickets = 0
    tickets_abiertos = 0
    prioridad_alta_tickets = 0

    tickets_totales_por_cliente = {}
    id_urgentes = []

    # PRIMER BUCLE:
    # recorremos todos los tickets y recopilamos información
    for ticket in tickets:

        total_tickets += 1

        # Contamos todos los tickets abiertos
        if ticket["estado"] == "abierto":
            tickets_abiertos += 1

        # Contamos los que son abiertos Y de prioridad alta
        if ticket["estado"] == "abierto" and ticket["prioridad"] == "alta":
            prioridad_alta_tickets += 1
            id_urgentes.append(ticket["id"])

        # Sacamos el cliente del ticket actual
        cliente = ticket["cliente"]

        # Contamos cuántos tickets tiene cada cliente
        if cliente in tickets_totales_por_cliente:
            tickets_totales_por_cliente[cliente] += 1
        else:
            tickets_totales_por_cliente[cliente] = 1


    # SEGUNDO BUCLE:
    # ahora que YA tenemos:
    #
    # {
    #     "Ana": 3,
    #     "Luis": 1,
    #     "Pedro": 1,
    #     "Marta": 1
    # }
    #
    # buscamos quién tiene el número más alto

    cliente_mas_tickets = None
    mayor_numero_tickets = 0

    for cliente, cantidad in tickets_totales_por_cliente.items():

        if cantidad > mayor_numero_tickets:
            mayor_numero_tickets = cantidad
            cliente_mas_tickets = cliente


    return {
        "total_tickets": total_tickets,
        "tickets_abiertos": tickets_abiertos,
        "urgentes": prioridad_alta_tickets,
        "tickets_por_cliente": tickets_totales_por_cliente,
        "cliente_mas_tickets": cliente_mas_tickets,
        "ids_urgentes": id_urgentes
    }

print(analizar_tickets(respuesta))

