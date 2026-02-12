class umano():
    def cammina(self):
        print("sto camminando sue due zampe")

class struzzo():
    def cammina(self):
        print("sto camminando sue due zampe")

u = umano()
s = struzzo()

def cammina(elemento: object):
    elemento.cammina()
# Andrà bene sia struzzo che umano poiché sono entrambi degli oggetti.

# Esempio
class Cane:
    def parla(self):
        return "Bau!"
class Gatto:
    def parla(self):
        return "Miao!"

def fai_parlare(animale):
    print(animale.parla())  # Non importa di che tipo sia l'animale.
cane = Cane()
gatto = Gatto()

fai_parlare(cane)   # Output: Bau!
fai_parlare(gatto)  # Output: Miao!