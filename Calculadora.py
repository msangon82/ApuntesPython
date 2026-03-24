# Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números.
# Incluye un constructor que inicialice los dos números como atributos.

class Calculadora:
    def __init__(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2

    def suma(self):
        return self.numero1 + self.numero2
        
    def resta(self):
        return self.numero1 - self.numero2
    
    def multiplica (self):
        return self.numero1*self.numero2
    
    def divide(self):
        if self.numero2 != 0:
            return self.numero1/self.numero2
        else:
            print ("Error al dividir por 0")
    
