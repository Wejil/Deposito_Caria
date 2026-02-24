'''
Somma e Media di Elementi.
Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
Calcolare e stampare la somma di tutti gli elementi dell'array.
Calcolare e stampare la media di tutti gli elementi dell'array.
'''

import numpy as np

array_numeri = np.random.randint(1, 101, size=15) # Creo un array di 15 numeri casuali tra 1 e 100.
somma_totale = np.sum(array_numeri) # Calcolo la somma di tutti gli elementi dell'array.
media_totale = np.mean(array_numeri) # Calcolo la media di tutti gli elementi dell'array.

print("Array generato:")
print(array_numeri)
print(f"Somma totale degli elementi dell'array: {somma_totale}")
print(f"Media degli elementi dell'array: {media_totale}")