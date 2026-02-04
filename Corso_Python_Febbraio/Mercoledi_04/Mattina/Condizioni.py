# Condizione "if", se.
x = 10
y = 20

if (x < y): # Funziona anche senza le parentesi
    print("bravo") # Print si trova dentro l'if, altrimenti dà errore.

if x < y: # Senza le parentesi
    print("bravo")
    print("bravo") # Bisogna sempre mettere tutto dentro l'if, altrimenti: errore.

# if - else (altrimenti)
numero = 10
if numero > 0:
    print("Il numero è positivo") # In questo caso non andrà oltre all'else.
else:
    print("Blocco Else")

numero = -10
if numero > 0:
    print("Il numero è positivo")
else:
    print("Blocco Else") # Si arriva all'else, poiché il numero non è maggiore di zero, dunque non positivo.

# if - else, elif
numero = 10
if numero > 0: # Solo se il numero è superiore a zero controllerà se è uguale a 100.
    print("Il numero è positivo")
    if numero == 100:
        print("wow")
elif numero < 0: # Se il numero non è superiore a zero, andrà nell'elif. Si possono avere infinito elif in mezzo.
    print("Il numero è negativo")
else:
    print("Il numero è zero")

if x < y:
    print("bravo")
    if x == 110: # If nell'If. Possibile finché coerente.
        print("sei 110")
else: # Descrive l'altrimenti
    print("Else")

# Match in Python
comando = input("Inserisci un comando: ")
match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")

