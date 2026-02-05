# Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è stato generato. Dopo ogni tentativo, il programma dovrebbe dire all'utente se il numero da indovinare è più alto o più basso rispetto al numero inserito. Il gioco termina quando l'utente indovina il numero o decide di uscire.
import random
def genera_numero_casuale(): # Genera un numero casuale tra 1 e 100. Restituisce il numero generato.
    numero = random.randint(1, 100)
    return numero
def chiedi_tentativo(): # Chiede all'utente di inserire un tentativo, gestisce anche l'opzione di uscire e restituisce il numero inserito o None se vuole uscire.
    scelta = input("Inserisci un numero (o scrivi 'esci' per uscire): ")
    if scelta.lower() == "esci":
        return None
    try:
        tentativo = int(scelta)
        return tentativo
    except ValueError:
        print("Input non valido! Inserisci un numero.")
        return chiedi_tentativo()  # Richiama se stesso (ovvero ricorsione).

def confronta_numeri(tentativo, numero_segreto): # Confronta il tentativo dell'utente con il numero segreto e restituisce "corretto" se ha indovinato, "alto" se il tentativo è troppo alto e "basso" se è troppo basso.
    if tentativo == numero_segreto:
        return "corretto"
    elif tentativo > numero_segreto:
        return "alto"
    else:
        return "basso"
def gioca(): # Funzione principale del "gioco", che gestisce l'intero flusso di esso.
    print("=" * 50)
    print("Indovina il numero")
    print("=" * 50)
    print("Ho generato un numero tra 1 e 100.")
    print("Prova ad indovinarlo.")
    print("(Scrivi 'esci' in qualsiasi momento per uscire)")
    numero_segreto = genera_numero_casuale() # Genera il numero segreto
    tentativi = 0 # Contatore tentativi
    while True: # Loop di gioco
        tentativo = chiedi_tentativo() # Chiedi tentativo
        if tentativo is None: # Se vuole uscire
            print(f"Hai abbandonato! Il numero era {numero_segreto}")
            break
        tentativi += 1 # Incrementa contatore
        risultato = confronta_numeri(tentativo, numero_segreto) # Confronta
        if risultato == "corretto":
            print(f"Hai indovinato.")
            print(f"Il numero era {numero_segreto}")
            print(f"Ci hai messo {tentativi} tentativi.")
            break
        elif risultato == "alto":
            print(f"Troppo alto, prova con un numero più basso.")
        else:  # basso
            print(f"Troppo basso, prova con un numero più alto.")
    rigioca = input("Vuoi giocare ancora? (si/no): ") # Chiedi se vuole rigiocare
    if rigioca.lower() == "si":
        print("\n" * 2)
        gioca()  # Ricomincia il gioco (ricorsione)
    else:
        print("Grazie per aver giocato!")
gioca() # Avvio del gioco.

# Chiedi all'utente di inserire un numero N. Il programma dovrebbe stampare la sequenza di Fibonacci fino a N. Ad esempio, se l'utente inserisce 100, il programma dovrebbe stampare tutti i numeri della sequenza di Fibonacci minori o uguali a 100.
def stampa_fibonacci(limite): # Funzione che calcola e stampa i numeri di Fibonacci fino a un valore massimo "limite".
    a, b = 0, 1
    print(f"Sequenza di Fibonacci fino a {limite}:")
    while a <= limite:
        print(a, end=" ") # Il nuovo a diventa il vecchio b; il nuovo b diventa la somma dei due precedenti
        a, b = b, a + b
    print() # Per andare a capo alla fine della sequenza
n_utente = int(input("Inserisci il valore massimo N: ")) # Si chiede l'input all'utente
stampa_fibonacci(n_utente) # Chiamiamo la funzione passando il numero inserito