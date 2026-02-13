# Definizione di chi sono le persone che entrano in azienda.
from abc import ABC, abstractmethod

# Astrazione
class Dipendente(ABC):  # Col metodo dell'astrazione si crea una classe base astratta, poiché non esiste una "persona" generica, ma solo dipendenti reali.
    def __init__(self, nome, cognome, badge_id):
        self.nome = nome
        self.cognome = cognome
        self.__badge_id = badge_id  # Incapsulamento. Essendo che il badge_it è privato, nessuno deve poterlo scambiare all'esterno, dunque metodo dell'incapsulamento.
    
    def get_badge(self):
        return self.__badge_id

    @abstractmethod # Metodo astratto. Ogni tipo di dipendente avrà un livello di accesso diverso.
    def livello_accesso(self):
        pass

    def descrizione(self):
        return f"{self.nome} {self.cognome} (Badge: {self.__badge_id})"

# Ereditarietà. Creazione di utenti specifici che estendono la classe padre Dipendente.
class Operaio(Dipendente):
    def livello_accesso(self):
        # Polimorfismo: l'operaio risponde a modo suo.
        return "Accesso standard: produzione e mensa."

class Manager(Dipendente):
    def livello_accesso(self):
        # Polimorfismo. Manager "risponde" con permessi più alti dell'operaio.
        return "Accesso totale: produzione, mensa, uffici e server."