from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):

    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())

    if isinstance(objeto, Gerente):# con este metodo podemos preguntar si cierto objeto
        print(objeto.departamento)#corresponde a la instancia o construtor de la clase, si
                                # no corresponde será falso o dara error, si es verdadero 
                                #Entonces imprimirá el argumento que se le dio.

empleado = Empleado('Juan',5000)
imprimir_detalles(empleado)

gerente = Gerente('Maria',6000,'Sistemas')
imprimir_detalles(gerente)