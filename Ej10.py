#Haz una clase dado que simule el lanzamiento de un dado de caras (moneda).
#Modificalo para introducir el número de caras al instanciar la clase.

import random

class dado: 
    def __init__(self, caras):
        self.caras = caras

    def lanzar(self):
        lanzamiento = random.randint(1,self.caras)
        return lanzamiento
    
    def __str__ (self):
        return f"El resultado ha sido {self.lanzar()}"

moneda=dado(2)
d4 = dado(4)
d6 = dado(6)
d8 = dado(8)
d10 = dado (10)
d12 = dado (12)

dadoRaro = dado(random.randint (1,6))

print(d6)

print(f"Tu dado de mierda tiene {dadoRaro.caras} caras y salió un {dadoRaro}")
