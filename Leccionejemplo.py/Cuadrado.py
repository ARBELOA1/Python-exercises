from figuraGeometrica import figuraGeometrica
from Color import Color

class Cuadrado(figuraGeometrica,Color):

    def __init__(self, lado, color):

        figuraGeometrica.__init__(self,lado, lado)
        Color.__init__(self,color)

    def operacion(self):

        return self.ancho * self.alto

    def __str__(self) -> str:
        return f'Cuadrado: [{figuraGeometrica.__str__(self)}] Color: [{Color.__str__(self)}]'