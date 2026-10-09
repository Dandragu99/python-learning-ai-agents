class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(self.nombre, self.precio, self.stock)

    def calcular_valor_stock(self):
        return self.precio * self.stock

    def hay_stock(self):
        if self.stock > 0:
            return True
        else:
            return False

teclado = Producto("Teclado", 25.99, 10)
portatil = Producto("Portatil", 799.99, 0)

teclado.mostrar_info()
print(teclado.calcular_valor_stock())
print(teclado.hay_stock())

portatil.mostrar_info()
print(portatil.hay_stock())