# Ejercicio 3 (Valor 1.0): Hacer una funcion que le permita al usuario configurar el tiempo de cada tarea de su listado 
# de tareas utilizando como base la tecnica Pomodoro; tenga en cuenta que esta tecnica consiste en asignar el tiempo
#  a una tarea de aproximadamente 25 minutos, seguido de un descanso de aproximadamente 5 minutos; 
# luego de repetir este ciclo 4 veces, se toma un descanso más largo de aproximadamente 20 a 30 minutos y se inicia 
# nuevamente el proceso.

# Juan Sebastian Hincapie Colorado
# Juan Pablo Ladino Betancur
# Jhonatan Pineda Carmona
# Santiago Arboleda Restrepo
# Jesus Maria Giraldo

from time import sleep, time

import os
class TIEMPO:

    Tareas = ['1 Tarea de Estaditica','2 leer un libro']
    configuracion = []

    def tareas(self):
        while True:

            print('¿Qué tarea quiere modificar? ')
            print(self.Tareas)
            self.elección = int(input())

            if self.elección == 1:
                self.pausa = input('¿Cuántas descansos quiere hacer en esta tarea? ')
                self.tiempo = int(input("¿Cuánto tiempo desea asignar a cada tarea? "))
                self.opcion = int(input('¿Cuánto tiempo en segundos quiere asignarle a cada descanso? '))
                sleep(self.opcion)
                self.configuracion.append(self.pausa)
                print("Tiempo configurado exitosamente")

            elif self.elección == 2:
                self.pausa2 = int(input("¿Cuántas descansos quiere hacer en esta tarea? "))
                self.tiempo2 = int(input("¿Cuánto tiempo desea asignar a cada tarea? "))
                self.opcion2 = int(input("¿Cuánto tiempo en segundos quiere asignarle a cada descanso? "))
                sleep(self.opcion2)
                print("Tiempo configurado exitosamente")

            else:
                print("Opción seleccionada no valida")
            
            input('Presione Enter para volver a ver el menú')
            os.system('cls')
        
def run():
    tiempo = TIEMPO()
    tiempo.tareas()
    

if __name__ == "__main__":
    run()