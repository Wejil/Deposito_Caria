'''
Scrivete un programma che chiede all'utente una
serie di parole e restituisce solo le vocali e l'indice della vocale all'interno delle parole.
'''
input_utente = input("Inserisci una serie di parole separate da uno spazio: ")

parole = input_utente.split()   # .split() prende la frase dell'utente e la "taglia" ogni volta che c'è uno spazio creando una lista di parole.

vocali = "aeiouAEIOU"

for parola in parole:
    print(f"Parola: '{parola}'")

    for i, lettera in enumerate(parola):    # enumerate numera ogni lettera della parola.
        if lettera in vocali:               # Controlla se la lettera è una vocale.
            print(f"Vocale '{lettera}' trovata all'indice {i}")