from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
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
