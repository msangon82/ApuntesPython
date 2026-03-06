# Crea una clase "Cuenta Bancaria" para hacer cuentas cuentas bancarias 
# El constructor tendrá en cuenta el nombre de  usuario y el saldo inicial.
# Añade métodos para: 
# - Retirar Dinero.
# - Ingresar Dinero.

class Cuenta_Bancaria:

    "los atributos de clase van fuera de los métodos"

    interes = 0.01
    comision_retirada = 1.5
    cantidad_clientes = 0

    def __init__ ( self, nickname, saldo_inicial):
        self.nombre = nickname
        self.saldo = saldo_inicial
        self.iban = self.numero_cuenta()
        Cuenta_Bancaria.cantidad_clientes += 1

    def Retirar_dinero(self, Saca_dinero):
        self.saldo -= (Saca_dinero + Cuenta_Bancaria.comision_retirada)
        return (self.saldo)

    def Ingresar_dinero(self, Ingresa_dinero):
        self.saldo += Ingresa_dinero
        return (self.saldo + Ingresa_dinero)
    
    def numero_cuenta (self):
        import random
        import string
        x = ""
        for i in range (20):
            x += str(random.randint(0, 9))
        return x
    
MiCuenta = Cuenta_Bancaria ("Santana", 10000)
OtraCuenta = Cuenta_Bancaria ("Otro tio", 500)
Cuenta_3 = Cuenta_Bancaria("Fulanito", 3000)
Cuenta_4 = Cuenta_Bancaria("Menganito", 20000)


print(f"La cuenta de {MiCuenta.nombre} tiene {MiCuenta.saldo} €\n El IBAN es {MiCuenta.iban}")

while True:
    print("BANCO SANTANA")
    print("Elija opción: ")
    print("1. Consultar datos")
    print("2. Retirar dinero")
    print("3. Ingresar dinero")
    print("4. Salir")
    print("5. ADMIN BANCO.- Modificar Comision")
    print("Otro numero. ¿Cuantas cuentas hay?")
    opcion = int(input("Introduzca opción: "))

    if opcion == 1: 
        print (f"Titular: {MiCuenta.nombre}\nSaldo: {MiCuenta.saldo}\nMi IBAN es {MiCuenta.iban}")
    elif opcion == 2: 
        x = (int(input("Introduce la cantidad de dinero a retirar de su cuenta: ")))
        MiCuenta.Retirar_dinero(x)
    elif opcion == 3: 
        y = (int(input("Introduce la cantidad de dinero a ingresar en su cuenta: ")))
        MiCuenta.Ingresar_dinero
    elif opcion == 4:
        break
    elif opcion ==5: 
        x = float(input("Instroduzca la nueva cantidad de interés de retirada: "))
        Cuenta_Bancaria.comision_retirada = x
    else:
        print (f"Hay {Cuenta_Bancaria.cantidad_clientes}")

""" 
Tipo_operacion = int(input("¿Que operación desea realizar?, ¿Sacar dinero o Ingresar Dinero?"))

if operacion == "Sacar dinero":
    Saca_dinero = (int(input("Introduce la cantidad de dinero a retirar de su cuenta: ")))
    Saca_dinero = Cuenta_Bancaria.Retirar_dinero(Saca_dinero)
    
elif operacion == "Ingresar dinero":
    Ingresa_dinero = (int(input("Introduce la cantidad de dinero a ingresar en su cuenta: ")))
    Ingresar_dinero = Cuenta_Bancaria.Ingresar_dinero(Ingresa_dinero)

else: 
        Opcion = (int(input("Para retirar dinero pulse 1 + enter, o pulse 2 + enter para ingresar dinero: ")))
if Opcion == 1: 
    Saca_dinero
elif Opcion == 2:
    Ingresa_dinero
else:
    print (f"Introduzca un valor valido \n{Opcion}") 

"""