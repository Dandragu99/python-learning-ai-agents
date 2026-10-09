class HerramientaClima:
    def __init__(self):
        # Aquí más adelante podría contener la api key
        pass

    def obtener_clima(self, ciudad):
        return {
            "ciudad": ciudad,
            "temperatura": 22,
            "estado": "Soleado"
        }

    def obtener_prevision(self, ciudad):
        return {
            "ciudad": ciudad,
            "manana": "Nublado",
            "temperatura": 18
        }

#HerramientaClima es una clase.
#obtener_clima() es una capacidad de esa clase.
#Si le pasas "Madrid", devuelve unos datos simulados.

class AgenteViajes:
    def __init__(self, nombre, herramienta_clima, herramienta_restaurante, herramienta_hoteles):
        self.nombre = nombre
        self.herramienta_clima = herramienta_clima
        self.herramienta_restaurante = herramienta_restaurante
        self.herramienta_hoteles = herramienta_hoteles
        self.herramientas = {
            "clima": self.consultar_clima,
            "prevision": self.consultar_prevision,
            "restaurantes": self.buscar_restaurantes,
            "hoteles": self.buscar_hoteles
        }

    def consultar_clima(self, ciudad):
        resultado = self.herramienta_clima.obtener_clima(ciudad)

        return {
            "agente": self.nombre,
            "clima": resultado
        }

    def consultar_prevision(self, ciudad):
        resultado = self.herramienta_clima.obtener_prevision(ciudad)
        return {
            "agente":self.nombre,
            "prevision": resultado
        }

    def buscar_restaurantes(self, ciudad):
        resultado = self.herramienta_restaurante.buscar_restaurantes(ciudad)

        return {
            "agente": self.nombre,
            "restaurantes": resultado
        }

    def buscar_hoteles(self, ciudad):
        # El agente utiliza la herramienta de hoteles.
        resultado = self.herramienta_hoteles.buscar_hoteles(ciudad)

        return {
            "agente": self.nombre,
            "hoteles": resultado
        }

    def procesar_peticion(self, accion, ciudad):
        herramienta = self.herramientas.get(accion)

        if herramienta is None:
            return {
                "error": "No sé qué herramienta utilizar"
            }

        return herramienta(ciudad)


class HerramientaRestaurantes:
    def buscar_restaurantes(self, ciudad):
        return {
            "ciudad": ciudad,
            "restaurantes": [
                "Casa Paco",
                "La Plaza",
                "El Centro"
            ]
        }

class HerramientaHoteles:
    def buscar_hoteles(self, ciudad):
        return {
            "ciudad": ciudad,
            "hoteles": [
                "Hotel Central",
                "Gran Plaza",
                "Madrid Suites"
            ]
        }

clima_tool = HerramientaClima()
restaurantes_tool = HerramientaRestaurantes()
hoteles_tool = HerramientaHoteles()

agente = AgenteViajes(
    "Agente de viajes",
    clima_tool,
    restaurantes_tool,
    hoteles_tool
)

print(agente.procesar_peticion("clima", "Madrid"))
print(agente.procesar_peticion("restaurantes", "Barcelona"))
print(agente.procesar_peticion("hoteles", "Valencia"))