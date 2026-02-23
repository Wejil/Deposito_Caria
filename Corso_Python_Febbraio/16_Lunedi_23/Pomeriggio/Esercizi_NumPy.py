'''
Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.

Esercizio:
1. Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
2. Verifica il tipo di dato dell'array e stampa il risultato.
3. Cambia il tipo di dato dell'array in float64 (o 32) e verifica di nuovo il tipo di dato.
4. Stampa la forma dell'array.
'''

import numpy as np

print("1. Creazione dell'array.")
mio_array = np.arange(10, 50)
print(mio_array)

print("\n2. Verifica del tipo di dato (dtype).")
tipo_originale = mio_array.dtype
print(f"Tipo di dato originale: {tipo_originale}")

print("\n3. Cambio del tipo di dato in float64.")
array_float = mio_array.astype(np.float64)

# Verifica del nuovo tipo di dato.
nuovo_tipo = array_float.dtype
print(f"Nuovo tipo di dato: {nuovo_tipo}")
print(array_float)

print("\n4. Stampa della forma dell'array.")
forma_array = array_float.shape
print(f"Forma dell'array: {forma_array}")