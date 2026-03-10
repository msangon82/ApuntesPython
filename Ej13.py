# Crea un progrmaa que gestione una agenda de contactos USANDO DICCIONARIO donde: 
#  - La clave es el nombre de la persona 
#  - El valor es su número de teléfono (opción de meter otro diccionario con télefono y dirección).
# El progrma debe permitir: 
# - Añadir un contacto nuevo 
# - Buscar un contacto por nombre
# - Eliminar un contacto 
# - Mostar todos los contactos (quien quiera sufrir, qu elos devuelva ordenados alfabéticamente).

agenda = {
    "1":{"Nombre":"miguel","Telefono":"666999333","Direccion":"Rúa Montón, 2 - Ferrol"}, 
    "2":{"Nombre": "fina", "Telefono":"555333111", "Direccion":"Residencia Galatea - Ferrol"}
    }

while True:
    print(f"Está usted enel programa AGENDA. Seleccione una opción: ")
    print(f"1. Añadir un contacto.")
    print(f"2. Buscar un contacto por el nombre")
    print(f"3. Mostrar todos los contactos ordenados alfabeticamente")
    print(f"4. Salir del programa")
    opcion = int(input(""))

    if opcion == 1:
        print(f"Introduzca los datos de la persona que desea añadir: ")
        Nombre= input("Introduzca el nombre del contacto: ").lower()
        Telefono = input("Introduzca el telefono del usuario: ")
        Direccion = input("Introduzca la direccion del contacto: ")
        agenda[len(agenda)+1] =  { Nombre, Telefono, Direccion}

    elif opcion == 2: 
        contacto_buscar = input(f"Introduzca el nombre del contacto a buscar: ").lower()
        for i in range agenda[len(agenda)]

        print (agenda.get(contacto_buscar))

    elif opcion == 3:
        agenda_ordenada = sorted(agenda, key=lambda x: x)
        for contacto in agenda_ordenada:
            print(contacto)

    else:
        break





