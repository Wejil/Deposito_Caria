# Classe base
class Animale:
    def __init__(self, nome):
        self.nome = nome
    
    def parla(self):
        print(f"{self.nome} fa suon generico.")

# Classe derivata (ereditata da Animale)
class Cane(Animale):
    def parla(self):
        print(f"{self.nome} abbaia!")

animale_generico = Animale("AnimaleGenercio")
cane = Cane("Fido")

animale_generico.parla()
cane.parla()