numeros = [4, 15, 8, 23, 42, 7, 18]

# Recorrer, quedarse con los mayores de 10 que sean pares. Guardarlos en una lista y devolverlos.

def obtener_mayores_pares(numeros):
    numerosPares = []

    for numero in numeros:
        if numero > 10 and numero %2 == 0:
            numerosPares.append(numero)

    return numerosPares

print(obtener_mayores_pares(numeros))