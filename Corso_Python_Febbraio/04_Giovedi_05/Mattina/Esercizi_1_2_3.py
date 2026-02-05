# Numeri pari e dispari o sequenza: Scrivi un programma che chiede all'utente di inserire un numero o una stringa scegliendo prima quale. Il programma dovrebbe determinare se il numero è pari o dispari e stampare il risultato e se deve ripetere o stampare e poi ripetere.
ripeti = "si"
while ripeti == "si": # Loop di while principale dove finché l'utente scrive "si", ripete.
    print("1. Numero") # Menu di scelta tra Numero e Stringa.
    print("2. Stringa")
    scelta = input("Cosa vuoi inserire? (1/2): ") # Scelta dell'utente e salva la scelta.
    match scelta:
        case "1":
            numero = int(input("Inserire un numero: ")) # Si chiede di inserire un numero
            if numero % 2 == 0: # Controllo se il numero è pari, ovvero se dà resto zero. Altrimenti è dispari.
                print(f"{numero} è pari.")
            else:
                print(f"{numero} è dispari.")
        case "2":
            testo = input("Inserisci una stringa: ") # In questo caso si chiede di inserire una stringa.
            print(f"Hai inserito: {testo}.")
            print(f"Lunghezza: {len(testo)} caratteri.")
        case _: # Caso di default nel caso in cui non venisse scelta nessuna delle altre opzioni.
            print("Scelta non valida.")
    ripeti = input ("Vuoi ripetere? (si/no): ") # Chiede se ripetere. Se sì, riparte il while. Altrimenti si ferma ed esce.

# Numeri primi in un intervallo: Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e 50). Il programma dovrebbe stampare tutti i numeri primi compresi in quell'intervallo o i numeri non primi o entrambi divisi a tua scelta, salvandoli in due aggregazioni differenti e chiedere se deve ripetere
ripeti = "si"
while ripeti == "si":
    inizio = int(input("Inserisci il numero iniziale dell'intervallo: ")) # Si chiedono i due estremi dell'intervallo (ES.: 10 e 50)
    fine = int(input("Inserisci il numero finale dell'intervallo: "))
    numeri_primi = [] # Liste per salvare i numeri.
    numeri_non_primi = []
    for numero in range(inizio, fine, + 1):
        if numero < 2: # I numeri minori di 2 non sono primi, dunque controlla.
            numeri_non_primi.append(numero)
        else:
            is_primo = True # Se non è minore di 2, controlla se è primo.
            for i in range(2, numero):
                if numero % i == 0: # Dunque controlla la divisibilità e salva nella lista corretta.
                    is_primo = False
                    break
            if is_primo:
                numeri_primi.append(numero)
            else:
                numeri_non_primi.append(numero)
    print("1. Solo numeri primi.") # Menu di scelta
    print("2. Solo numeri non primi.")
    print("3. Entrambi.")
    scelta = input("Scegli (1/2/3): ")
    match scelta:
        case "1": # Mostra solo i primi.
            print(f"Numeri primi tra {inizio} e {fine}:")
            print(numeri_primi)
            print(f"Totale: {len(numeri_primi)} numeri primi.")
        case "2": # Mostra solo i non primi.
            print(f" Numeri non primi tra {inizio} e {fine}:")
            print(numeri_non_primi)
            print(f"Totale: {len(numeri_non_primi)} numeri non primi:")
        case "3": # Mostra entrambi.
            print(f"Numeri non primi tra {inizio} e {fine}: ")
            print(numeri_primi)
            print(f"Totale: {len(numeri_primi)} numeri primi.")
            print(f"Numeri non primi tra {inizio} e {fine}: ")
            print(numeri_non_primi)
            print(f"Totale: {len(numeri_non_primi)} numeri non primi.")
        case _: # Nel caso in cui non venga fatta una delle altre scelte, quindi si arriva a quella di default. In questo caso non valida.
            print("Scelta non valida.")

# Fattori comuni: Chiedi all'utente di inserire due numeri. Il programma dovrebbe determinare e stampare i fattori comuni di entrambi i numeri. Se non ci sono fattori comuni oltre 1, dovrebbe stampare "I numeri sono comprimi". La stessa cosa ma anche per due stringhe (.equal ) e chiedere se deve ripetere ma sono “ complementari” solo se hanno tutte le lettere in comune (es:abs/ sab)
ripeti = "si"
while ripeti == "si":
    print("1. Fattori comuni tra due numeri.")
    print("2. Lettere comuni tra due stringhe.")
    scelta = input("Scegli (1/2): ")
    match scelta:
        case "1": # Fattori comuni tra numeri
            num1 = int(input("Inserisci il primo numero: "))
            num2 = int(input("Inserisci il secondo numero: "))
            fattori_comuni = [] # Lista per salvare i fattori comuni
            limite = min(num1, num2) # Trova i fattori comuni, controlla da 1 fino al numero più piccolo.
            for i in range (1, limite + 1):
                if num1 % i == 0 and num2 % i == 0: # Se entrambi sono divisibili per "i", allora "i" è un fattore comune.
                    fattori_comuni.append(i)
            print(f"Fattori comuni: {fattori_comuni}")
            if len(fattori_comuni) == 1 and fattori_comuni[0] == 1: # Controlla se sono comprimi (e c'è solo il numero 1 in comune).
                print(f"I numeri sono comprimi.")
            else:
                print(f"Totale: {len(fattori_comuni)}")
        case "2": # Lettere comuni tra stringhe.
            str1 = input("Inserisci la prima stringa: ").lower()
            str2 = input("Inserisci la seconda stringa: ").lower()
            lettere_comuni = [] # Trova e salva le lettere comuni.
            for lettera in str1:
                if lettera in str2 and lettera not in lettere_comuni:
                    lettere_comuni.append(lettera)
            print(f"Lettere comuni: {lettere_comuni}")
            print(f"Totale: {len(lettere_comuni)}")
            # Controllo delle stringhe se sono complementari e lo sono se hanno tutte le lettere in comune (anche se in ordine diverso).
            set1 = set(str1) # Conversione in set per confrontare.
            set2 = set(str2)
            if set1 == set2:
                print(f"Le stringhe sono complementari.")
            else:
                print(f"Le stringhe non sono complementari")
        case _: # Caso di default
            print("Scelta non valida")
    ripeti = input("Vuoi ripetere? (si/no): ")