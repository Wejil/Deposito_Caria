'''
Creare una classe base MembroSquadra e una Squadra che conterrà le diverse classi figlie che rappresentano ruoli specifici all'interno della squadra di calcio,
come Giocatore, Allenatore e Assistente.

Classe MembroSquadra:

Attributi:
nome (stringa)
età (intero)
Metodi:
descrivi() (stampa una descrizione generale del membro della squadra)
Classi Derivate:

Giocatore:

Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team

Crea due squadre e falle giocare contro.
'''

import random   # Per simulare il punteggio della partita.

class MembroSquadra:    # Classe base.
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def descrivi(self):
        return f"{self.nome}, {self.eta} anni"

class Giocatore(MembroSquadra):                             # Classi derivate (ereditarietà).
    def __init__(self, nome, eta, ruolo, numero_maglia):    # Passiamo solo nome ed età alla classe base (2 argomenti + self)
        super().__init__(nome, eta)                         # Richiama il costruttore del padre.
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    def descrivi(self):                 # Si sovrascrive il metodo descrivi per aggiungere informazioni specifiche
        info_base = super().descrivi()  # Si richiama super().descrivi() per ottenere la parte comune (Nome, Età) e poi si attaccano le informazioni extra.
        return f"[Giocatore] {info_base} | Ruolo: {self.ruolo} | N°: {self.numero_maglia}"
    
class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, modulo_preferito):
        super().__init__(nome, eta)
        self.modulo_preferito = modulo_preferito
    
    def descrivi(self):
        return f"[Allenatore] {super().descrivi()} | Modulo: {self.modulo_preferito}"

class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specialita):
        super().__init__(nome, eta)
        self.specialita = specialita
    
    def descrivi(self):
        return f"[Assistente] {super().descrivi()} | Specialità: {self.specialita}"

class Squadra:              # Classe squadra, non eredita da nessuno poiché il suo compito è quello di contenere una lista di oggetti.
    def __init__(self, nome_squadra):
        self.nome_squadra = nome_squadra
        self.membri = []    # Lista che conterrà oggetti Giocatore, Allenatore, ...
    
    def aggiungi_membro(self, membro):
        self.membri.append(membro)
    
    def mostra_formazione(self):
        print(f"Formazione {self.nome_squadra}")
        for m in self.membri:   # Ciclo for per descrivere con descrivi() ognuno della lista.
            print(m.descrivi())

def gioca_partita(squadra1, squadra2):  # Funzione partita esterna che mette in relazione due istanze diverse.
    print(f"Inizio partita: {squadra1.nome_squadra} vs {squadra2.nome_squadra}")
    gol1 = random.randint(0, 5)         # Simulazione punteggio casuale
    gol2 = random.randint(0, 5)
    print(f"Risultato finale: {squadra1.nome_squadra} {gol1} - {gol2} {squadra2.nome_squadra}")

    if gol1 > gol2:
        print(f"Vincitore: {squadra1.nome_squadra}")
    elif gol2 > gol1:
        print(f"Vincitore: {squadra2.nome_squadra}")
    else:
        print("Pareggio.")
    
# Partita.
team_a = Squadra("Juventus")    # Squadra A
team_a.aggiungi_membro(Allenatore("Luciano Spalletti", 66, "4-3-3"))
team_a.aggiungi_membro(Giocatore("Yildiz", 20, "Attaccante", 10))
team_a.aggiungi_membro(Assistente("Luigi", 30, "Fisioterapista"))

team_b = Squadra("Roma")    # Squadra B
team_b.aggiungi_membro(Allenatore("Gianpiero Gasperini", 68, "4-3-3"))
team_b.aggiungi_membro(Giocatore("Dybala", 32, "Attaccante", 21))

# Esecuzione.
team_a.mostra_formazione()
team_b.mostra_formazione()
gioca_partita(team_a, team_b)