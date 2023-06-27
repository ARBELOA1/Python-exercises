class Calculadora:

    def __init__(self,num1,num2):

        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f'Estos son los números a sumar:[{self.num1} y {self.num2}]'

class Suma(Calculadora):

    def __init__(self, num1, num2):
        super().__init__(num1, num2)

        self.suma = self.num1 + self.num2

    def __str__(self):
        return f'La suma de los dos números es de: {self.suma}'

class Resta(Calculadora):

    def __init__(self, num1, num2):
        super().__init__(num1, num2)

        self.resta = self.num1 - self.num2

    def __str__(self):
        return f'La resta de los dos números es de: {self.resta}'

class Multiplicacion(Calculadora):

    def __init__(self, num1, num2):
        super().__init__(num1, num2)

        self.multiplicacion = self.num1 * self.num2

    def __str__(self):
        return f'La multiplicación de los dos números es de: {self.multiplicacion}'

class Division(Calculadora):

    def __init__(self, num1, num2):
        super().__init__(num1, num2)

        self.division = self.num1 / self.num2

    def __str__(self):
        return f'La división de los dos números es de: {self.division}'