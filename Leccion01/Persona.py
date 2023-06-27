# #EJEMPLO1

# # class Persona:
# #     def __init__(self, nombre, edad):
# #         self.nombre = nombre
# #         self.edad = edad

# #     def desplegar(self):
# #         print(f'Nombre: {self.nombre}, Edad: {self.edad}')


# # persona1 = Persona('Juan', 28)
# # persona1.desplegar()
# # persona2 = Persona('Karla', 30)
# # persona2.desplegar()

# """EJEMPLO 2"""

# # class Persona:
# #     def __init__(self, nombre, apellido, edad):
# #         self.nombre = 'Juan'
# #         self.apellido = 'Perez'
# #         self.edad = 28

# # persona1 = Persona()
# # print(persona1.nombre)
# # print(persona1.apellido)
# # print(persona1.edad)

# """EJEMPLO 3"""

# # class Persona:
# #     def __init__(self, nombre, apellido, edad):
# #         self.nombre = nombre
# #         self.apellido = apellido
# #         self.edad = edad

# # persona1 = Persona('Juan', 'Perez', 28)
# # print(persona1.nombre)
# # print(persona1.apellido)
# # print(persona1.edad)

# """EJEMPLO 4"""

# # class Persona:
# #     def __init__(self, nombre, apellido, edad):
# #         self.nombre = nombre
# #         self.apellido = apellido
# #         self.edad = edad

# # persona1 = Persona('Juan', 'Perez', 28)
# # print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# # persona2 = Persona('Karla', 'Gomez', 30)
# # print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

# """EJEMPLO 5"""

# class Persona:
#     def __init__(self, nombre, apellido, edad, *valores, **terminos):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.valores = valores
#         self.terminos = terminos

#     def mostrarDetalle(self):
#         print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

# persona1 = Persona('Juan', 'Perez', 28, '3117958113', 2, 3, 5, m = 'Manzan', p = 'Pera')
# #print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
# persona1.mostrarDetalle()

# persona2 = Persona('Karla', 'Gomez', 30)
# #print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
# persona2.mostrarDetalle()

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre   #El guion bajo indica que el atributo esta encapsulado y no
                                #deberia ser usado fuera de la clase; si quiero restringir este atributo para 
                                # que solo se utilice dentro de la clase, utilizo (__) doble guión bajo.
        self._apellido = apellido
        self._edad = edad
    
    #METODO GET

    #METODO SET

    @property
    def nombre(self):
        print('Llamando método GET nombre')
        return self._nombre 

    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método SET nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Llamando método GET apellido')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        print('Llamando método GET edad')
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self):

        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':

    persona1 = Persona('Juan', 'Perez', 28)
    # print(persona1.nombre)
    persona1.nombre = 'Juancho'
    # print(persona1.nombre)
    persona1.apellido = 'Arboleda'
    persona1.edad = 19
    persona1.mostrarDetalle()
    # persona1._nombre= 'Santiago Arboleda'
    # persona1.mostrarDetalle()

    print(__name__)


