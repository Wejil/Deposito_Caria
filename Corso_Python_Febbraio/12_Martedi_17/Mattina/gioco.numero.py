"""Scrivete un gioco in cui il giocatore 1 inserisce un
numero da 1 a 100 e il giocatore2 ha 5 tentativi per
indovinare il numero.
Il programma fornisce suggerimenti (troppo alto,
troppo basso), termina quando l'utente indovina
correttamente, quando i tentativi finiscono o se
scrive «mi arrendo»."""

giocatore1 = int(input("inserisci un numero da 1 a 100: "))


counter = 0
tentativi_rimasti = 5

while counter < 5:
    giocatore2 = int(input("indovina il numero da 1 a 100 o digita: "))
    if giocatore1 != giocatore2:
        counter += 1
        tentativi_rimasti -= 1
        if giocatore2 > giocatore1:
            print("numero troppo alto")
            scelta = input("vuoi arrenderti? (si/no)")
            if scelta == "si":
                break
        else:
            print("numero troppo basso")
            scelta = input("vuoi arrenderti? (si/no)")
            if scelta == "si":
                break
            
    elif giocatore2 == "mi arrendo":
        print("hai perso")
        
        
    else:
        print(f"hai indovinato il numero è {giocatore1}")
        break
    
    if tentativi_rimasti == 0:        
        print("numero tentativi esauriti")