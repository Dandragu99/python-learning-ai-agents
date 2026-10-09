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
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas

    def calcular_bonus(self):
        return self.ventas * 0.05


empleado1 = Programador("Ana", 30000)
empleado2 = Programador("Luis", 26000)
empleado3 = Comercial("Pedro", 24000, 50000)

empleados = [empleado1, empleado2, empleado3]

for empleado in empleados:
    print(empleado.nombre, empleado.calcular_bonus())