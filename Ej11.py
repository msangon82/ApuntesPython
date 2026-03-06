#Cra una clase Calculadora que reciba dos números.
#Haz los siguientes métodos: 
# - Un método apra sumar los dos números
# - Un método para restar los dos números
# - Al hacer print de un objeto Calculadora se imprimirán los dos números 

class Calculadora: 

    def __ini__ (self,A,B):
        self.a = int (A)
        self.b = int (B) 

    def sumar (self): 
        suma = (self.a + self.b)
        return suma

    def restar (self): 
        resta = (self.a - self.b)
        return resta
    
    def multiplicar (self):
        multiplica = (self.a * self.b)
        return multiplica
    
    def dividir (self):
        divide = (self.a / self.b)
    
    def __str__(self):
        return f"Los números utilizados son {self.a} y {self.b}"
    

Operacion1 = Calculadora.sumar(2,3)
Operacion2 = Calculadora.restar(3,5)
        
print (Operacion1)