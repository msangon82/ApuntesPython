# Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
# Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.

def contador():
    texto = str(input("Introduce el texto a contabilizar:      "))
    palabras = len(texto)
    return palabras

class Texto:
    def __init__ (self):
        self.texto = str(input("Introduce el texto a contabilizar: "))

    def contardor(self):
        palabras = len(self.texto)
        return palabras