numeros = [4, 12, 7, 20, 3, 15]

def contar_mayores(numeros):
    contador = 0
    for numero in numeros:
        if numero > 10:
            contador += 1

    return contador

print(contar_mayores(numeros))


def devolver_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


print(devolver_pares(numeros))

def obtener_mayor(numeros):
    mayor = 0

    for numero in numeros:
        if numero > mayor:
            mayor = numero

    return mayor


print(obtener_mayor(numeros))