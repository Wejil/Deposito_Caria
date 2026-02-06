'''
Esercizio 1:  Condizioni e cicli
Chieda all'utente di inserire un numero intero positivo. 
 
 Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
 
 Per ogni numero: 
 
 stampi "pari" se il numero è pari 
 
 stampi "dispari" se il numero è dispari 
 
 
 
 Se l'utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore.
'''
numero = int(input("Inserisci un numero intero positivo: ")) # Si chiede all'utente un numero intero positivo.

if numero <= 0: # Si controlla se il numero è valido, ovvero se è positivo.
    print("Il numero deve essere positivo (maggiore di zero).")
else:
    for i in range(1, numero + 1): # Ciclo for da 1 fino al numero inserito dall'utente.
        if i % 2 == 0: # Si controlla se il numero è pari o dipari.
            print(f"{i} - pari") # Se resto = 0 , è pari.
        else:
            print(f"{i} - dispari") # Se resto != è dispari.

'''
Esercizio 2:  Funzioni e Liste
Definisca una funzione chiamata conta_vocali. 
 
 La funzione deve: 
 
 ricevere una stringa come parametro 
 
 contare quante vocali contiene (a, e, i, o, u) 
 
 restituire il numero totale di vocali 
 
 
 
 Nel programma principale: 
 
 chiedi all'utente di inserire una parola 
 
 chiama la funzione 
 
 stampa il numero di vocali trovate
'''
def conta_vocali(testo): # Si definisce la funzione conta_vocali. Conta quante vocali ci sono in una stringa e come parametri ci sono il testo (stringa da analizzare) e restituisce il numero totale di vocali.
    vocali = ['a', 'e', 'i', 'o', 'u'] # Liste delle vocali in minuscolo.
    conteggio = 0
    for lettera in testo.lower(): # .lower() per gestire le maiuscole.
        if lettera in vocali:
            conteggio += 1
    return conteggio # Restituisce il totale.
parola = input("Inserisci una parola: ") # Si chiede all'utente di inserire una parola.
numero_vocali = conta_vocali(parola) # Chiama la funzione.
print(f"La parola '{parola}' contiene {numero_vocali} vocali.")