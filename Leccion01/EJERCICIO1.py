#Ejercicio 1 (Valor 1.0): Realice un programa que permita crear un listado para cuentas y otro para tareas,
#en donde se especifique que el elemento guardo pertenece a una cuenta de ingreso o gasto o es una tarea.

# Juan Sebastian Hincapie Colorado
# Juan Pablo Ladino Betancur
# Jhonatan Pineda Carmona
# Santiago Arboleda Restrepo
# Jesus Maria Giraldo

import os
class program:

    ingreso = ''
    gasto = ''
    cuenta = []
    cuenta2 = []
    cuent = ''
    tipo = ''
    opcion = ''
    cuenta_Encontrar = 0
    tarea = []
    tarea2 = []
    total = 0
    total2 = 0
        
    def tipoDeCuenta(self):
        while True:
            print('\t.:BIENVENID@ AL CAJERO:.\n')
            print('\t1 Cuenta de Ingreso')
            print('\t2 Cuenta de Gasto')
            print('\tPresione 3 para salir\n')

            self.tipo = (input('Digite (1) ó (2) según sea la cuenta, ó (3) para salir: '))

            if self.tipo == '1':
                self.tareasCuenta1()
            elif self.tipo == '2':
                self.tareasCuenta2()
            elif self.tipo == '3':
                quit()
            
            input('Presione Enter para volver a ver el menú')
            os.system('cls')
        
        
    def proceso(self):

        self.cantidad = int(input('Digite cuantas cuentas va ha guardar: '))

        for self.i in range(1,self.cantidad+1):

            self.cuent = (input('Ingrese él número de la cuenta '+str(self.i)+': '))
            self.cuenta.append(self.cuent)
        
        self.tareasCuenta1()
    
    def procesocuent2(self):
        self.cantidad2 = int(input('Digite cuantas cuentas va ha guardar: '))

        for self.i in range(1,self.cantidad2+1):

            self.cuent2 = (input('Ingrese él número de la cuenta '+str(self.i)+': '))
            self.cuenta2.append(self.cuent2)
        self.tareasCuenta2()
    
    def tareasCuenta1(self):

        while True:
            self.imprimir()
            print('Desea realizar alguna de estas tareas? \n1 Consultar saldo\n2 Consignar\n\b'
            '3 Retirar saldo\n4 Crear cuentas\n0 salir')

            self.opcion = int(input('Ingresa la opción: '))
           

            if self.opcion == 1:
                self.cuenta_Encontrar = (input('Ingresa la cuenta a consultar: '))

                for self.j in range(len(self.cuenta)):
                    if self.cuenta_Encontrar == self.cuenta[self.j]:
                        print('Usted tiene un saldo de: {}'.format(self.total))
                    
            elif self.opcion == 2:
                while True:    
                    self.consignar = (input('Señor Usuario, ¿a que cuenta le quiere consignar? '
                    '\n\bSi quiere salirse, presione x \n'))

                    for self.k in range(len(self.cuenta)):
                        if self.consignar == self.cuenta[self.k]:
                            print(f'Su saldo actual es de: {self.total}')
                            self.ingreso= float(input('¿Cuanto dinero desea ingresar? \nRecuerde'
                            ' que puede depositar un máximo de 5 millones de pesos\n'))
                            if self.ingreso < 5000000:
                                self.total += self.ingreso
                                print(f'Este es tu nuevo saldo: {self.total}')
                                input('Presione Enter para volver a ver el menú')
                                os.system('cls')
                                return self.tareasCuenta1()
                            else:
                                print('Ha excedido el limite de consignación')
                                break
                            
                    
                        elif self.consignar == 'x':
                            return self.tareasCuenta1()
                    else:
                        print('La cuenta no esta registrada')
                    
            elif self.opcion == 3:
                while True:     
                    self.sacar = (input('Señor Usuario, ¿a que cuenta quiere retirar el saldo?: '
                        '\n\bSi quiere salirse, presione x \n'))
                    for self.l in range(len(self.cuenta)):
                        if self.sacar == self.cuenta[self.l]:
                            print(f'Su saldo actual es de: {self.total}')
                            self.egreso= float(input('¿Cuanto dinero deseas sacar?: '))
                            if self.egreso > self.total:
                                print('Su saldo es insuficiente, no se puede realizar ésta transacción')
                                
                            else:
                                self.total -= self.egreso
                                print(f'Este es tu nuevo saldo: {self.total}')
                                input('Presione Enter para volver a ver el menú')
                                os.system('cls')
                                return self.tareasCuenta1()
                        elif self.sacar == 'x':
                            return self.tareasCuenta1()

            elif self.opcion == 4:
                return self.proceso()

            elif self.opcion == 0:
                print()
                return self.tipoDeCuenta()

            input('Presione Enter para volver a ver el menú')
            os.system('cls')

    def tareasCuenta2(self):

        while True:
            self.imprimir()
            print('Desea realizar alguna de estas tareas? \n1 Consultar saldo\n2 Consignar\b\n'
            '3 Retirar saldo\n4 Crear cuentas\n0 salir')
            
            self.opcion = int(input('Ingresa la opción: '))
           
            if self.opcion == 1:
                self.cuenta_Encontrar2 = (input('Ingresa la cuenta a consultar: '))

                for self.j in range(len(self.cuenta2)):
                    if self.cuenta_Encontrar2 == self.cuenta2[self.j]:
                        print('Usted tiene un saldo de: {}'.format(self.total2))
                    
            elif self.opcion == 2:
                while True:    
                    self.consignar = (input('Señor Usuario, ¿a que cuenta le quiere consignar? '
                    '\n\bSi quiere salirse, presione x \n'))

                    for self.k in range(len(self.cuenta2)):
                        if self.consignar == self.cuenta2[self.k]:
                            print(f'Su saldo actual es de: {self.total2}')
                            self.ingreso= float(input('¿Cuanto dinero desea ingresar? \nRecuerde'
                            ' que puede depositar un máximo de 5 millones de pesos\n'))
                            if self.ingreso < 5000000:
                                self.total2 += self.ingreso
                                print(f'Este es tu nuevo saldo: {self.total2}')
                                input('Presione Enter para volver a ver el menú')
                                os.system('cls')
                                return self.tareasCuenta2()
                            else:
                                print('Ha excedido el limite de consignación')
                                break
                            
                    
                        elif self.consignar == 'x':
                            return self.tareasCuenta2()
                    else:
                        print('La cuenta no esta registrada')
                
            elif self.opcion == 3:
                while True:     
                    self.sacar = (input('Señor Usuario, ¿a que cuenta quiere retirar el saldo?: '
                        '\n\bSi quiere salirse, presione x \n'))
                    for self.l in range(len(self.cuenta2)):
                        if self.sacar == self.cuenta2[self.l]:
                            print(f'Su saldo actual es de: {self.total2}')
                            self.egreso= float(input('¿Cuanto dinero deseas sacar?: '))
                            if self.egreso > self.total2:
                                print('Su saldo es insuficiente, no se puede realizar ésta transacción')
                                
                            else:
                                self.total2 -= self.egreso
                                print(f'Este es tu nuevo saldo: {self.total2}')
                                input('Presione Enter para volver a ver el menú')
                                os.system('cls')
                                return self.tareasCuenta2()
                        elif self.sacar == 'x':
                            return self.tareasCuenta2()
            elif self.opcion == 4:
                return self.procesocuent2()
            
            elif self.opcion == 0:
                print()
                return self.tipoDeCuenta()

            input('Presione Enter para volver a ver el menú')
            os.system('cls')

    def imprimir(self):
        if self.tipo == '1':
            print(f'Estas son todas las cuentas de Ingreso: {self.cuenta}')
        elif self.tipo == '2':
            print(f'Estas son todas las cuentas de Gasto: {self.cuenta2}')
        

def run():
    todo = program()
    todo.tipoDeCuenta()

if __name__=="__main__":
    run()





