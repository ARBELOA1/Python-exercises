# # Ejercicio 5 (Valor 1.0): Hacer una funcion que le permita al usuario saber si una tarea esta en estado 
# # de por realizar, en ejecucion o terminada y con base al estado, mostrarle al usuario un mensaje de recordatorio 
# # especifico para cada estado de una tarea

# Para probar el funcionamiento de la funcion, se debe simular la visualizacion de un mensaje personalizado 
# dependiendo del estado de las tareas creadas por el usuario; para realizar esta labor, la funcion que debe 
# desarrollar debe permitir crear una tarea y asignarle un estado; al final, debe mostrar el mensaje correspondiente 
# al estado de dicha tarea.


# Juan Sebastian Hincapie Colorado
# Juan Pablo Ladino Betancur
# Jhonatan Pineda Carmona
# Santiago Arboleda Restrepo
# Jesus Maria Giraldo


# class verificación:
 
#     def __init__(self, cantidad):
#         self.amount = cantidad
    
#     def evalueWord(self):
#         state = ['Tarea por realizar', 'Tarea en ejecución', 'Tarea terminada']
#         i=0
#         for i in range(self.amount):
#             tarea =  input('Digite el nombre de la tarea: ')
#             estado = int(input('Digite el número en el que está el estado de la tarea... \n 0.Tarea por realizar \n 1.Tarea en ejecución \n 2.Tarea terminada \n Digita el número: '))
#             print(tarea, state[estado])

# usuario = verificación (int(input('Digite la cantidad de tareas: ')))
# usuario.evalueWord()

class program:
    def __init__(self,calcular,descuento):
        self.calcular = calcular
        self.descuento = descuento

    def cal(self):
        return self.calcular *  self.descuento 

calcular = float(input('Ingrese valor: '))
descuento = float(input('Ingrese descuento: '))

Program = program(calcular,descuento)

print(f'Este es el resultado del semestre con descuento: {Program.cal()}')


