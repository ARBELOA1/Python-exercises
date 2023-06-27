class Persona:

    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1  #Se crea un ID unico para cada persona u objeto 
                                    #que se cree
        return cls.contador_personas


    def __init__(self, nombre, edad):
         
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Santiago',19)
print(persona1)
persona2 = Persona('Juan',16)
print(persona2)
persona3 = Persona('María', 38)
print(persona3)
Persona.generar_siguiente_valor()#Aca se hace un salto en el contador,
                                #Por lo cual la persona 4 va ha incrementar en 1 su id
persona4 = Persona('Fabio', 48)
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')