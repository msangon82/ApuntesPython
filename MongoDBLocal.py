from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.errors import PyMongoError
clientelocal = MongoClient('mongodb://localhost:27017/')
db = clientelocal['mibase']                
collection = db['productos']
print (clientelocal.server_info())

try:
    
    for producto in collection.find ():
        print(producto)

except ConnectionFailure: 
    print(f"Error de conexión a MongodB")

# con hashlib se puede hashear la contraseña y así es más dificil descifrarla 

# Aquí vamos a crear una variable para introducir nuevos elementos en la base de dato

''' class producto:

    def __init__ (self, nombre, precio, stock):
         self.name = nombre
         self.precio = precio
         self.stock = stock
         
    def cambiar_precio(self, nuevo_precio):
         self.precio = nuevo_precio
    
producto1 = producto(producto[self.name ], producto[self.precio], producto[self.stock])''' 

while True:

        print("Seleccione una opcion: ")
        print("1 - Para introducir artículos.")
        print("2 - Para buscar un artículo")
        print("3 - Para actualizar productos")
        print("4 - Para eliminar un artículo")
        print("5 - Para salir del menú.")
        opcion = (int(input()))

        if opcion == 1:
            cantidad_productos = int(input("¿Cuantos productos quiere introducir?: "))

            productos_insertar = []

            for i in range (cantidad_productos):

                nombre = input("Indroduzca el nombre del producto: ").lower()
                precio = float(input("Introduzca el precio del produzco: "))
                stock = int(input("Introduzca el stock de productos: "))

                producto_nuevo = {"nombre": nombre, 
                "precio": precio,
                "stock": stock
                }

            productos_insertar.append(producto_nuevo)

            db.productos.insert_many(productos_insertar)

        elif opcion ==2: 
            
            articulo_buscar = input("Instroduzca el nombre del artículo: ").lower()
            articulos = db.productos.find({"nombre": articulo_buscar})

            for articulo in articulos: 
                 print(articulo)

        elif opcion == 3:
            articulo = input("¿Que articulo quiere actualizar? ").lower()
            precio = float(input("¿Que precio quiere introducir? "))
            db.productos.update_one({"nombre":articulo},{"$set":{"precio":precio}})


        elif opcion == 4:
             articulo = input("¿Que articulo quiere elimnar? ").lower()

             db.productos.delete_one({"nombre":articulo})


        elif opcion == 5:
             break
        

for producto in db.productos.find({},{"_id":0}):
    print (producto)

