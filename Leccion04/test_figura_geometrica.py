from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

#No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print(f'Creación objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado= 5, color= 'black')
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'Cálculo de area de cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print()

print(f'Creación objeto Cuadrado'.center(50,'-'))
Rectangulo1 = Rectangulo(ancho = 5,alto =9, color ='Green')
print(f'Cálculo de area de rectángulo: {Rectangulo1.calcular_area()}')
print(Rectangulo1)


#MRO - Method Resolution Order
#print(Cuadrado.mro())