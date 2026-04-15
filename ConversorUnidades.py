"""
Escribe un programa que convierta una cantidad dde metros a kilómetros, centímetros y milímetros. 
La función debe recibir lacantidad de metros como parámetro y devolver un 
dicceionario con las conversiones. 

Contempla validar que la entrada sea un número positivo.
"""

def convertir_metros(metros):
    if metros < 0:
        return "Error: La cantidad de metros debe ser un número positivo."
    
    conversiones = {
        "kilometros": metros / 1000,
        "centimetros": metros * 100,
        "milimetros": metros * 1000
    }
    
    return conversiones 

# Ejemplo de uso
cantidad_metros = 1500      
conversiones = convertir_metros(cantidad_metros)
print(conversiones) 