class figuraGeometrica:

    def __init__(self,ancho,alto):

        if self._rango_(ancho):
            self._ancho = ancho
        
        else:
            self._ancho = 0
            print('El valor de ancho sobrepasa el rango')
        
        if self._rango_(alto):
            self._alto = alto
        else:
            self._alto = 0
            print('El valor de alto sobrepasa el rango')

    @property   
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho

    @property   
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self,alto):
        self._alto = alto
    
    def __str__(self) -> str:
        return f'Este es el ancho {self._ancho} y este es el alto {self._alto}'

    def _rango_(self, valor):   

        return True if 0 < valor < 10 else False
        