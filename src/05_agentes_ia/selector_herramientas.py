
class HerramientaClima:
    def obtener_clima(self, ciudad):
        return {
            "ciudad": ciudad,
            "temperatura": 22,
            "estado": "Soleado"
        }


class HerramientaCalculadora:
    def sumar(self, a, b):
        return a + b

    def multiplicar(self, a, b):
        return a * b

    def restar(self, a, b):
        return a - b

clima = HerramientaClima()
calculadora = HerramientaCalculadora()



def seleccionar_herramienta(peticion):
    peticion = peticion.lower()

    if "temperatura" in peticion or "clima" in peticion:
        return "obtener_clima"

    elif "multiplica" in peticion:
        return "multiplicar"

    elif "sumar" in peticion:
        return "sumar"

    elif "restar" in peticion:
        return "restar"

    else:
        return "Herramienta no encontrada"


def ejecutar_herramienta(herramienta, a, b):
    if herramienta == "sumar":
        return calculadora.sumar(a, b)

    elif herramienta == "multiplicar":
        return calculadora.multiplicar(a, b)

    elif herramienta == "restar":
        return calculadora.restar(a, b)

    else:
        return "Herramienta no disponible"



herramienta = seleccionar_herramienta("Quiero sumar dos números")
resultado = ejecutar_herramienta(herramienta, 10, 5)
print(resultado)

herramienta = seleccionar_herramienta("Multiplica 10 por 5")
resultado = ejecutar_herramienta(herramienta, 10, 5)
print(resultado)  # 50

herramienta = seleccionar_herramienta("Quiero restar dos números")
resultado = ejecutar_herramienta(herramienta, 10, 5)
print(resultado)





