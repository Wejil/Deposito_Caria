'''
Esercizio: Sistema di Gestione Negozio

Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve interagire con clienti, gestire l'inventario e permettere agli amministratori di supervisionare le operazioni. Il sistema sarà strutturato in tre parti principali:
Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.
Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).
Amministrazione:
l'analisi del negozio da parte degli amministratori.
Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali.
Puoi pre inserire gli amministratori non i clienti
Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio dopo un login e una registrazione, nonché fornire gli strumenti necessari per la manutenzione e l'analisi del negozio da parte degli amministratori.
'''
class Negozio:
    def __init__(self): # Inventario {"Nome articolo": {"prezzo": float, "quantità": int}}
        self.inventario = { # Utilizza i nomi dei prodotti come chiavi, quindi if nome in self.inventario permette di vedere se esiste anziché scorrere una lista col ciclo for.
            "Mela": {"prezzo": 0.50, "quantita": 20},
            "Pane": {"prezzo": 1.20, "quantita": 10},
            "Latte": {"prezzo": 1.80, "quantita": 5}
        }
        self.utenti = { # Utenti: {"username": {"password": str, "ruolo": str, "acquisti": list}}. Admin: pre-inseriti. Permette di distinguere "admin" e "cliente" tramite la chiave "ruolo".
            "admin": {"password": "123", "ruolo": "admin"},
            "boss": {"password": "root", "ruolo": "admin"}
        }
        self.guadagni_totali = 0.0
    
    def aggiungi_aggiorna_articolo(self, nome, prezzo, quantita): # Gestione inventario solo per gli admin.
        self.inventario[nome] = {"prezzo": prezzo, "quantita": quantita}
        print(f"Articolo '{nome}' aggiornato con successo.")
    def rimuovi_articolo(self, nome):
        if nome in self.inventario:
            del self.inventario[nome]
            print(f"Articolo '{nome}' rimosso.")
        else:
            print("Articolo non trovato.")
    def visualizza_inventario_completo(self):
        for nome, info in self.inventario.items():
            print(f"{nome:<15}, prezzo: €{info['prezzo']:.2f}, quantità: {info['quantita']}")
    
    def mostra_articoli_disponibili(self): # Gestione clienti.
        for nome, info in self.inventario.items():
            if info['quantita'] > 0:
                print(f"{nome:<15}, prezzo: €{info['prezzo']:.2f}")
    def acquista_articolo(self, username, nome_articolo):
        if nome_articolo in self.inventario:
            if self.inventario[nome_articolo]["quantita"] > 0: # Esegui vendita.
                prezzo = self.inventario[nome_articolo]["prezzo"]
                self.inventario[nome_articolo]["quantita"] -= 1
                self.guadagni_totali += prezzo
                if "acquisti" not in self.utenti[username]:
                    self.utenti[username]["acquisti"] = []
                self.utenti[username]["acquisti"].append(nome_articolo)
                print(f"Acquisto completato.")
            else:
                print("Articolo non disponibile.")
        else:
            print("Articolo non trovato.")

    def mostra_analisi(self): # Analisi (solo per gli admin).
        print(f"Guadagni totali: €{self.guadagni_totali:.2f}")
        print(f"Utenti registrati: {len(self.utenti)}")

# Accesso e registrazione.
negozio = Negozio()
while True:
    print("1. Login.")
    print("2. Registrazione.")
    print("3. Esci.")
    scelta_iniziale = input ("Scegli: ")

    utente_loggato = None
    if scelta_iniziale == "1":
        user = input("Username: ")
        psw = input("Password: ")
        if user in negozio.utenti and negozio.utenti[user]["password"] == psw:
            utente_loggato = user
            print("Bentornato {user}.")
        else:
            print("Credenziali errate.")
    elif scelta_iniziale == "2":
        nuovo_user = input("Scegli Username: ")
        if nuovo_user in negozio.utenti:
            print("Username già esistente.")
        else:
            nuova_psw = input("Scegli Password: ")
            negozio.utenti[nuovo_user] = {"password": nuova_psw, "ruolo": "cliente", "acquisti": []}
            print("Registrazione completata.")
    elif scelta_iniziale == "3":
        break

# Sotto-Menu dopo il login.