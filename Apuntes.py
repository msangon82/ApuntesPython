#Vamos a ver como se importa un módulo 
import math
#hemos importado el módulo de math 
print(math.sqrt(100))

#también podemos importar solo una cosa del módulo math 
from math import sqrt
print(sqrt(100))    

#Tambien se pueden crear tus propios módulos para llamar funciones de otro sitio o módulos.

#Crea un generador de contraseñas seguras usando los modulos: 
# - ramdom 
# - string

import random 
import string 

contrasena =""

for i in range (10):
    caracter = string.ascii_letters + string.digits + string.punctuation
    contrasena = contrasena + random.choice(caracter)

print (contrasena)



