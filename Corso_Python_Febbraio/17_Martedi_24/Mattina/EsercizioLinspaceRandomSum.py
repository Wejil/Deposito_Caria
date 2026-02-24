'''
Descrizione: Crea un array utilizzando linspace, cambia la sua
forma con reshape, genera un array casuale e calcola la somma degli elementi.

Esercizio:
1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
2. Cambia la forma dell'array a una matrice 3x4.
3. Genera una matrice 3x4 di numeri casuali tra 0 e 1.
4. Calcola e stampa la somma degli elementi di entrambe le matrici.
'''

import numpy as np

print("1 e 2. Creazione con linspace e reshape")
array_lineare = np.linspace(0, 1, 12)   # Creo 12 numeri equidistanti tra 0 e 1.
matrice_linspace = array_lineare.reshape(3, 4)  # Array 1D in una matrice 2D (3 righe e 4 colonne).

print("Matrice generata con linspace (3x4):")
print(matrice_linspace)

print("3. Matrice casuale (random)")
matrice_casuale = np.random.rand(3, 4)  # Genero una matrice 3x4 di numeri casuali tra 0 e 1.

print("Matrice generata con random (3x4):")
print(matrice_casuale)

print("4. Calcolo delle somme")
somma_linspace = np.sum(matrice_linspace)  # Somma degli elementi della matrice linspace.
somma_casuale = np.sum(matrice_casuale)  # Somma degli elementi della matrice casuale.

print(f"Somma degli elementi della matrice linspace: {somma_linspace}")
print(f"Somma degli elementi della matrice casuale: {somma_casuale}")