class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


producto1 = Producto("Teclado", 25, 4)
producto2 = Producto("Monitor", 180, 0)
producto3 = Producto("Ratón", 15, 8)
producto4 = Producto("Portátil", 850, 2)

productos = [producto1, producto2, producto3, producto4]

def analizar_productos(productos):
    disponible = 0
    valor_stock = 0
    mas_caro = None

    for producto in productos:
        if producto.stock > 0:
            disponible += 1

            valor_stock += producto.stock * producto.precio

            if mas_caro == None or producto.precio > mas_caro.precio:
                mas_caro = producto

    return {"disponibles": disponible,"valor_stock": valor_stock,"mas_caro": mas_caro.nombre}

print(analizar_productos(productos))