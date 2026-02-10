'''Il sistema deve includere una classe Pacco con: codice (stringa), peso (numero) e stato (es. "in magazzino", "in consegna", "consegnato"), con un metodo per mostrare le info e un metodo per cambiare stato.
Deve esserci una classe Magazzino che contiene una lista (o dizionario) di pacchi e permette di aggiungere un pacco, cercarlo per codice, e mostrare tutti i pacchi in un certo stato.
Deve esserci infine una classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”, segnare un pacco come “consegnato” e calcolare il peso totale dei pacchi ancora non consegnati.
Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, cambia lo stato di alcuni pacchi (almeno una consegna avviata e una consegna completata) e stampa: elenco pacchi “in magazzino”, elenco pacchi “in consegna” e il peso totale dei pacchi non ancora consegnati.'''

class Pacco:                            # Classe che rappresenta un pacco.
    def __init__(self, codice, peso):   # Costruttore, inizializza un pacco. Parametri: codice (identificativo del pacco, stringa); peso (peso del pacco in kg, numero).
        self.codice = codice            # Codice identificativo del pacco.
        self.peso = peso                # Peso in kg, ad es. 4.5.
        self.stato = "in magazzino"     # Stato iniziale.
    
    def mostra_info(self):  # Mostra e stampa tutte le informazioni del pacco.
        print(f"Codice: {self.codice}.")
        print(f"Peso: {self.peso} kg.")
        print(f"Stato: {self.stato}.")
    
    def cambia_stato(self, nuovo_stato):    # Cambia lo stato del pacco. Parametri: nuovo_stato (il nuovo stato, stringa).
        self.stato = nuovo_stato            # Cambia l'attributo self.stato e stampa la conferma.
        print(f"Pacco {self.codice}: stato cambiato in '{nuovo_stato}'")
    
class Magazzino:                # Classe che gestisce una collezione di pacchi.
    def __init__(self, nome):   # Costruttore, inizializza il magazzino. Parametri: nome (nome del magazzino).
        self.nome = nome        # Nome del magazzino
        self.pacchi = []        # Lista vuota di pacchi.
    
    def aggiungi_pacco(self, pacco):    # Aggiunge un pacco al magazzino. Parametri: pacco (oggetto di tipo Pacco).
        self.pacchi.append(pacco)       # Oggetto di tipo Pacco. Aggiunge il pacco alla lista self.pacchi.
        print(f"Pacco {pacco.codice} aggiunto al magazzino")
    
    def cerca_pacco(self, codice):      # Cerca un pacco per codice. Parametri: codice (codice del pacco da cercare) e restituisce oggetto "Pacco" se trovato, altrimenti None.
        for pacco in self.pacchi:
            if pacco.codice == codice:
                return pacco            # Se trovato, restituisce l'oggetto Pacco.
        return None                     # Pacco non trovato.
    
    def mostra_pacchi_per_stato(self, stato):           # Mostra tutti i pacchi in un certo stato. Parametri: stato, lo stato da cercare (per esempio "in magazzino").
        print(f"Pacchi con stato: '{stato}'")
        pacchi_trovati = []                             # Salva i pacchi in una lista temporanea
        for pacco in self.pacchi:
            if pacco.stato == stato:
                pacchi_trovati.append(pacco)
        if len(pacchi_trovati) == 0:
            print(f"Nessun pacco con stato '{stato}'")
        else:
            for pacco in pacchi_trovati:
                pacco.mostra_info()
        print(f"Totale: {len(pacchi_trovati)} pacchi")  # Stampa tutti i pacchi.

class GestorePacchi:                # Classe che gestisce le operazioni sui pacchi.
    def __init__(self, magazzino):  # Costruttore, inizializza il gestore. Parametri: magazzino (oggetto di tipo Magazzino).
        self.magazzino = magazzino

    def avvia_consegna(self, codice):   # Mette un pacco in consegna. Parametri: codice (codice del pacco).
        pacco = self.magazzino.cerca_pacco(codice)
        if pacco is None:               # is None controlla se una variabile è None. Se True, non trovato. False, se trovato.
            print(f"Pacco {codice} non trovato.")
        else:
            pacco.cambia_stato("In consegna.")
    
    def segna_consegnato(self, codice): # Segna un pacco come consegnato. Parametri: codice (codice del pacco). Uguale a avvia_consegna, ma cambia stato in "consegnato".
        pacco = self.magazzino.cerca_pacco(codice)
        if pacco is None:
            print(f"Pacco {codice} non trovato.")
        else:
            pacco.cambia_stato("consegnato")

    def calcola_peso_non_consegnati(self):  # Calcola il peso totale dei pacchi non ancora consegnati. Restituisce il peso totale in kg.
        peso_totale = 0
        for pacco in self.magazzino.pacchi:
            if pacco.stato != "consegnato":
                peso_totale += pacco.peso
        return peso_totale

# Programma principale.
print("Sistema gestione pacchi.")

# Crea il magazzinio.
magazzino = Magazzino("Magazzino Centrale")
print(f"{magazzino.nome} creato.")

gestore = GestorePacchi(magazzino)  # Crea il gestore pacchi.
print("Gestore pacchi attivo.")

# Crea almeno 5 pacchi. Tutti hanno come stato = "in magazzino".
pacco1 = Pacco("PACKAGE01", 5.5)
pacco2 = Pacco("PACKAGE02", 3.2)
pacco3 = Pacco("PACKAGE03", 8.0)
pacco4 = Pacco("PACKAGE04", 2.1)
pacco5 = Pacco("PACKAGE05", 10.5)

# Inserisci i pacchi nel magazzino.
magazzino.aggiungi_pacco(pacco1)
magazzino.aggiungi_pacco(pacco2)
magazzino.aggiungi_pacco(pacco3)
magazzino.aggiungi_pacco(pacco4)
magazzino.aggiungi_pacco(pacco5)

# Gestione consegne e avvia alcune consegne.
print("Avvio consegne: ")
gestore.avvia_consegna("PACKAGE01")
gestore.avvia_consegna("PACKAGE03")

print("Segno pacchi consegnati: ")      # Segna alcuni pacchi come consegnati
gestore.segna_consegnato("PACKAGE01")

magazzino.mostra_pacchi_per_stato("in magazzino")       # Mostra pacchi "in magazzino".
magazzino.mostra_pacchi_per_stato("in consegna")        # Mostra pacchi "in consegna".
magazzino.mostra_pacchi_per_stato("consegnato")         # Mostra pacchi "consegnato".

peso_totale = gestore.calcola_peso_non_consegnati()     # Calcola peso totale dei pacchi non consegnati.
print(f"Peso totale pacchi non consegnati: {peso_totale} kg.")