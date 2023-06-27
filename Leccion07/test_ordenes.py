from Producto import Producto
from Orden import  Orden

producto1 = Producto('Camisa',100.000)
producto2 = Producto('Pantalón', 80.000)
producto3 = Producto('Medias',30.000)
producto4 = Producto('Gorra', 50.000)

productos1 = [producto1, producto2]
productos2 = [producto3,producto4]
orden1 = Orden(productos1)
orden1.agregar_producto(producto3)#Agrego un nuevo producto a mi clase Orden
orden1.agregar_producto(producto4)
print(orden1)
print(f'Total de la orden 1: {orden1.calcular_total()}\n')
orden2 = Orden(productos2)
print(orden2)
print(f'Total de la orden 2: {orden2.calcular_total()}')