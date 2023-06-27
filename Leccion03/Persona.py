class Persona(object):
    def __init__(self,nombre,edad):

        self.nombre = nombre
        self.edad   = edad

    def __str__(self):
        return f'Person[Name: {self.nombre}, age: {self.edad}]'

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad) 

        self.sueldo = sueldo

    def __str__(self):
        return f'employee[Salary: {self.sueldo}] {super().__str__()} '