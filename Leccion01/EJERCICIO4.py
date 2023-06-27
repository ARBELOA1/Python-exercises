# Ejercicio 4 (Valor 1.0): Realizar la programacion de una funcion que permita simular un solo ciclo de tareas
#  utilizando la tecnica Pomodoro, en el cual se asignen las tareas a realizar con sus respectivos descansos.


# Juan Sebastian Hincapie Colorado
# Juan Pablo Ladino Betancur
# Jhonatan Pineda Carmona
# Santiago Arboleda Restrepo
# Jesus Maria Giraldo

from time import sleep, time

class TIEMPO:

    Tareas = ['1 Parcial de Estaditica','2 leer un libro']

    def tareas(self):
        while True:
            
            print('¿Qué tarea quiere modificar? ')
            print(self.Tareas)
            self.elección = int(input())

            if self.elección == 1:
                self.pausa = int(input('¿Cuántas descansos quiere hacer en esta tarea? '))
                self.tiempo = int(input("¿Cuánto tiempo desea asignar a cada sesión? "))
                self.opcion = int(input('¿Cuánto tiempo en segundos quiere asignarle a cada descanso? '))
                print("Tiempo configurado exitosamente")
                for self.j in range (1,self.pausa+1):
                    print('\tDesarrollando ejercicio de Estadistica...\n\tSesión'+str(self.j)+"\n")
                    sleep(self.tiempo)
                    print("\tDescansando...\n\tDescanso "+str(self.j)+"\n\n")
                    sleep(self.opcion)
                print('Parcial finalizado.')
           

            elif self.elección == 2:
                self.pausa2 = int(input("¿Cuántas descansos quiere hacer en esta tarea? "))
                self.tiempo2 = int(input("¿Cuánto tiempo desea asignar a cada sesión? "))
                self.opcion2 = int(input("¿Cuánto tiempo en segundos quiere asignarle a cada descanso? "))
                print("Tiempo configurado exitosamente")
                for self.i in range (1,self.pausa2+1):
                    print("\tLeyendo libro...\n\tSesión "+str(self.i)+"\n")
                    sleep(self.tiempo2)
                    print("\tDescansando...\n\tDescanso "+str(self.i)+"\n\n")
                    sleep(self.opcion2)
                print("Lectura del libro finalizada.")
            else:
                print("Opción seleccionada no valida")
            
    
        
    
        
def run():
    tiempo = TIEMPO()
    tiempo.tareas()
    

if __name__ == "__main__":
    run()