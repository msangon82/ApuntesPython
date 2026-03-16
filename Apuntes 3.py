class Persona:
    def __init__(self):
        self.pelo ="Moreno"
        self.__sexualidad= "Hetero"
        #Si lo escribimos entre 4 barras bajas declaramos el atributo como privado.

    # getters son metodos para saltar la privacidad del atributo. 
    def getSexualidad(self):
        return self.__sexualidad 
    # setters son metodos para modificar la privacidad del atributo.
    def setSexualidad(self, sex):
        self.__sexualidad = sex

Antonio = Persona()

print (Antonio.pelo)

Antonio.pelo = "Rubio"

print (Antonio.pelo)

class Animal: 
    def __init__(self):
        pass

class Perro(Animal):
    def __init__(self):
        pass

class Militar(Persona): 
    def __init__(self):
        pass

#Herencia y Polimorfios (para investigar por nuestra cuenta). 

