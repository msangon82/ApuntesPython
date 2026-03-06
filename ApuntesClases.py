#Una clase es hacerme mis datos a mi medida. 
nombre = "Antonio"
edad = 36 
empleo = "SGT1"

antonio = ["Antonio", 36, "SGT1"]

#Una clase es una estructura, es un molde.
#Una clase equivale a la generalizaicón de un tipo específico de objetos. Una 
#clase es una plantilla que define las variables y los métodos que son comunes
#para todos los objetos de un cierto tipo. La clase define los atributos (datos)
#de un objeto y sus operaciones o métodos (comportamiento).

#En Python están prohibidas las clases vacías.

#Se recomienda que las classes se enumeren con mayúsculas 
# y las variables en minúsculas (PEP 8)

class Persona: 
    pass 

antonio = Persona ()
jaime = Persona ()
ruben = Persona ()

print (type(antonio))

class Personas: 
    def __init__(self, name, age, rank, guapo=True):
        self.nombre = name 
        self.edad = age 
        self.empleo = rank
    
    def correr (self):
        print (f"{self.nombre} está corriendo")

    def saludar(): 
        print("Mano al botón")
    
    def cumpleanos (self):
        self.edad += 1
        print(f"Feliz Cumple {self.nombre} por tu {self.edad} cumpleaños")


antonio = Personas ("Antonio", 36, "SGT1")

ruben = Personas ("Ruben", 44, "SGT1")

ruben.correr()

Personas.saludar()

print (ruben.nombre)

ruben.cumpleanos()
ruben.cumpleanos()
ruben.cumpleanos()
ruben.cumpleanos()



