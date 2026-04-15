class Estudiante:
    def __init__(self, name, age, calification):
        self.__nombre = name
        self.__edad = age
        self.__calificacion = float(calification)
    
    def get_age(self):
        return self.__edad

    def set_nombre(self, name):
        self.__nombre = name
        return self.__nombre
    
    
    def resultado (self):
        if self.__calificacion >= 5:
            print ("Aprobado")
        elif self.__calificacion < 5:
            print ("Suspenso")
        else: 
            print ("Debe introducir una calificación númerica")






    
