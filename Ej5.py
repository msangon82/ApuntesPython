#Haz una calculadora de edad exacta (años, meses, días)

import datetime 

fecha_hoy = (datetime.date.today())
print (fecha_hoy)


dd = int(input("Introduce el día de tu fecha de nacimiento: "))
mm = int(input("Introduce el mes de tu fecha de nacimiento: "))
yyyy = int(input("Introduce el año de tu fecha de nacimiento: "))
fecha_nacimiento = datetime.date (yyyy, mm, dd)

numero_dias = fecha_hoy - fecha_nacimiento

dias = int(numero_dias%30)
meses = int(numero_dias/30)

meses_anos = int(meses%12 )
anos = int(meses_anos/12)

print("Tienes", dias, "días,", meses_anos, "meses y", anos, "años")
