# Utilizzo di if. Scrivi un sistema che prende in input un numero e stama "Pari" se il numero è pari e "Dispari" se il numero è dispari.
numero = int(input("Inserisci un numero: ")) # Si chiede di inserire un numero
if numero % 2 == 0: #Verifica la condizione. Dunque se uguale a 0, esegue la riga successiva.
    print("Pari")
else: # Ma se la condizione di prima non è vera (quindi il resto non è 0) eseguirà l'else.
    print("Dispari")

# Utilizzo di while e range. Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i numero da n a 0 (compreso), decrementando di 1. Deve potersi ripetere all'infinito.
while True: # Ciclo che col True diventa infinito.
    n = int(input("Inserisci un numero intero positivo: "))
    for i in range (n, -1, -1):
        print(i)
    print("Ciclo terminato")

# Utilizzo di for. Scrivi un sistema che prende in input una lista di numeri e stampa il quadro di ciascun numero nella lista.
input_utente = input("Inserisci una serie di numeri separati da uno spazio: ") 
numeri_stringa = input_utente.split() # Comando split per trasformare la stringa in una lista di stringhe.
print("I quadrati dei numeri inseriti: ")
for stringa in numeri_stringa: # Uso del ciclo per scorrere la lista.
    n = int(stringa) # Conversione della singola stringa in un numero intero.
    quadrato = n ** 2
    print("Il quadrato di", n, "è", quadrato) # Il quadrato di {n} è {quadrato}.

# Utilizzo di if, while e for insieme. Scrivi un sistema in una lista di numeri interi che precedentemente è stata valorizzata dall'utente . Il sistema deve: 1. Utilizzare un ciclo for per trovare il numero massimo nella lista; 2. Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista; 3. Utilizzare una condizione if per stampare "Lista vuota" se la lista è vuota, altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.
input_utente = input("Inserisci i numeri separati da uno spazio: ")
numeri = [int(x) for x in input_utente.split()] # Creazione della lista convertendo ogni testo in intero.
if len(numeri) == 0: # Condizione if per controllare se la lista è vuota.
    print("Lista vuota")
else:
    massimo = numeri[0]
    for n in numeri: # Ciclo for per trovare il massimo.
        if n > massimo:
            massimo = n
    conteggio = 0
    indice = 0
    while indice < len(numeri): # Ciclo while per contare gli elementi.
        conteggio += 1
        indice += 1
    # Risultati finali
    print("Il numero massimo trovato è", massimo)
    print("La lista contiene", conteggio, "numeri")