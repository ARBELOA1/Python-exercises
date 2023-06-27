class MiClase:

    variable_clase = 'valor variable clase'

    def __init__(self, variable_instancia):

        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():  #Un metodo estatico solo recibe información de nuestra clase
                            #Pero no recibe objetos,atributos de instancia; esto deberia 
                            #usarse más que todo en métodos  lógicos que no necesitan 
                            #información adicional.
        
        print(MiClase.variable_clase)
    
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

MiClase.metodo_clase()
miObjeto1 = MiClase('valor variable instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

# MiClase.metodo_estatico()

# print(MiClase.variable_clase)

# miclase = MiClase('valor variable instancia')
# print(miclase.variable_instancia)
# print(miclase.variable_clase)

# MiClase.variable_clase2 = 'Valor variable clase 2'

# miclase2 = MiClase('Otro valor de variable instancia')
# print(miclase2.variable_instancia)
# print(miclase2.variable_clase)
# print(MiClase.variable_clase2)
# print(miclase.variable_clase2)
# print(miclase2.variable_clase2)

