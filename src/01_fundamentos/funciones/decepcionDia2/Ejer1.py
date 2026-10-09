class Empleado():
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
        super().__init__(nombre,salario)
        self.ventas = ventas

    def calcular_bonus(self):
        return self.ventas * 0.05


empleado1 = Programador("Ana", 30000)
empleado2 = Programador("Luis", 50000)
empleado3 = Comercial("Carlos",15000,30000)

empleados = [empleado1, empleado2, empleado3]

for empleado in empleados:
    print(empleado.calcular_bonus())

def analizar_empleados(empleados):
    total_bonus = 0
    mayor_bonus = None

    for empleado in empleados:
        if empleado.salario > total_bonus:
            bonus = empleado.calcular_bonus()

            total_bonus += bonus

            if mayor_bonus is None or bonus > mayor_bonus.calcular_bonus():
                    mayor_bonus = empleado


    return {"total_bonus": total_bonus, "mayor_bonus": mayor_bonus.nombre}

print(analizar_empleados(empleados))
