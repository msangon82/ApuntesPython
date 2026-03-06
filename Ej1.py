def Calcular_IMC (kg,m):
    IMC = round (kg /(m**2),2)
    
    if IMC < 18.5: 
        return { "Tipo":"Bajo peso", 
                "Valor":IMC
                }
    elif IMC >= 18.5  and IMC < 25:
        return ("Normal")
    elif IMC >= 25  and IMC <= 30:
        return ("Sobrepeso")
    else:
        return ("Obesidad")

# tipo, valor = Calcular_IMC(80, 180)
# print (f"Tiene un IMC{tipo} con un valor de {round (valor, 2)}")

print (f"Su IMC es {Calcular_IMC(80,1.180)[0]} con un valor de {Calcular_IMC(80,1.80)[1]}")

print (Calcular_IMC(80, 1.80))

integrer = 5
flotante = 5.5
cadena = "Hola Mundo"
booleano = True
lista = [1,2,3]
tupla= (1,2,3) #La tupla no se puede modificar
diccionario = {"clave":"valor"}



