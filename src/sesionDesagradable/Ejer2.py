precios = [15, 40, 8, 60, 25, 100]

def sumar_caros(precios):
    suma = 0
    for precio in precios:
        if precio > 30:
            suma += precio
    return suma

print(sumar_caros(precios))