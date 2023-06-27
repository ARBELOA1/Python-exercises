# class Cubo:

#     def __init__(self,ancho,alto,profundo):

#         self.ancho = ancho
#         self.alto = alto
#         self.profundo = profundo

#     def calcularVolumen(self):
#         return self.ancho * self.alto * self.profundo

# ancho = float(input('Proporciona el ancho: '))
# alto = float(input('Proporciona el alto: '))
# profundo = float(input('Proporciona la profundidad: '))

# cubo = Cubo(ancho,alto,profundo)

# print(f'El volumen del cubo es de: {cubo.calcularVolumen():.1f}m³')

# import math


# class Billete():
#     def __init__(self, valor, cantidad):
#         self.valor = valor
#         self.cantidad = cantidad

#     def __repr__(self):
#         return "<__main__.Billete: valor = " +
#         str(self.valor)+ "; cantidad = " + int(self.cantidad) + ";>"


# papeles = 0
# dinero = 300
# entregado = []
# caja = []
# caja.append(Billete(500, 5))
# caja.append(Billete(200, 6))
# caja.append(Billete(100, 4))


# def entregarDinero():
#     global caja
#     global dinero
#     global entregado
#     for bi in caja:
#         if (dinero > 0):
#             div = math.floor(dinero / bi.valor)
#         if (div > bi.cantidad):
#             papeles = bi.cantidad
#         else:
#             papeles = div
#     entregado.append(Billete(bi.valor, papeles))
#     dinero = dinero - (bi.valor * papeles)


# entregarDinero()
# print(str(entregado[:]))

import math


class Billete():
    def __init__(self, valor, cantidad):
        self.valor = valor
        self.cantidad = cantidad

    def __repr__(self):
        return f"<__main__.Billete: valor = {self.valor}; cantidad = {self.cantidad};>" 
        
papeles = 0
dinero = 300
entregado = []
caja = []
caja.append(Billete(500, 5))
caja.append(Billete(200, 6))
caja.append(Billete(100, 4))


def entregarDinero():
    global caja
    global dinero
    global entregado
    for bi in caja:
        if (dinero > 0):
            div = math.floor(dinero / bi.valor)
        if (div > bi.cantidad):
            papeles = bi.cantidad
        else:
            papeles = div
    entregado.append(Billete(bi.valor, papeles))
    dinero = dinero - (bi.valor * papeles)


entregarDinero()
print(str(entregado[:]))

