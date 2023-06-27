class Persona:

    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self,other):
        return f'{self.edad - other.edad}'

persona1 = Persona('Luis',28)
persona2 = Persona('Santiago',19)
print(persona1 + persona2)
print(persona1 - persona2)

# obj1 + obj2
# obj1.__add__(obj2) Esto es lo mismo que arriba
