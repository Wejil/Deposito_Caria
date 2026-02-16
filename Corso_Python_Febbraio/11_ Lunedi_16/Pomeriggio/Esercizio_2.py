'''
Scrivete un programma che chiede una stringa all'utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}
'''

testo = input("Inserisci una parola o una frase: ") # Richiesta stringa all'utente.

frequenze = {}  # Dizionario vuoto per memorizzare i conteggi.

for carattere in testo:         # Ciclo su ogni carattere della stringa.
    if carattere in frequenze:  # Se il carattere è già nel dizionario, aumento il suo "valore".
        frequenze[carattere] += 1
    else:                       # Se il carattere non c'è, lo si aggiunge partendo da 1.
        frequenze[carattere] = 1

# Stampa del risultato.
print("Frequenza dei caratteri: ")
print(frequenze)