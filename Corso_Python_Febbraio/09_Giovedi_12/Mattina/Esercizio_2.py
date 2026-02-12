'''
Andiamo a creare un sistema ripetibile che simuli un teatro:

Classe Base: Posto
    - Attributi privati:
        - _numero (intero): il numero del posto.
        - _fila (stringa): la fila in cui si trova il posto.
        - _occupato (booleano): stato del posto, se è occupato (True) o libero (False).
    - Metodi:
        - __init__(numero, fila): inizializza il posto impostando _occupato a False.
        - prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato.
        - libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato.
        - Getter: per recuperare il numero, la fila e lo stato (occupato/libero).
Classi Derivate:
    - PostoVIP:
        - Attributi aggiuntivi: servizi_extra (ad es. una lista di servizi come “Accesso al lounge”, “Servizio in posto”).
        - Metodi:
            - Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l'attivazione dei servizi extra.
        - PostoStandard:
            - Attributi aggiuntivi: costo (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).
            - Metodi:
                - Può sovrascrivere prenota() per includere la visualizzazione del costo o altre particolarità della prenotazione.
Classe Teatro:
    - Attributi:
        - _posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
    - Metodi:
        - aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
        - prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
        - stampa_posti_occupati(): stampa tutti i posti che risultano occupati.
'''

# Classe base.
class Posto:
    def __init__(self, numero, fila):   # Attributi "protetti" (_ prima per l'incapsulamento).
        self._numero = numero
        self._fila = fila
        self._occupato = False
    
    # Getter.
    def get_numero(self):
        return self._numero
    def get_fila(self):
        return self._fila
    def is_occupato(self):
        return self._occupato
    
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato.")
            return True
        else:
            print("Errore: il posto è già occupato.")
            return False
    
    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} è ora libero.")
        else:
            print(f"Il posto {self._fila}{self._numero} non era prenotato.")

# Classi derivate.
class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra, costo):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra  # È una lista.
        self.costo = costo
    
    def prenota(self):  # Si richiama il metodo della classe base e si aggiunge una logica specifica. Senza riscrivere la logica del controllo se è occupato o meno. Il "padre" Posto verifica se il posto è libero e cambia lo stato in True.
        if super().prenota():
            print(f"Servizi VIP attivati: {', '.join(self.servizi_extra)}")
            print(f"Tariffa VIP (servizi inclusi): €{self.costo}")

class PostoStandard(Posto):
    def __init__(self, numero, fila, costo):
        super().__init__(numero, fila)
        self.costo = costo
    
    def prenota(self):
        if super().prenota():
            print(f"Costo prenotazione standard: €{self.costo}")

# Classe teatro.
class Teatro:
    def __init__(self):
        self._posti = {}    # Dizionario dove la chiave è una tupla (fila, numero). Le tulpe sono immutabili e così facendo Python risale ubito a quel posto senza guardare gli altri.
    
    def aggiungi_posto(self, posto):
        chiave = (posto.get_fila(), posto.get_numero())
        self._posti[chiave] = posto
    
    def prenota_posto(self, fila, numero):
        chiave = (fila, numero)
        if chiave in self._posti:
            self._posti[chiave].prenota()   # In base al posto (se VIP o Standard) mostrerà il metodo che mostra i servizi extra o il costo. Unico comando con comportamenti diversi in base all'oggetto.
        else:
            print("Questo posto non esiste.")
        
    def libera_posto(self, fila, numero):
        chiave = (fila, numero)
        if chiave in self._posti:
            self._posti[chiave].libera()
        else:
            print("Errore, posto non valido.")
    
    def stampa_posti_occupati(self):
        print("Elenco dei posti occupati.")
        trovati = False
        for posto in self._posti.values():
            if posto.is_occupato():
                tipo = "VIP" if isinstance(posto, PostoVIP) else "Standard"
                print(f"Fila {posto.get_fila()}, Numero {posto.get_numero()} [{tipo}]")
                trovati = True
        if not trovati:
            print("Nessun posto occupato al momento.")

# Menu ripetibile.
teatro = Teatro()

while True:
    print("1. Aggiungi Posto VIP.")
    print("2. Aggiungi Posto Standard.")
    print("3. Prenota un Posto.")
    print("4. Libera un Posto.")
    print("5. Mostra Posti Occupati.")
    print("6. Esci.")

    scelta = input("Operazione: ")

    if scelta == "1" or scelta == "2":
        f = input("Fila: ").upper() # Esempio: A.
        n_str= input("Numero posto: ")
        costo_str = input("Costo del biglietto (€): ")

        if n_str.isdigit() and costo_str.replace(".", "", 1): # Controllo validità dei numeri.
            n = int(n_str)
            costo = float(costo_str)

            if scelta == "1":
                servizi = ["Accesso Lounge", "Servizio al posto"]
                teatro.aggiungi_posto(PostoVIP(n, f, servizi, costo))
            else:
                teatro.aggiungi_posto(PostoStandard(n, f, costo))
            print(f"Posto {f}{n} aggiunto al sistema.")
        else:
            print("Errore, il numero deve essere un intero.")
    
    elif scelta == "3":
        f = input("Fila: ").upper()
        n = input("Numero: ")
        if n.isdigit():
            teatro.prenota_posto(f, int(n))

    elif scelta == "4":
        f = input("Fila: ").upper()
        n = input("Numero: ")
        if n.isdigit():
            teatro.libera_posto(f, int(n))

    elif scelta == "5":
        teatro.stampa_posti_occupati()

    elif scelta == "6":
        print("Il sistema si sta chiudendo.")
        break