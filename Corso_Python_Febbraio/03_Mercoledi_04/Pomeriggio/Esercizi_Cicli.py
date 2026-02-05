# Chiedi all'utente di inserire un programma. Il programma dovrebbe quindi fare un conto alla rovescia a partire da quel numero fino a zero, stampando ogni numero e chiederti se vuoi ripetere o no. (Mescola While e For)
ripeti = "si" # Variabile per controllare il while
while ripeti == "si": # While che continua finché l'utente vuole
    numero = int(input("Inserisci un numero: "))
    print("Conto alla rovescia")
    for i in range(numero, -1, -1): # For per il conto alla rovescia
        print(i)
    print("Fine countdown")
    ripeti = input("Vuoi ripetere? (si/no): ") # Richiesta se si vuole continuare o meno.
print("Programma terminato")

# Chiedi all'utente di inserire un numero. Il programma dovrebbe controllare se il numero inserito primo / pari o no. Se è primo lo salva e stampa "Il numero è primo". Altrimenti "Il numero non è primo". Si ferma il tutto quando ha 5 numeri primi. (Mescola While, For e Liste)
numeri_primi = [] # Lista vuota per i numeri primi in cui salvarli.
while len(numeri_primi) < 5: # While che continua finché non riesco ad ottenere 5 numeri primi
    numero = int(input("Inserisci un numero: "))
    if numero < 2: # Controllo del numero se è primo
        print("Il numero non è primo")
    else:
        is_primo = True # Dunque è preso in considerazione perché primo
        for i in range(2,numero): # For controlla i divisori. Se lo trova, non è primo.
            if numero % i == 0: # Se divisibile per i (che sarebbe per due, quindi pari). "%"" Serve a controllare se è divisibile. Se 1: non divisibile. Se 0: divisibile.
                is_primo = False # Non è primo
                break # Si esce fuori dal for
        if is_primo:
            numeri_primi.append(numero) # Se è primo lo aggiunge alla lista iniziale in cui poter salvare il numero.
            print("Il numero è primo!")
        else:
            print("Il numero non è primo")
