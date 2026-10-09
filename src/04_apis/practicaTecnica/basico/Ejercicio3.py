precios = [12, 45, 7, 30, 18]

# Debe devolver cuántos son mayores a 20
def contar_caros(precios):
    resultado = 0

    for precio in precios:
        if precio > 20:
            resultado +=1
    return resultado

print(contar_caros(precios))
