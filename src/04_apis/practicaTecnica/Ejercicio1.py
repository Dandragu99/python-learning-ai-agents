numeros = [4, 17, 8, 23, 10, 5, 30, 12]

def filtrar_mayores(numeros):
    resultado = []

    for numero in numeros:
        if numero > 10:
            resultado.append(numero)
    return resultado


print(filtrar_mayores(numeros))