# Creare una serie di condizioni una dentro l'altra che a fronte di un input per ogni if decidano se farti passare o no (3 livelli fate un paragone con ==)
password = input("Inserisci la password: ")

if password == "123":
    print("Password corretta.")
    
    # Secondo livello - 2FA
    codice = input("Inserisci il codice: ")
    
    if codice == "5834":
        print("Codice corretto.")
        
        # Terzo livello - Domanda di sicurezza
        risposta = input("Qual e' il tuo animale preferito? ")
        
        if risposta == "gatto":
            print("Accesso consentito.")
        else:
            print("Risposta sbagliata, accesso negato.")
    else:
        print("Codice sbagliato, accesso negato.")
else:
    print("Risposta sbagliata, accesso negato.")

# Andare a creare un if con vari elif e un else finale che gestisca un menu per la selezione di un crud basilare (aggiungi rimuovi elimina). Ha bisogno delle liste.
studenti = ["paolo", "aldo"]
print("1 - Aggiungi")
print("2 - Rimuovi")
print("3 - Elimina tutto")

scelta = input("Scegli un'opzione (1-3): ")

if scelta == "1":
    valore = input("Inserisci valore: ")
    studenti.append(valore)
    print(studenti)
elif scelta == "2":
    valore = input("Valore da rimuovere: ")
    if valore in studenti:
        studenti.remove(valore)
    print(studenti)
elif scelta == "3":
    studenti.clear()
    print("Lista studenti svuotata.")
else:
    print("Scelta non disponibile.")



# Creare un if con else semplice, dentro l'if inserire una struttura di creazione di dati (nome, password, id dato dal sistema a crescere) e nell'else il controllo automatico là dove è presente l'account nel sistema e solo se si passa dall'else concludere lo script.
utenti = []
password_utenti = []
id_utente = 1
nome = input("Inserisci nome: ")
if nome not in utenti:
    password = input("Inserisci password: ")
    utenti.append(nome)
    password_utenti.append(password)
    print("Account creato.")
    print("ID utente:", id_utente)
    id_utente = id_utente + 1
else:
    print("Account già presente.")
    password = input("Inserisci password per entrare: ")
    indice = utenti.index(nome)
    if password == password_utenti[indice]:
        print("Login effettuato con successo.")
    else:
        print("Password errata.")
print("Fine programma.")
