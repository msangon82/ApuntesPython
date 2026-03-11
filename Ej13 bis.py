# Crea un progrmaa que gestione una agenda de contactos USANDO DICCIONARIO donde: 
#  - La clave es el nombre de la persona 
#  - El valor es su número de teléfono (opción de meter otro diccionario con télefono y dirección).
# El progrma debe permitir: 
# - Añadir un contacto nuevo 
# - Buscar un contacto por nombre
# - Eliminar un contacto 
# - Mostar todos los contactos (quien quiera sufrir, qu elos devuelva ordenados alfabéticamente).
import json 

with open("Ej13_bis_Jason.json", "r") as archivo:
        agenda = json.load(archivo)

while True:
    print(f"Está usted en el programa AGENDA. Seleccione una opción: ")
    print(f"1. Añadir un contacto.")
    print(f"2. Buscar un contacto por el nombre")
    print(f"3. Mostrar todos los contactos ordenados alfabeticamente")
    print(f"4. Eliminar un contacto")
    print(f"5. Salir del programa")
    opcion = int(input(""))

    if opcion == 1:
        print(f"Introduzca los datos de la persona que desea añadir: ")
        Nombre= input("Introduzca el nombre del contacto: ").lower()
        Telefono = input("Introduzca el telefono del usuario: ")
        Direccion = input("Introduzca la direccion del contacto: ")
        agenda[len(agenda)+1] =  { Nombre, Telefono, Direccion}

    elif opcion == 2: 
        contacto_buscar = input(f"Introduzca el nombre del contacto a buscar: ").lower()
        encontrado = False
        for key in agenda:
            if contacto_buscar == agenda[key]["Nombre"]:
                print(agenda[key])
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado")

    elif opcion == 3:
        agenda_ordenada = sorted(agenda.values(), key=lambda x: x["Nombre"])
        for contacto in agenda_ordenada:
          print(contacto)
    
    elif opcion == 4: 
        nombre = input("Introduzca el contacto a elimintar: ").lower()
        try: 
            del agenda[key]["Nombre"]
            print("Contacto eliminado")
        except: 
            print("El contacto no existe")

    else:
        break





