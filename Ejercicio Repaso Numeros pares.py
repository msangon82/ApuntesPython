# Crea una clase Numeros con un atributo que sea una lista de enteros.
# Incluye un método que devuelva solo los números pares de esa lista.

class Numeros:
    def __init__(self, lista):
        self.lista = lista

    def dame_pares(self):
        pares = []
        for num in self.lista:
            if num % 2 == 0:
                pares.append(num)
        return pares