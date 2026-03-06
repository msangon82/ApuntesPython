# Haz un videojuego usando clases
# Hay la clase Personaje que tiene nombre, vida y una función de ataque.
# El jugador y el enemigo son Personaje y atacan por turnos
# Gana quien deje la vida del otro a 0. 

import random

ataque = random.randint (1,15)

class Personaje: 
    def __init__(self, nick, life):
        self.nombre = nick 
        self.vida =  life 
    
    def atacar (self):
        return (ataque)

jugador = Personaje("Santanita", 50)
enemigo = Personaje("EnemigoMalo", 20)
    
def enemigo_ataca ():
        while   enemigo.vida > 0:
            enemigo.vida -= jugador.atacar()

        else: 
            print (f"Tu {jugador.nombre} ha muerto") 
            print ("Has ganado.")
        
        return("Vida enemigo:", "#"*enemigo.vida)

def jugador_ataca ():
        while   jugador.vida > 0:
            jugador.vida -= enemigo.atacar()

        else:   
            print (f"{enemigo.nombre}te ha matado") 
            print ("Has perdido.")
        
        return("Vida jugador:", "#"*jugador.vida)

atacantes = [jugador_ataca, enemigo_ataca]  

print (random.choice(atacantes))

