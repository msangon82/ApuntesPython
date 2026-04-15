"""
Crea una aplicación que calcule el Índice de Masa Corporal (IMC) de una persona. 

La aplicación debe pedir al usuario su peso en kilogramos y su altura en metros, 
y luego calcular el IMC usando la fórmula: IMC =PESO/(ALTURA)2

Debe mostrar el IMC con dos decimales.
"""

def Calcular_IMC (kg,m):
    IMC = round (kg /(m**2),2)
    
while True:
    try:
        peso = float(input("Introduce tu peso en kg: "))
        altura = float(input("Introduce tu altura en metros: "))
        print(f"Tu IMC es: {Calcular_IMC(peso, altura)}")
        break
    except ValueError:
        print("Por favor, introduce un número válido.")



