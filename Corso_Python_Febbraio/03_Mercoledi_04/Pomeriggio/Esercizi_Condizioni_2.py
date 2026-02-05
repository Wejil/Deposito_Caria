# Scrivi un programma che chieda all'utente la sua età. Se l'età è inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi vedere questo film". Altrimenti, dovrebbe stampare "Puoi vedere questo film".
eta =int(input("Inserisci la tua eta': "))
match eta:
    case eta if eta < 18: # Controllo dell'età, se è maggiore o minore di 18.
        print("Mi dispiace, non puoi vedere questo film") # Se minore, non potrà vedere il film.
    case _:
        print("Puoi vedere questo film") # Se maggiore, potrà vedere il film.

#Scrivi un programma che chieda all'utente di inserire due numeri e un'operazione da eseguire tra addizione (+), sottrazione (-), moltiplicazione (*) e divisone (/). Il programma dovrebbe poi eseguire l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere per zero, il programma dovrebbe stampare "Errore: Divisione per zero". Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione non valida".
num1 = int(input("Inserisci primo numero: "))
num2 = int(input("Inserisci secondo numero: "))
operazione = input("Inserisci operazione (+ - * /): ")
match operazione:
    case "+" | "-" | "*": # Case: addizione, sottrazione e moltiplicazione raggruppati poiché simili.
        if operazione == "+":
            risultato = num1 + num2
        elif operazione == "-":
            risultato = num1 - num2
        else:
            risultato = num1 * num2
        print(risultato)
    case "/": # Case: divisione, a parte con l'if poiché c'è bisogno di prendere in analisi la situazione con lo 0.
        if num2 == 0:
            print("Errore.")
    case _:
        print("Operazione non valida.")

# Esercizio extra "match nel match"
animale = input("Che animale preferisci?: ")

match animale: # Match iniziale: richiesta dell'animale, quindi si parla dell'animale.
    case "gatto":
        print("Gatto è la scelta.")
        colore = input("Colore gatto")
        match colore: # Secondo match: il colore dell'animale, in questo caso del gatto.
            case "bianco":
                print("Il gatto è bianco")
    