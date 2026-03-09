# Crea una clase Kart.
# Cada kart tendrá un piloto, una velocidad máxima y una aceleración.
# Haz métodos para: 
# - Acelerar, que subirá la velocidad el valor de la aceleración.
# - Frenar, que reducirá la velocidad el valor de aceleración.
# - Mostrar datos, que devolverá que el piloto X va a velocidad Y 
# Añade manejo de excepciones para evitar pasar de las velocidades máximas.

class Kart: 

    def __init__ (self, pilot, vel_max, acelerate, vel_ini):
        self.piloto = pilot
        self.max_vel = vel_max
        self.aceleration = acelerate
        self.v0 = vel_ini

    def acelerar (self):
        try:
            aceleratekart = (self.v0 + self.aceleration)
            if aceleratekart > self.max_vel:
                aceleratekart = self.max_vel
            else:
                aceleratekart = aceleratekart
            self.v0 = aceleratekart
            return aceleratekart
        except Exception:
            print(f"Los datos introducidos no son números")
             
    def frenar (self, frenado):
        self.freno = frenado
        decelerate = (self.v0 - self.freno)
        if self.freno >= self.v0: 
            decelerate = 0
        else:
            return decelerate
       
    
    def show_data (self):
        print (f"El Kart del piloto {self.piloto} circula a una velocidad de {self.v0} km/h")
    
Mario = Kart("Mario", 120, 20, 5)

print (Mario.acelerar())
print (Mario.frenar(5))
Mario.show_data()
    

    

       



