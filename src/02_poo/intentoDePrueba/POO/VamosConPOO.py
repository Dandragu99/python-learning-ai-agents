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
        return self.salario * 0.15


programador1 = Programador("Ana", 30000)
programador2 = Programador("Carlos", 35000)
comercial1 = Comercial("Luis", 28000)

empleados = [programador1, comercial1, programador2]

def calcular_bonus_totales(empleados):
    bonus_total = 0

    for empleado in empleados:
        bonus_total += empleado.calcular_bonus()

    return bonus_total

print(calcular_bonus_totales(empleados))

