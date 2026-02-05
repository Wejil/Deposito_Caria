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