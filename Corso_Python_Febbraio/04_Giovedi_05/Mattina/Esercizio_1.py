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