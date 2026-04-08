# Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa. 
# Utiliza un constructor para introducir la temperatura base. 

class ConversorTemperatura:

    def __init__(self, base):
        self_temperatura = base 
        base = int(input("f/ Introduce la temperatura base: "))
        return self_temperatura

    def celcius(self, self_temperatura):
        convertir_C = (self_temperatura / 33,8)
        return convertir_C
    
    def Fahrenheit(self, self_temperatura):
        convertir_F = (self_temperatura * 33.8)
        return convertir_F
