# Scrivi un programma che esegua le seguenti operazioni: Chiedi all'utente di inserire un numero intero positivo n. Se l'utente inserisce un numero negativo o zero, continua a chiedere un numero fino a quando non viene inserito un numero positivo. Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza della lista deve essere n. Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista. Utilizza un ciclo for per stampare tutti i numeri dispari nella lista. Utilizza una funzione per determinare se un numero è primo. La funzione deve restituire True se il numero è primo, altrimenti False. Utilizza un ciclo for per stampare tutti i numeri primi nella lista. Infine, utilizza una struttura if per determinare se la somma di tutti i numeri nella lista è un numero primo e stampa il risultato
import random # Genera una lista casuale, importando una libreria di numeri casuali.
n = 0 # Si chiede un numero positivo. n = 0 così entra nel while
while n <= 0: # Continua finché n non è negativo o zero.
    n = int(input("Inserisci un numero intero positivo n: "))
    if n <= 0:
        print("Errore. Inserisci un numero maggiore di 0.")
# Genera una lista di numeri n casuali tra 1 ed n
numeri = []
for i in range(n):
    numero_casuale = random.randint(1, n) # Genera un numero casuale tra 1 e n (inclusi).
    numeri.append(numero_casuale)
print(f"Lista generata ({n} numeri): {numeri}")
# Somma dei numeri pari
somma_pari = 0
for numero in numeri:
    if numero % 2 == 0: # Controlla se è pari. Se è pari, resto 0.
        somma_pari += numero # Aggiunge alla somma.
print(f"Somma dei numeri pari: {somma_pari}")
print("Numeri dispari nella lista: ") # Stampa i numeri dispari.
dispari_trovati = []
for numero in numeri:
    if numero % 2 != 0: # Se è dispari.
        dispari_trovati.append(numero)
print(dispari_trovati)
print("Numeri primi nella lista") # Stampa numeri primi
primi_trovati = []
for numero in numeri: # Controlla se un numero è primo e nel caso lo salva.
    if numero < 2: # Non è primo
        is_primo = False
    else: # Controlla divisibilità
        is_primo = True # Si assume che il numero sia primo.
        for i in range(2, numero):
            if numero % i == 0:
                is_primo = False # Se viene trovato il divisore, il numero non è primo.
                break # Si esce dal for.
    if is_primo: # Se è primo, lo si aggiunge alla lista.
        primi_trovati.append(numero)
print(primi_trovati)
somma_totale = 0 # Controlla se la somma totale è prima.
for numero in numeri:
    somma_totale += numero
print(f"Somma totale di tutti i numeri: {somma_totale}")
if somma_totale < 2: # Controlla se la somma_totale è primo.
    print(f"{somma_totale} non è un numero primo.")
else:
    is_primo_somma = True
    for i in range(2, somma_totale):
        if somma_totale % i == 0:
            is_primo_somma = False
            break
    if is_primo_somma:
        print(f"{somma_totale} è un numero primo.")
    else:
        print(f"{somma_totale} non è un numero primo.")