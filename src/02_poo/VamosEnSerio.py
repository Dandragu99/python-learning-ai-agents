class Coche:
    def __init__(self, marca, modelo, kilometros):
        self.marca = marca
        self.modelo = modelo
        self.kilometros = kilometros

    def mostrar_info(self):
        print(self.marca, self.modelo, self.kilometros)

    def necesita_revision(self):
        # devolver True si tiene 15000 km o más+
        if self.kilometros >= 15000:
            return True
        # devolver False si tiene menos
        else:
            return False

coche1 = Coche("Toyota", "Corolla",12000)
coche2 = Coche("BMW", "320d",22000)

coche1.mostrar_info()
print(coche1.necesita_revision())

coche2.mostrar_info()
print(coche2.necesita_revision())
