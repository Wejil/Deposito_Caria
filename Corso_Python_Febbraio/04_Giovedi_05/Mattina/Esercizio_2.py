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