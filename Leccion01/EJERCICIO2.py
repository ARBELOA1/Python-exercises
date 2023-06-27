# Ejercicio 2 (Valor 1.0): Codifique una funcion que permita calcular el estado las finanzas personales 
# con base en los listados de cuentas de ingresos y gastos, en donde se pueda detallar si el estado financiero 
# es saludable (no se tienen deficits) o si por el contrario las finanzas son negativas 
# (los gastos son mayores a los ingresos).


# Juan Sebastian Hincapie Colorado
# Juan Pablo Ladino Betancur
# Jhonatan Pineda Carmona
# Santiago Arboleda Restrepo
# Jesus Maria Giraldo

class Estado:
    cuenta = 0
    contadoringresos = 1
    contadorgastos = 1
    Ingresos = 0
    Gastos = 0
    Diferencia = 0

    def CapturarIngresos(self):
        self.CantidadIngresos = int(input("¿Cuántos ingresos tuviste? "))
        for self.i in range (1,self.CantidadIngresos+1):
            self.ingreso = float(input("Ingresa por favor el ingreso "+str(self.i)+": "))
            self.contadoringresos +=1
            self.Ingresos +=   self.ingreso
        print(f"El total de ingresos es {self.Ingresos:.2f}")
        self.CapturarGastos()
        self.CalcularEstado()
            
        
    def CapturarGastos(self):   
        self.CantidadGastos = int(input("¿Cuántos gastos tuviste? "))
        for self.i in range (1,self.CantidadGastos+1):
            self.gasto = float(input("Ingresa por favor el gasto "+str(self.i)+": "))
            self.contadorgastos +=1
            self.Gastos +=   self.gasto
        print(f"El total de los gastos es {self.Gastos:.2f}")

    def CalcularEstado(self):
        self.Diferencia = self.Ingresos - self.Gastos
        if self.Ingresos < self.Gastos:
            print("El estado de tus finanzas tiene deficit negativo\nY tu saldo actual es de ",self.Diferencia)
        elif self.Ingresos > self.Gastos:
            print("El estado de tus finanzas es positivo\nY tu saldo actual es de ",self.Diferencia)
        else: 
            self.Ingresos == self.Gastos
            print("El estado de tus finanzas es normal\nY tu saldo actual es de ",self.Diferencia)
        


def run():
    Capturaringresos = Estado()
    Capturaringresos.CapturarIngresos()

if __name__ == "__main__":
    run()