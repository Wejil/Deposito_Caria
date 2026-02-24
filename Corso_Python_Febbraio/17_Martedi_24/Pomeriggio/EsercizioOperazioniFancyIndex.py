'''
Esercizio: Operazioni con Fancy Indexing.
Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1).
(1, 3), (2, 2) e (3, 0).
Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array
(considerando la numerazione delle righe che parte da 0).
Modificare gli elementi sleezionati nel primo punto dell'esercizio aggiungendo 10
al loro valore.
'''

import numpy as np

print("1. Creazione della matrice 4x4.")
matrice = np.random.randint(10, 51, size=(4, 4)) # Genero interi tra 10 e 50 (51 escluso).

print("Matrice originale:")
print(matrice)

print("2. Selezione con Fancy Indexing.")
# Septto le coordinate in due liste separate per righe e colonne.
indici_righe = [0, 1, 2, 3]
indici_colonne = [1, 3, 2, 0]

elementi_selezionati = matrice[indici_righe, indici_colonne] # Seleziono gli elementi usando fancy indexing.
print(f"Elementi estratti agli indici richiesti: {elementi_selezionati}")

print("3. Selezione delle righe dispari.")
righe_dispari = matrice[1, 3] # Seleziono le righe dispari (1 e 3).

print("Righe dispari selezionate:")
print(righe_dispari)

print("4. Modifica degli elementi selezionati.")
# Aggiungo 10 agli elementi selezionati.
matrice[indici_righe, indici_colonne] += 10

print("Matrice modificata (aggiunto 10 agli elementi selezionati):")
print(matrice)