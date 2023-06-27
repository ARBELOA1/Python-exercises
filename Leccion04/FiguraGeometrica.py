#ABC = Abstract Base Class

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
        if  self._validar_valor(ancho): # Valida si el número ingresado esta en el rango
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
        if self._validar_valor(alto):
            self._alto  = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self,alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')
    
    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self) -> str:
        return f'Este es el ancho {self._ancho} y este es el alto {self._alto}'
    
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False

