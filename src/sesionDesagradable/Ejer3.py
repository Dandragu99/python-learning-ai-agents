numeros = [5, 12, 3, 18, 7, 25, 9]

def obtener_mayor(numeros):
    mayor = 0

    for numero in numeros:
        if numero > mayor:
            mayor = numero

    return mayor

print(obtener_mayor(numeros))