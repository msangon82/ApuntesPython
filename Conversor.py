# Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa. 
# Utiliza un constructor para introducir la temperatura base. 

class ConversorTemperatura:

    def __init__(self, base):
        self.temperatura = base 
    
    def celsius (self):
        convertir_C = (self.temperatura * 9/5) + 32
        return convertir_C
      
    
    def fahrenheit(self):
        convertir_F = (self.temperatura - 32) * 5/9
        return convertir_F
       
# Ejemplo de uso
convierte_c = ConversorTemperatura(20)   # 20°C
print("Celsius a Fahrenheit:", ConversorTemperatura.celsius())
convierte_f = ConversorTemperatura(68)   # 68°F
print("Fahrenheit a Celsius:", ConversorTemperatura.fahrenheit())