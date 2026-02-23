'''
1. Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
2. Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
3. Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
4. Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
5. Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore di -1.
6. Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.

Obiettivo: esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, applicando operazioni avanzate come l'inversione delle righe e la sostituzione condizionale degli elementi.
'''

import numpy as np

# Creazione della matrice 6x6 (nuumeri da 1 a 100 inclusi).
matrice_originale = np.random.randint(1, 101, size=(6, 6))

print("1. Matrice originale (6x6):")
print(matrice_originale)

# Estrazione della sotto-matrice centrale 4x4.
sotto_matrice = matrice_originale[1:5, 1:5] # Indice righe: da 1 a 5 (escluso 5); Indice colonne: da 1 a 5 (escluso 5).
print("2. Sotto-matrice centrale (4x4):")
print(sotto_matrice)

# Inversione delle righe della matrice estratta.
matrice_invertita = sotto_matrice[::-1, :].copy() # Uso di .copy() per scollegarla dall'originale ed evitare modifiche.
print("3. Matrice invertita (righe invertite):")
print(matrice_invertita)

# Estrazione della diagonale principale.
diagonale = np.diag(matrice_invertita)
print("4. Diagonale principale (Array 1D):")
print(diagonale)

# Sostituzione degli elementi multipli di 3 con -1.
matrice_modificata = matrice_invertita.copy() # Uso di .copy() per evitare modifiche alla matrice invertita.
matrice_modificata[matrice_modificata % 3 == 0] = -1
print("5. Matrice finale (multipli di 3 sostituiti con -1):")
print(matrice_modificata)