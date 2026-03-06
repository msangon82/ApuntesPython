#Ejercicio 3 puntos
#Crea una función llamada generar_lista que reciba un número y haga una lista de los números impares hasta ese número. 
#Al final imprimirá por pantalla losnúmero en una sola línea separados por el caracter "|"(AltGr +1)

def generar_lista (numero):
    lista_impares = []

    for i in range (1, numero +1, 2): #La estructura for i in range() en Python se utiliza para repetir un bloque de código un número específico de veces. range()
       lista_impares.append (i)

    return lista_impares

for i in generar_lista:

    numero = int(input()) #Aquí introducimos el numero de la variable generar_lista
    resultado = generar_lista(numero) #Aquí creamos la variable resultado  para llamarla luego con la función print 


print (resultado, end='|')

# SSL Stripping (Hackear una red wifi)
# Delorean (1000 días al futuro)
# Se evita utilizando una VPN 

