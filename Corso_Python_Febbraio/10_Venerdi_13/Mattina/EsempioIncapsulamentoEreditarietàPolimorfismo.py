# Incapsulamento
class ContoBancario:
    def __init__(self, saldo):
        self.__saldo = saldo  # Privato e non accessibile direttamente fuori dalla classe.

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Versamento eseguito. Nuovo saldo: {self.__saldo}")

    def get_saldo(self): # Getter, quindi unico modo "legale" per vedere il saldo.
        return self.__saldo

# Ereditarietà
class Veicolo:
    def __init__(self, marca):
        self.marca = marca

    def muoviti(self):
        print("Il veicolo si sta muovendo.")

class Moto(Veicolo): # "Moto" eredita da "Veicolo".
    def impenna(self):
        print(f"La {self.marca} sta impennando.")

# Polimorfismo
class Gatto:
    def fai_verso(self):
        return "Miao!"

class Cane:
    def fai_verso(self):
        return "Bau!"

# Una lista con oggetti diversi.
animali = [Gatto(), Cane(), Gatto()]

for animale in animali:
    # Non è importante se è un gatto o un cane, chiamando 'fai_verso' sa cosa fare.
    print(animale.fai_verso())