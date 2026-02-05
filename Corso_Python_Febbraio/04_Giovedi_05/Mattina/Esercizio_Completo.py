# Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni: Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo. Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n. Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n. Utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se n è primo o no.
n = 0 # Inizializzato con 0, poiché 0 <= 0 il ciclo while parte subito.
while n <= 0: # Validazione dell'input con il ciclo While. Finchè non è > 0, la condizione non si "rompe".
    n = int(input("Inserisci un numero intero positivo: "))
    if n <= 0:
        print("Il numero deve essere positivo, riprova.")
somma_pari = 0 # Calcolo della somma dei numeri pari con ciclo for e range
for i in range(1, n + 1): # n + 1 perché ad esempio il range(1, 10) si ferma a 9. Per includere il numero inserito dall'utente, serve n + 1.
    if i % 2 == 0: # Identifica i numeri pari
        somma_pari += i
print(f"La somma dei numeri pari da 1 a {n} è: {somma_pari}")
print(f"Numeri dispari da 1 a {n}: ") # Stampa dei numeri dispari con ciclo for
for i in range(1, n + 1):
    if i % 2 != 0: # Identifica i numeri dispari
        print(i, end=" ")
print() # Un comando stampa per andare a capo dopo la lista.
is_primo = True # Verifica se n è un numero primo con struttura if e ciclo per supporto.
if n < 2:
    is_primo = False
else: # Controllo, invece, del numero n se è dibisibile per qualche numero tra n e n-1.
    for div in range(2, n): # Uso il ciclo for per dividere n per tutti i numeri da 2 a n - 1.
        if n % div == 0: # Se è divisibile, è stato trovato, dunque is_primo = False.
            is_primo = False
            break # Dato che è stato trovato un divisore, non serve andare avanti dunque "break".
if is_primo:
    print(f"Il numero {n} è primo.")
else:
    print(f"Il numero {n} non è primo.")

