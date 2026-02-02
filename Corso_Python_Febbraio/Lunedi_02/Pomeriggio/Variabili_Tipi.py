nome = "valerio"
numero = 1

print(nome, numero) # Versione "semplificata"
print("Questo e' il mio nome: ", nome, "Questo e' il mio numero: ", numero) # Versione più elaborata

nome = input("Inserisci il tuo nome: ")
eta = int( input("Inserisci la tua eta': "))
print ("Ciao, " + nome + "! Benvenuto in Python!")

# Prova operatori
x = 3
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)

ilaria_ = "1" 
ilaria_ = 1

x = 10 # Variabile intera
a = 3.14 # Variabile float

numero = str(100) # Stringhe: insieme di valori

s = "Giorno"
print(s[0])

# Esempi di manipolazioni di stringhe
s = "Ciao, mondo!"
print(len(s)) # len: ottenere la lunghezza di una stringa
print(s.upper()) # upper: convertire una stringa in maiuscolo
print(s.lower()) # lower: convertire una stringa in minuscolo
print(s.split(',')) #split: divide una stringa in una lista di sottostringe in base al delimitatore (in questo caso la virgola, ma puo' essere qualsiasi)
print(s.replace('mondo', 'universo')) #replace: per sostituire una parte di stringa con un'altra e molti altri

# booleani
booleanT = True
booleanF = False
print ( booleanT, booleanF )

booleanT = True
booleanF = int(False) # Stampa 0
print( booleanF )

print ( 5 > 10 ) # Esempio: falso

x = 5
y = 10

print(x == y) # uguale a
print(x != y) # diverso da
print(x < y) # minore di
print(x > y) # maggiore di
print(x <= y) # minore o uguale di
print(x >= y) # maggiore o uguale di