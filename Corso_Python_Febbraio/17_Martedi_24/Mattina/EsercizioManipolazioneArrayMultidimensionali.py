'''
Manipolazione di Array Multidimensionali.
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
'''

import numpy as np

print("1. Creazione della matrice 5x5.")
matrice = np.arange(1, 26).reshape(5, 5) # Creo una matrice 5x5 con numeri da 1 a 25.
print("Matrice:")
print(matrice)

print("2. Estrazione della seconda colonna.")
seconda_colonna = matrice[:, 1] # Estrazione della seconda colonna (indice 1).

print("Seconda colonna:")
print(seconda_colonna)

print("3. Estrazione della terza riga.")
terza_riga = matrice[2, :] # Estrazione della terza riga

print("Terza riga:")
print(terza_riga)

print("4. Calcolo della somma degli elementi della diagonale principale.")
diagonale = np.diag(matrice) # Estrazione della diagonale principale.
somma_diagonale = np.sum(diagonale) # Calcolo della somma degli elementi della diagonale.

print(f"Elementi della diagonale: {diagonale}")
print(f"Somma degli elementi della diagonale principale: {somma_diagonale}")