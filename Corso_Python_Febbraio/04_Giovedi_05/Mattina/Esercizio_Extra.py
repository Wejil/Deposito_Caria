storico_tentativi = [] # Inizializzo una lista vuota per salvare tutti i numeri validi inseriti.
while True:
    print("Nuovo tentativo.")
    n = 0 # Validazione input
    while n <= 0:
        n = int(input("Inserisci un numero intero positivo: "))
        if n <= 0:
            print("Errore. Deve essere un numero positivo.")
    storico_tentativi.append(n) # Salvo il tentativo nella lista. Aggiunge il numero n alla fine della lista e ogni volta che viene aggiunto un numero valido, la lista si allunga.
    somma_pari = sum(i for i in range(1, n + 1) if i % 2 == 0) # Somma pari, dispari, primo.
    print(f"Somma pari: {somma_pari}")
    print("Menu gestione storico.") # Sezione di gestione dello storico.
    print("1. Visualizza tutti i tentativi.")
    print("2. Modifica un tentativo precedente.")
    print("3. Elimina un tentativo.")
    print("4. Continua con un nuovo numero.")
    print("5. Esci dal programma.")
    scelta = input("Cosa vuoi fare? (1-5): ")
    if scelta == "1":
        print(f"Lista tentativi: {storico_tentativi}")
    elif scelta == "2":
        if not storico_tentativi:
            print("Lista vuota!")
        else:
            for i, valore in enumerate(storico_tentativi): # Viene mostrata la lista con gli indici per aiutare l'utente, poiché fornisce anche la posizione.
                print(f"Indice {i}: Valore {valore}")
            indice = int(input("Quale indice vuoi modificare? "))
            nuovo_valore = int(input("Inserisci il nuovo valore: "))
            if 0 <= indice < len(storico_tentativi):
                storico_tentativi[indice] = nuovo_valore # Sovrascrive quello che c'era in quella determinata posizione.
                print("Modifica effettuata con successo.") 
            else:
                print("Indice non valido.")
    elif scelta == "3":
        if storico_tentativi:
            for i, valore in enumerate(storico_tentativi):
                print(f"Indice {i}: Valore {valore}")
            indice = int(input("Quale indice vuoi eliminare? "))
            if 0 <= indice < len(storico_tentativi):
                rimosso = storico_tentativi.pop(indice) # Elimina e rimuove l'elemento in quella posizione e "accorcia" la lista di conseguenza, automaticamente.
                print(f"Rimosso il valore {rimosso}.")
        else:
            print("Lista vuota.")
    elif scelta == "5":
        print("Arrivederci.")
        break