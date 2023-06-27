
from Calculadora import Calculadora, Resta
from Calculadora import Suma


opcion = str(input('¿Que operación desea hacer?: '))
num1 = int(input('Ingresa el número 1: '))
num2 = int(input('Ingresa el número 2: '))
calculadora1= Calculadora(num1,num2)
print(calculadora1)

if opcion == '+':

    Suma1 = Suma(num1,num2)
    
    
    print(Suma1)
    
else:
    Resta1 = Resta(num1,num2)
    print(Resta1)