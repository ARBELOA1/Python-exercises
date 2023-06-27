class Vehiculo:

    def __init__(self,color,ruedas):

        self.color  = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehicle[color: {self.color}, wheel: {self.ruedas}]'
    
class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)

        self.velocidad = velocidad

    def __str__(self):
        return f'Car[Speed: {self.velocidad}Km/hr] {super().__str__()}'

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)

        self.tipo = tipo
    
    def __str__(self):
        return f'Bike[type: {self.tipo}] {super().__str__()}'