'''
Scrivete un programma che utilizza una funzione che accetta
come parametro una stringa passata dall'utente e restituisce in
risposta se è palindroma o no.
Esempio:
'I topi non avevano nipoti' è palindroma
'Ciao' non è palindroma
'''

def controlla_palindroma(frase):
    frase_pulita = frase.lower()   # Tutto in minuscolo.

    frase_pulita = frase_pulita.replace(" ", "")    # Prende il primo elemento della stringa (uno spazio) e lo sostituisce con letteralmente niente, così da rendere una frase come "I topi non avevano nipoti" in "itopinonavevanonipoti".

    frase_invertita = frase_pulita[::-1]    # [::-1] serve per leggere una stringa al contrario.

    if frase_pulita == frase_invertita:
        return True
    else:
        return False

testo_utente = input("Inserisci una parola o una frase: ")

if controlla_palindroma(testo_utente):
    print(f"'{testo_utente}' è palindroma.")
else:
    print(f"'{testo_utente}' non è palindroma.")