import thinker
class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar,restar,etc
    """
    def __init__(self,operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB
    
    def potencia(self):
        return self.operandoA ** self.operandoB

# aritmetica1 = Aritmetica(3,2)
# print(f'Suma: {aritmetica1.sumar()}')
# print(f'Resta: {aritmetica1.restar()}')
# print(f'Multiplicación: {aritmetica1.multiplicar()}')
# print(f'División: {aritmetica1.dividir():.2f}')
# print(f'Potencia: {aritmetica1.potencia()}')

import pyautogui as pg
import time

pg.hotkey('win','r')
pg.typewrite('https://youtu.be/NE6pANWJGuU?t=20\n')
pg.typewrite('k')
pg.hotkey('win','r')
pg.typewrite('notepad\n')
time.sleep(1)
pg.typewrite("I wouldn't try to throw myself away\n")
time.sleep(5)
pg.typewrite("If you asked me, I'd say\n")



