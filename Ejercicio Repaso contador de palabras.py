# Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
# Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.

def contador():
    texto = str(input("Introduce el texto a contabilizar:      "))
    palabras = texto.split()
    return len(palabras)

class Texto:
    def __init__ (self, miTexto):
        self.texto = miTexto

    def contador(self):
        return contador(self.texto)


print (contador())



