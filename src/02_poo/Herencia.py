class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(self.nombre, self.salario)


class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        # aquí tienes que reutilizar nombre y salario
        super().__init__(nombre,salario)
        # y además guardar lenguaje
        self.lenguaje = lenguaje

    def mostrar_info(self):
        # mostrar nombre, salario y lenguaje
        print(self.nombre, self.salario, self.lenguaje)

programador1 = Programador("Dani", 22000, "Python")
programador1.mostrar_info()