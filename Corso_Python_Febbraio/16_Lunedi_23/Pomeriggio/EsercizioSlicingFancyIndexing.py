'''
Esercizio su NumPy Slicing

Consegna:
1. Crea un array NumPy 1D di 20 numeri interi casuali compresi da 10 e 50.
2. Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
3. Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
4. Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
5. Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
6. Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.

Obiettivo: esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande.
'''

'''
Inizio: Da quale indice partire (incluso). Se ometti il numero, parte da 0.

Fine: A quale indice fermarsi (escluso). Se ometti il numero, arriva fino alla fine dell'array.

Passo: Di quanti elementi saltare alla volta. Se ometti il numero, va di 1 in 1.
'''

import numpy as np

array_originale = np.random.randint(10, 51, size=20)    # "Random" per creare un array di 20 numeri interi casuali compresi tra 10 e 50.
print("1. Array originale:")
print(array_originale)

# Estrazione dei primi 10 elementi.
primi_10 = array_originale[:10] # :10 indica che vogliamo partire dall'inizio dell'array (indice 0) e arrivare fino all'indice 10 (escluso).
print("2. Primi 10 elementi:")
print(primi_10)

# Estrazione degli ultimi 5 elementi.
ultimi_5 = array_originale[-5:] # -5: indica che vogliamo partire dall'indice -5 (quindi 5 elementi prima della fine dell'array) e arrivare fino alla fine dell'array.
print("3. Ultimi 5 elementi:")
print(ultimi_5)

# Estrazione degli elementi dall'indice 5 all'indice 15 (escluso).
da_5_a_15 = array_originale[5:15]   # 5:15 indica che vogliamo partire dall'indice 5 e arrivare fino all'indice 15 (escluso).
print("4. Elementi dall'indice 5 all'indice 15 (escluso):")
print(da_5_a_15)

# Estrazione di ogni terzo elemento.
ogni_terzo = array_originale[2::3]   # Aggiungo "2" a "::3" per iniziare a estrarre dal terzo elemento (indice 2) e poi saltare di 3 in 3.
print("5. Ogni terzo elemento:")
print(ogni_terzo)

# Modifica tramite slicing.
array_modificato = array_originale.copy()  # Creo una copia per modificare.
array_modificato[5:10] = 99 # 5:10 indica che vogliamo partire dall'indice 5 e arrivare fino all'indice 10 (escluso), e assegnare a questi elementi il valore 99.

# Stampa dell'array modificato.
print("6 e 7. Array modificato (indici da 5 a 10 sostituiti con 99): ")
print(array_modificato)