# Crea un programa que gestione una agenda de contactos USANDO DICCIONARIO donde: 
#  - La clave es el nombre de la persona 
#  - El valor es su número de teléfono (opción de meter otro diccionario con télefono y dirección).
# El progrma debe permitir: 
# - Añadir un contacto nuevo 
# - Buscar un contacto por nombre
# - Eliminar un contacto 
# - Mostar todos los contactos (quien quiera sufrir, qu elos devuelva ordenados alfabéticamente).
import json

MiAgenda="Ej13_bis_Jason.json"

def cargar_agenda():
    with open(MiAgenda, "r") as agenda:
        archivo = json.load(agenda)
    return archivo

def guardar_agenda(archivo):
    with open(MiAgenda, "w") as agenda:
        json.dump(archivo, agenda, indent=4)

agenda = cargar_agenda()

guardar_agenda(agenda)

while True:
    print(f"Está usted en el programa AGENDA. Seleccione una opción: ")
    print(f"1. Añadir un contacto.")
    print(f"2. Buscar un contacto por el nombre")
    print(f"3. Mostrar todos los contactos ordenados alfabeticamente")
    print(f"4. Eliminar un contacto")
    print(f"5. Modificar un conctacto")
    print(f"6. Salir del programa")
    opcion = int(input(""))

    if opcion == 1:
        print(f"Introduzca los datos de la persona que desea añadir: ")
        Nombre= input("Introduzca el nombre del contacto: ").lower()
        Telefono = input("Introduzca el telefono del usuario: ")
        Direccion = input("Introduzca la direccion del contacto: ")
    
        MiAgenda[len(MiAgenda)+1] =  {
            "Nombre":Nombre,
            "Telefono":Telefono,
            "Direccion":Direccion
            }
        guardar_agenda(MiAgenda)
        print("Contacto añadido correctamente")

    elif opcion == 2: 
        contacto_buscar = input(f"Introduzca el nombre del contacto a buscar: ").lower()
        if contacto_buscar in MiAgenda:
            print(f"\nNombre:{contacto_buscar}")
            print(f"\nTelefono: {MiAgenda[key][contacto_buscar]["Telefono"]}")
            print(f"\nDireccion: {MiAgenda[key][contacto_buscar]["Direccion"]}")

        else:
            print("Contacto no encontrado")

    elif opcion == 3:
        if len(MiAgenda) == 0:
            print("La agenda está vacía")
        else:
            print("\nContactos ordenados alfabeticamente:")
            agenda_ordenada = sorted(agenda.values(), key=lambda x: x["Nombre"])
            for contacto in agenda_ordenada:
                print(f"Nombre: {contacto["Nombre"]}, Telefono: {contacto["Telefono"]}, Direccion: {contacto["Direccion"]}")
    
    elif opcion == 4: 
        nombre = input("Introduzca el contacto a eliminar: ").lower()
        try: 
            del MiAgenda[key]["Nombre"]
            print("Contacto eliminado")
        except: 
            print("El contacto no existe")
        guardar_agenda(MiAgenda)
    
    elif opcion == 5: 
        contacto_modificar = input("Introduzca el contacto a modificar: ").lower()
        if contacto_modificar in MiAgenda:
            print("Elija una opción")
            input("1. Modificar el nombre")
            input("2. Modificar el telefono")
            input("3. Modificar la direccion")
            input("4. Salir")
            opcion = int(input(""))
            if opcion == 1:
                nuevo_nombre=input("Introduzca el nuevo nombre")
                MiAgenda[contacto_modificar].update({Nombre:nuevo_nombre})
                guardar_agenda(MiAgenda)

            elif opcion == 2: 
                nuevo_telefono=input("Introduzca el nuevo telefono")
                MiAgenda[contacto_modificar].update({Telefono:nuevo_telefono})
                guardar_agenda(MiAgenda)                
            elif opcion == 3: 
                nueva_direccion=input("Introduzca la nueva direccion")
                MiAgenda[contacto_modificar].update({Direccion:nueva_direccion})
                guardar_agenda(MiAgenda)
            else:
                break
        else:
            print("Contacto no encontrado")
    
    else:
        break



            






