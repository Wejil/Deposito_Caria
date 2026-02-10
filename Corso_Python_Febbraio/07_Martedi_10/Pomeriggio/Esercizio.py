''' Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che produce e vende vari tipi di prodotti.
Gli studenti dovranno creare una classe base chiamata prodotto e diverse classi parallele che rappresentano diversi tipi di prodotti.
Inoltre, dovranno creare una classe Fabbrica che gestisce l'inventario e le vendite dei prodotti.
1. Classe Prodotto:
- Attributi:
nome (stringa che descrive il nome del prodotto)
costo_produzione (costo per produrre il prodotto)
prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
- Metodi:
calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
2. Classi parallele:
- Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
- Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
3. Classe Fabbrica:
- Attributi:
inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
- Metodi:
aggiungi_prodotto: aggiunge prodotti all'inventario.
vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.'''

# Classe padre che contiene le caratteristiche che tutti i prodotti della fabbrica hanno in comune.
class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    def calcola_profitto(self): # Semplice sottrazione tra quanto incassiamo e quanto abbiamo speso. Che erediteranno Elettronica e Abbigliamento.
        return self.prezzo_vendita - self.costo_produzione
    
# Classi figlie che ereditano da "Prodotto", aggiungendo dettagli specifici.
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)    # super().__init__ chiama il costruttore della casa padre.
        self.garanzia = garanzia                                    # Attributo specifico: mesi di garanzia.

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)    # Prima di aggiungere la garanzia o il materiale, dice al prodotto di andare dal Padre per fargli impostare nome, costo e prezzo.
        self.materiale = materiale                                  # Attributo specifico: tipo di tessuto.

# Classe fabbrica. La chiave sarà il nome del prodotto e il valore un piccolo dizionario contenente l'oggetto e la quantità.
class Fabbrica:
    def __init__(self):
        self.inventario = {}        # Inventario: { "Nome": {"oggetto":obj, "quantità": int} }. Permette di accedere ai dati velocemente.
    
    def aggiungi_prodotto(self, prodotto_obj, quantita):
        nome = prodotto_obj.nome
        if nome in self.inventario: # Se esiste già, si aumenta solo la quantità.
            self.inventario[nome]["quantita"] += quantita
        else:                       # Se è nuovo, si crea la voce nel dizionario.
            self.inventario[nome] = {"oggetto": prodotto_obj, "quantita": quantita}
        print(f"Aggiungi {quantita} pezzi di '{nome}' in inventario.")
    
    def vendi_prodotto(self, nome_prodotto, quantita_da_vendere):
        if nome_prodotto in self.inventario:            # Controllo se è presente nell'inventario.
            info = self.inventario[nome_prodotto]
            if info["quantita"] >= quantita_da_vendere: # Se sì, sottraiamo i pezzi.
                info["quantita"] -= quantita_da_vendere # Calcoliamo il profitto usando il metodo dell'oggetto.
                profitto_singolo = info["oggetto"].calcola_profitto()
                profitto_totale = profitto_singolo * quantita_da_vendere
                print(f"Venduti {quantita_da_vendere} di '{nome_prodotto}'. Profitto: €{profitto_totale:.2f}")
            else:
                print(f"Quantità insufficiente di {nome_prodotto}.")
        else:
            print(f"Il prodotto '{nome_prodotto}' non esiste in inventario.")
    
    def resi_prodotto(self, nome_prodotto, quantita_resa):
        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]["quantita"] += quantita_resa
            print(f"Reso accettato: +{quantita_resa} pezzi di '{nome_prodotto}'.")
        else:
            print("Questo prodotto non appartiene alla nostra fabbrica.")

# Creazione fabbrica.
mia_fabbrica = Fabbrica()

# Alcuni prodotti specifici.
tv = Elettronica("Smart TV", 200, 350, 24)  # 24 = Mesi di garanzia.
camicia = Abbigliamento("Camicia Seta", 15, 50, "Seta")

# Riformiamo il magazzino.
mia_fabbrica.aggiungi_prodotto(tv, 10)
mia_fabbrica.aggiungi_prodotto(camicia, 20)

# Simulazioni vendite.
mia_fabbrica.vendi_prodotto("Smart TV", 2)      # Profitto atteso: (350-200)*2 = 300
mia_fabbrica.vendi_prodotto("Camicia Seta", 5)  # Profitto atteso: (50-15)*5 = 175

# Simulazione di un reso.
mia_fabbrica.resi_prodotto("Smart TV", 1)

# Tentativo di vendita di un prodotto inesistente.
mia_fabbrica.vendi_prodotto("Smartphone", 1)