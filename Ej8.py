#Crea una clase Pokedex para llevar un registro de pokemon capturados.
#Los pokemon tendran nombre, tipo, nivel y si estan capturados o no.
#Habra un contador del numero de pokemon capturados y otro de vistos.
#Crea un método para capturar un pokemon. El método tendrá en cuenta que la 
#probabilidad de captura de un pokemon es del 40%.

class pokemon:

    pokemon_vistos = 0
    pokemon_capturados = 0

    def __init__(self, nick, tipoPokemon, level,):
        self.nombre = nick
        self.tipo = tipoPokemon
        self.nivel = level
        self.captura = False 
    
    def captura_pokemon(self):
        print (f"Pulsa 1 para lanzar la Pokeball")
        opcion = int(input(f"Lanza la Pokeball"))
        if opcion == 1: 
            import random
            print(f"Lanzando la pokeball")
            Probabilidad = [1,2,3,4,5,6,7,8,9,10]
            y = [random.choice(Probabilidad)]
            if  y <= 4:          
                x = random.choice(POKEDEX)
                if x.captura == True:
                    print(f"Has capturado a {x.nombre}, tienes {pokemon.pokemon_capturados} pokemons. Enhorabuena!")
                    pokemon.pokemon_capturados += 1
               
            else: 
                print (f"Lo siento mucho has fallado y no has capturado a {x.nombre}, tienes {pokemon.pokemon_capturados} pokemons.")
                

             
pikachu = pokemon ("Pikachu", "Electrico", 100)
charmander = pokemon ("Charmander", "Fuego", 80,)
squirtle = pokemon ("Squirtle", "Agua", 75,)
eevee = pokemon ("Eevee", "Normal", 83, )
mewtwo = pokemon ("Mewtwo", "Psíquico", 92,)
POKEDEX = [pikachu, charmander, squirtle, eevee, mewtwo]
print(pikachu.nombre, charmander.nombre, squirtle.nombre, eevee.nombre, mewtwo.nombre)

while True:
    pokemon.captura_pokemon











