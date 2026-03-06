#Crea un programa que genere un numero aleatorio del 1 al 100. Le pida al usuario que introduzca numero, y le diga que si el numero es mas alto o mas bajo.
#En un numero de intentos predeterminado. 

import random 
numero_oculto = random.randint(1,100)
print(numero_oculto)


print ("Adivina el número del 1 al 100")
print ("Tienes 7 intentos")

for intento in range(7):

    numero_usuario  = int(input("Introduce un número: "))

    if numero_usuario ==numero_oculto:
        print= ("¡Has acertado!")
        break

    else: 
        if numero_usuario < numero_oculto:
            print("El número es más alto")
        else: 
            print("El número es más bajo")

    print ("Te quedan", 6 - intento,"intentos")

print("El numero era ", numero_oculto)