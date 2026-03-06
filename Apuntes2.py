#Una fecha en Python no es un tipo de dato propio, pero podemos importar
#un módulo nombrado para trabajar con fechas como fecha objetos.

import datetime

x = datetime.datetime.now ()
print (x)


#Cuando ejecutamos el código desde el ejemplo nos devolverá 
#Año, mes, día, hora, minuto, segundo y microsegundo. 
#Tiene mucho metodos de devolver información sobre un objeto. 

import datetime 
x=datetime.datetime.now ()

print(x.year)
print(x.strftime("%A")) #%A es para que escriba el nombre de la semana completo.


#Para crear una fecha, podemos utilizar la clase datetime del módulo datetime.
import datetime

x= datetime.datetime(2026,2,25)

print (x)

#El objeto tiene un método para formatear objetos date en cadenas legibles
#El método se llama, y toma un parámetro, para especificar el formato de la 
#cadena devuelta: strftime() format

import datetime 

x = datetime.datetime (2026, 2, 25)

print (x.strftime("%B")) #%B es para que escriba el nombre del mes completo.




#