
import os
from time import sleep
cuenta = []
cuenta2 = []
class program(object):

    def __init__(self,cuentausuario,consignar,retiro,):

        #PARA LA CUENTA DE INGRESO
        self.cuentausuario = cuentausuario
        self.consignar     =   consignar
        self.retiro        = retiro
        self.saldo         = (consignar - retiro)
        self.detalle = []

    #-------------------------------------------------------------------------------------------------------------------
        
    #CUENTA1
    
    def registro(self):
            print('Esta es tu cuenta: {}\nSaldo de: {} '.format(self.cuentausuario,self.saldo))

    def transaccion(self,consignar,retiro):
        sald = self.saldo
        self.consignar = consignar
        self.retiro = retiro
        self.saldo = (sald + consignar - retiro)
        self.detalle = []
        print('Transacción Exitosa!!\n')

    def Consignacion(self):
   
        return('Ultima Consignación: {}\nSaldo Actual: {} '.format(self.consignar,self.saldo))

    def Retiro(self):

        return('Ultimo Retiro: {}\nSaldo Actual: {} '.format(self.retiro,self.saldo))


    #------------------------------------------------------------------------------------------------------------------

#MENU DE OPCIONES DEL CAJERO

def tipoDeCuenta():
    while True:
        print('.:BIENVENID@ AL CAJERO:.'.center(50,'.'))#Center para 
                                                        #centrar con 50 caracteres y 
                                                        #especificar el caracter '.'
        print('\t1 Cuenta de Ingreso')
        print('\t2 Cuenta de Gasto')
        print('\tPresione 3 para salir\n')

        tipo = (input('Digite (1) ó (2) 1según sea la cuenta, ó (3) para salir: '))

        if tipo == '1':
            tareasCuenta1()
        elif tipo == '2':
            tareasCuenta2()
        elif tipo == '3':
            quit()
        
        input('Presione Enter para volver a ver el menú')
        os.system('cls')
        tareasCuenta1()

#-----------------------------------------------------------------------------------------------------------------------

#PROCESOS CUENTA UNO (1,5,6)

def proceso():
  
    cuentausuario = int(input('Digite la cuenta: '))
    consignar = float(input('Saldo inicial: '))
    retiro = 0
    v = program(cuentausuario,consignar, retiro)
    cuenta.append(v)
    print(v.registro())
    input('Presione Enter para volver a ver el menú')
    os.system('cls')
    return tareasCuenta1()

        

def historial():
    
    print('Este es el historial de movimientos\n')
    cuentausuario = int(input('Digite el número de la cuenta: '))
    for v in cuenta:
        if cuentausuario == v.cuentausuario:
            for recepcionmensaje in v.detalle:
                print('Movimiento:\n{}'.format(recepcionmensaje))


def clientes():

    print('TODOS LOS CLIENTES REGISTRADOS HASTA EL MOMENTO\n')

    for v in cuenta:

            v.registro()

#-----------------------------------------------------------------------------------------------------------------------

#TAREAS DE CUENTA 1

def tareasCuenta1():

    while True:
       
        print('Desea realizar alguna de estas tareas? \n1 Crear cuenta\n2 Consultar saldo\n'
        '3 Consignar\n4 Retirar saldo\n5 Historial de Cuenta\n6 Listado de cuentas\n0 salir')

        opcion = int(input('Ingresa la opción: '))
        if opcion == 1:
            return proceso()

        if opcion == 2:
            cuentausuario = int(input('Ingresa la cuenta a consultar: '))

            for v in (cuenta):
                if cuentausuario == v.cuentausuario:
                    v.registro()
                
        elif opcion == 3:
            while True:    
                
                cuenta_Encontrar = int(input('Señor Usuario, ¿a que cuenta le quiere consignar? '
                '\n\bSi quiere salirse, presione 0 \n'))

                for v in (cuenta):
                    if cuenta_Encontrar == v.cuentausuario:
                        print(f'Su saldo actual es de: {v.saldo}')
                        consignar = float(input('¿Cuanto dinero desea ingresar? \nRecuerde'
                        ' que puede depositar un máximo de 5 millones de pesos\n'))
                        retiro = 0
                        if consignar < 5000000:
                            print('Consignacion en proceso, espero un momento porfavor...')
                            sleep(3)
                            v.transaccion(consignar,retiro)
                            v.registro()
                            recepcionmensaje = v.Consignacion()
                            v.detalle.append(recepcionmensaje)
                            input('Presione Enter para volver a ver el menú')
                            os.system('cls')
                            return tareasCuenta1()

                        else:
                            print('Ha excedido el limite de consignación')
                            
                        
                
                    elif cuenta_Encontrar == 0:
                        return tareasCuenta1()
                else:
                    print('La cuenta no esta registrada')
                
        elif opcion == 4:
            while True:     
                sacar = int(input('Señor Usuario, ¿a que cuenta quiere retirar el saldo?: '
                    '\n\bSi quiere salirse, presione 0 \n'))
                for v in cuenta:
                    if sacar == v.cuentausuario:
                        print(f'Su saldo actual es de: {v.saldo}')
                        retiro = float(input('¿Cuanto dinero deseas sacar?: '))
                        consignar = 0
                        v.transaccion(consignar,retiro)
                        v.registro()
                        recepcionmensaje = v.Retiro()
                        v.detalle.append(recepcionmensaje)
                        input('Presione Enter para volver a ver el menú')
                        os.system('cls')
                        return tareasCuenta1()

                    elif sacar == 0:
                        return tareasCuenta1()

        elif opcion == 5:
            historial()

        elif opcion == 6:
            clientes()

        elif opcion == 0:
            print()
            return tipoDeCuenta()

        input('Presione Enter para volver a ver el menú')
        os.system('cls')

