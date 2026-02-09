# Creazione di una classe
class Automobile: # Dichiaro una classe
    numero_di_ruote = 4 # Attributo di classe. Non è negli init, poiché non è una cosa unica: tutte le macchine devono avere per forza 4 ruote. Non serve quindi metterlo negli init.
    def __init__(self, marca, modello): # Metodo costruttore
        self.marca = marca # Attributo di istanza
        self.modello = modello # Attributo di istanza
    def stampa_info(self): # Metodo di istanza
        print("L'automobile è una", self.marca, self.modello)


class Persona(): # Classe vuota. Per definizione la classe ha il costruttore intrinseco.
    pass

# mirko = Persona()
mirko_OBJ = Persona()
print(mirko_OBJ.x)

# Tipi base
print(type(10)) # int
print(type(3.14)) # float
print(type("test")) # str
print(type([1, 2])) # list

# Tipi non basilari
class MioOggetto:
    pass
obj = MioOggetto()
print(type(obj)) # Il nome della classe definisce il tipo dell'oggetto.

auto1 = Automobile("Fiat", "500") # Crea un oggetto di un'automobile
auto2 = Automobile("BMW", "X3") # Crea un oggetto di un'automobile

auto1.stampa_info() # Stampa l'automobile 1
auto2.stampa_info() # Stampa l'automobile 2

# Metodo statico
class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b
# Uso del metodo statico senza creare un'istanza.
risultato = Calcolatrice.somma(5, 3)
print(risultato) # Output: 8.

# Class method
class Contatore:
    numero_istanze = 0 # Attributo di classe
    def __init__(self):
        Contatore.numero_istanze += 1
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")
# Creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()
Contatore.mostra_numero_istanze() # Output: Sono state create 2 istanze.