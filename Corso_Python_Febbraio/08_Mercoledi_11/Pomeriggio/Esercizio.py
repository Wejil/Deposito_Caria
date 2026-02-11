'''
Creare una classe ContoBancario che incapsula le informazioni di un conto e fornisce
metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare
l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.
1. Classe ContoBancario:
Attributi privati:
- __titolare (stringa che rappresenta il nome del titolare del conto)
- __saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
- deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
- preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
- visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
2. Gestione dei Metodi e Sicurezza:
- I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
- Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota).

(utente può creare il suo conto, l'admin no)
'''

class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):   # Attributi privati con il doppio underscore.
        self.__titolare = titolare
        self.__saldo = saldo_iniziale
    
    def visualizza_saldo(self): # Restituisce il saldo in sola lettura. Metodo per il saldo (sicurezza).
        return self.__saldo

    def deposita(self, importo):    # Aggiunge fondi se l'importo è valido (non deve essere negativo).
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di €{importo} effettuato")
        else:
            print("Errore: l'importo deve essere positivo.")
    
    def preleva(self, importo): # Sottrae fondi se disponibili e importo valido.
        if importo <= 0:
            print("Errore: l'importo deve essere positivo.")
        elif importo > self.__saldo:
            print("Fondi insufficienti per il prelievo.")
        else:
            self.__saldo -= importo
            print(f"Prelievo di €{importo} effettuato.")
    
    def get_titolare(self): # Restituisce il nome del titolare.
        return self.__titolare
    
database_conti = {} # Dizionario per permettere all'Admin di vedere tutti i conti creati.

while True:
    print("Che utente sei?")
    print("1. Utente (Crea/Gestisci il tuo conto)")
    print("2. Admin (Supervisione)")
    print("3. Esci dal sistema.")

    ruolo = input("Seleziona ruolo: ")

    if ruolo == "1":
        nome = input("Inserisci il tuo nome per aprire il conto: ")
        if nome in database_conti:
            print(f"Bentornato {nome}.")
            conto_attivo = database_conti[nome]
        else:   # L'utente crea il suo conto.
            conto_attivo = ContoBancario(nome)
            database_conti[nome] = conto_attivo
            print("Conto creato con successo.")
        
        while True: # Menu operativo per l'utente.
            print("a. Visualizza saldo")
            print("b. Deposita")
            print("c. Preleva")
            print("d. Torna al menu principale")

            azione = input("Scegli: ")
            if azione == "a":
                print(f"Saldo attuale: €{conto_attivo.visualizza_saldo(): }")
            elif azione == "b":
                imp = input("Importo: ")
                if imp.replace(".", "", 1).isdigit():
                    conto_attivo.deposita(float(imp))
            elif azione == "c":
                imp = input("Importo: ")
                if imp.replace(".", "", 1).isdigit():
                    conto_attivo.preleva(float(imp))
            elif azione == "d":
                break
    
    elif ruolo == "2":                                      # Logica admin.
        codice = input("Inserisci il codice di sicurezza Admin: ")
        if codice == "admin123":
            print("Accesso consentito.")
            if not database_conti:
                print("Nessun conto presente nel sistema")
            else:                                           # Mostra tutti i conti.
                print(f"{'TITOLARE':<20} | {'SALDO':<10}")  # Configurazione formattazione.
                totale_liquidi = 0
                for nome, conto in database_conti.items():
                    saldo_c = conto.visualizza_saldo()
                    print(f"{nome:<20} | €{saldo_c}")
                    totale_liquidi += saldo_c
                print(f"Liquidità totale banca: €{totale_liquidi}")
        else:
            print("Accesso negato, codice errato.")
    elif ruolo == "3":
        print("Arrivederci.")
        break
    else:
        print("Scelta non valida.")