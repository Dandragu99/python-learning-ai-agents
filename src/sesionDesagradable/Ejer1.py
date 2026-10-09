numeros = [4, 7, 12, 3, 18, 21, 8, 10]

def contar_mayores_de_10(numeros):
    contador = 0
    for numero in numeros:
        if numero > 10:
            contador += 1
    return contador

print(contar_mayores_de_10(numeros))
