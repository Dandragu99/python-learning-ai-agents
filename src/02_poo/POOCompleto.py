class Vehiculo:
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    def calcular_impuesto(self):
        # por defecto devuelve 0
        return 0


class Coche(Vehiculo):
    def calcular_impuesto(self):
        # devuelve el 10% del precio
        precioFinal = self.precio * 0.10
        return precioFinal


class Moto(Vehiculo):
    def calcular_impuesto(self):
        # devuelve el 5% del precio
        precioFinal = self.precio * 0.05
        return precioFinal


coche1 = Coche("Toyota", 20000)
coche2 = Coche("BMW", 30000)
moto1 = Moto("Honda", 8000)

vehiculos = [coche1, coche2, moto1]

for vehiculo in vehiculos:
    print(vehiculo.calcular_impuesto())

def calcular_impuestos_totales(vehiculos):
    impuesto = 0
    for vehiculo in vehiculos:
        impuesto += vehiculo.calcular_impuesto()
    return impuesto

print(calcular_impuestos_totales(vehiculos))