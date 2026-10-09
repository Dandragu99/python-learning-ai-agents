numeros = [14, 3, 29, 8, 17, 41, 6]

def obtener_menor(numeros):
    menor = numeros[0]

    for numero in numeros:
        if numero < menor:
            menor = numero

    return menor

print(obtener_menor(numeros))