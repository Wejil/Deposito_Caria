'''
Crea uno script Python che esegua i seguenti passaggi:
1. Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a 49 più altre 50 posizioni casuali tra 49 e 101.
- Stampa l'array, il suo dtype e la sua shape.
2. Modifica il tipo di dato (dtype) dell'array in float64.
- Verifica e stampa di nuovo dtype e shape.
3. Utilizza lo slicing per ottenere:
- I primi 10 elementi
- Gli ultimi 7 elementi
- Gli elementi dall'indice 5 all'indice 20 escluso
- Ogni quarto elemento dell'array
4. Modifica tramite slicing gli elementi dall'indice 10 a 15 (escluso) assegnando loro il valore 999.
5. Utilizza la fancy indexing per selezionare:
- Gli elementi in posizione (0, 3, 7, 13, 25, 33, 48)
- Tutti gli elementi pari dell'array utilizzando una maschera booleana
- Tutti gli elementi maggiori della media dell'array
6. Stampa:
- L'array originale dopo tutte le modifiche
- Tutti i sotto-array ottenuti tramite slicing e fancy indexing.
'''

import numpy as np

print("1. Creazione dell'array:")
parte_ordinata = np.arange(0, 50) # Genero i primi 50 numeri da 0 a 49.
parte_casuale = np.random.randint(49, 102, size=50) # Genero 50 numeri casuali tra 49 e 101.

array_originale = np.concatenate((parte_ordinata, parte_casuale)) # Unisco i due array in uno solo usando concatenate.

print("Array iniziale:")
print(array_originale)
print(f"Dtype: {array_originale.dtype} | Shape: {array_originale.shape}")

print("2. Modifica del tipo di dato:")
array_float = array_originale.astype(np.float64)

print(f"Nuovo Dtype: {array_float.dtype} | Nuova Shape: {array_float.shape}")

print("3. Slicing:")
primi_10 = array_float[:10]
ultimi_7 = array_float[-7:]
dal_5_al_20 = array_float[5:20]
ogni_quarto = array_float[3::4]

print("4. Modifica tramite slicing:")
array_float[10:15] = 999.0

print("5. Fancy indexing e maschere booleane:")
indici_specifici = array_float[[0, 3, 7, 13, 25, 33, 48]] # Lista di indici specifici.

elementi_pari = array_float[array_float % 2 == 0] # Maschera booleana per selezionare gli elementi pari

media_array = np.mean(array_float) # Calcolo la media dell'array.
maggiori_media = array_float[array_float > media_array] # Estraggo gli elementi maggiori della media.

print("Stampa finale:")
print(array_float) # Stampo l'array originale dopo tutte le modifiche.

print(f"Primi 10 elementi: {primi_10}")
print(f"Ultimi 7 elementi: {ultimi_7}")
print(f"Elementi dall'indice 5 al 20 escluso: {dal_5_al_20}")
print(f"Ogni quarto elemento: {ogni_quarto}")
print(f"Elementi agli indici scelti [0, 3, 7, 13, 25, 33, 48]: {indici_specifici}")
print(f"Elementi pari: {elementi_pari}")
print(f"Media calcolata: {media_array}")
print(f"Elementi maggiori della media: {maggiori_media}")