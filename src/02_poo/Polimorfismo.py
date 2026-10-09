class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bonus(self):
        return 0


class Programador(Empleado):
    def calcular_bonus(self):
        return self.salario * 0.10


class Comercial(Empleado):
    def calcular_bonus(self):
        return self.salario * 0.20

class Becario(Empleado):
    def calcular_bonus(self):
        return self.salario * 0.05


programador = Programador("Dani", 22000)
comercial = Comercial("Ana", 24000)
becario = Becario("Juan", 18000)

empleados = [programador, comercial, becario]

for empleado in empleados:
    print(empleado.nombre, empleado.calcular_bonus())