#-----------------------------------------------------------------------------------------------------------------------

class program2(object):

    def __init__(self,cuentausuario2,consignar2,retiro2):

 #PARA LA CUENTA DE GASTO
        self.cuentausuario2 = cuentausuario2
        self.consignar2     = consignar2
        self.retiro2        = retiro2
        self.saldo2         = (consignar2 - retiro2)
        self.detalle2 = []

#-----------------------------------------------------------------------------------------------------------------------

 #CUENTA2

    def registro2(self):
        print('Esta es tu cuenta: {}\nSaldo de: {} '.format(self.cuentausuario2,self.saldo2))

    def transaccion2(self,consignar2,retiro2):
        sald2 = self.saldo2
        self.consignar2 = consignar2
        self.retiro2 = retiro2
        self.saldo2 = (sald2 + consignar2 - retiro2)
        self.detalle2 = []
        print('Transacción Exitosa!!\n')

    def Consignacion2(self):
   
        return('Ultima Consignación: {}\nSaldo Actual: {} '.format(self.consignar2,self.saldo2))

    def Retiro2(self):

        return('Ultimo Retiro: {}\nSaldo Actual: {} '.format(self.retiro2,self.saldo2))

#-----------------------------------------------------------------------------------------------------------------------

#PROCESOS CUENTA DOS (1,5,6)

def procesocuent2():

    cuentausuario2 = int(input('Digite la cuenta: '))
    consignar2 = float(input('Saldo inicial: '))
    retiro2 = 0
    vii = program2(cuentausuario2,consignar2, retiro2)
    cuenta2.append(vii)
    print(vii.registro2())
    input('Presione Enter para volver a ver el menú')
    os.system('cls')
    tareasCuenta2()

def historialCuenta2():
    
    print('Este es el historial de movimientos\n')
    cuentausuario2 = int(input('Digite el número de la cuenta: '))
    for vii in cuenta2:
        if cuentausuario2 == vii.cuentausuario2:
            for recepcionmensaje2 in vii.detalle2:
                print('Movimiento:\n{}'.format(recepcionmensaje2))


def clientesDeCuenta2():

    print('TODOS LOS CLIENTES REGISTRADOS HASTA EL MOMENTO\n')

    for vii in cuenta2:

            vii.registro2()



def tareasCuenta2():

    while True:
       
        print('Desea realizar alguna de estas tareas? \n1 Crear cuenta\n2 Consultar saldo\n'
        '3 Consignar\n4 Retirar saldo\n5 Historial de Cuenta\n6 Listado de cuentas\n0 salir')

        opcion = int(input('Ingresa la opción: '))
        if opcion == 1:
            return procesocuent2()

        if opcion == 2:
            cuentausuario = int(input('Ingresa la cuenta a consultar: '))

            for vii in (cuenta2):
                if cuentausuario == vii.cuentausuario2:
                    vii.registro2()
                
        elif opcion == 3:
            while True:    
                
                cuenta_Encontrar = int(input('Señor Usuario, ¿a que cuenta le quiere consignar? '
                '\n\bSi quiere salirse, presione 0 \n'))

                for vii in (cuenta2):
                    if cuenta_Encontrar == vii.cuentausuario2:
                        print(f'Su saldo actual es de: {vii.saldo2}')
                        consignar2 = float(input('¿Cuanto dinero desea ingresar? \nRecuerde'
                        ' que puede depositar un máximo de 5 millones de pesos\n'))
                        retiro2 = 0
                        if consignar2 < 5000000:
                            
                            vii.transaccion2(consignar2,retiro2)
                            vii.registro2()
                            recepcionmensaje2 = vii.Consignacion2()
                            vii.detalle2.append(recepcionmensaje2)
                            input('Presione Enter para volver a ver el menú')
                            os.system('cls')
                            return tareasCuenta2()

                        else:
                            print('Ha excedido el limite de consignación')
                            
                        
                
                    elif cuenta_Encontrar == 0:
                        return tareasCuenta2()
                else:
                    print('La cuenta no esta registrada')
                
        elif opcion == 4:
            while True:     
                sacar = int(input('Señor Usuario, ¿a que cuenta quiere retirar el saldo?: '
                    '\n\bSi quiere salirse, presione 0 \n'))
                for vii in cuenta2:
                    if sacar == vii.cuentausuario2:
                        print(f'Su saldo actual es de: {vii.saldo2}')
                        retiro2 = float(input('¿Cuanto dinero deseas sacar?: '))
                        consignar2 = 0
                        vii.transaccion2(consignar2,retiro2)
                        vii.registro2()
                        recepcionmensaje2 = vii.Retiro2()
                        vii.detalle2.append(recepcionmensaje2)
                        input('Presione Enter para volver a ver el menú')
                        os.system('cls')
                        return tareasCuenta2()

                    elif sacar == 0:
                        return tareasCuenta2()

        elif opcion == 5:
            historialCuenta2()

        elif opcion == 6:
            clientesDeCuenta2()

        elif opcion == 0:
            print()
            return tipoDeCuenta()

        input('Presione Enter para volver a ver el menú')
        os.system('cls')


if __name__=="__main__":
    tipoDeCuenta()





