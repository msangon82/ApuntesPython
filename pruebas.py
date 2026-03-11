import json 

with open("Ej13_bis_Jason.json", "r") as archivo:
        agenda = json.load(archivo)
    
print (agenda)

# json.dump != json.dumps 

# en lugar de r utiliza w