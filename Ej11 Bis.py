#Crea una clase Calculadora que reciba dos números.
#Haz los siguientes métodos: 
# - Un método apra sumar los dos números
# - Un método para restar los dos números
# - Al hacer print de un objeto Calculadora se imprimirán los dos números
# Añade Try-Except la entrada de datos 

class Calculadora: 

    def __ini__ (self,A,B):
        self.a = A
        self.b = B

        try: 
            type(A) == int or type(B) == int
        
        except:
            print ("No son numeros los datos introducidos")
        

    def sumar (self):
        if self.a >=100 or self.b >= 100:
            raise Exception

        try:
            suma = (self.a + self.b)
            print (suma)

        except Exception:
            print ("Los números son muy grandes")
        except: 
            print ("Los datos no son números")

    def restar (self): 
        resta = (self.a - self.b)
        return resta
    
    def __str__(self):
        return (f"Los números utilizados son {self.a} y {self.b}")
    
A = input (f"Introduce un numero para el primer valor:  ")
B = input (f"Introduce un numero para el segundo valor: ")

       
print (Calculadora.sumar())