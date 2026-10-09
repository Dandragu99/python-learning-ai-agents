productos = [
    {"nombre": "Teclado", "precio": 25.99, "stock": 10},
    {"nombre": "Portatil", "precio": 799.99, "stock": 3},
    {"nombre": "Monitor", "precio": 249.99, "stock": 7},
    {"nombre": "Raton", "precio": 19.99, "stock": 2}
]

# Debe devolver los productos cuyo precio sea superior al indicado
def obtener_productos_caros(productos, precio_minimo):
    productos_caros = []
    for producto in productos:
        if producto["precio"] > precio_minimo:
            productos_caros.append(producto)

    return productos_caros

print(obtener_productos_caros(productos,700))

# Calcular valor inventario
def calcular_valor_inventario(productos):
    valorTotal = 0
    for producto in productos:
        valorTotal += producto["precio"] * producto["stock"]

    return valorTotal


print(calcular_valor_inventario(productos))

def buscar_producto(productos,nombre):
    nombre = ""

    for producto in productos:
        if nombre != None:
            return producto["nombre"]
        else:
            return None


print(buscar_producto(productos, "Teclado"))

