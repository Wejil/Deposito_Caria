'''
Consegna:
1. Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
2. Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
3. Somma i due array elemento per elemento per ottenere un nuovo array.
4. Calcola la somma totale degli elementi del nuovo array.
5. Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
6. Stampa gli array originali, il nuovo array risultante della somma e le somme calcolate.
7. Salva i dati su un file TXT a ogni giro
8. Rendi ripetibile il processo complessivo
9. Chiedi se si vuole sovrascrivere il TXT o no.

Obiettivo:
Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, random
per creare array di numeri casuali, e sum per eseguire operazionidi somma
sugli array, incluso l'uso di condizioni per la somma parziale e gestire il
salvataggio di file in merito.
'''

import numpy as np

def main():
    print("Generatore e analizzatore di array.")

    # Processo complessivo ripetibile.
    while True:
        # Richiesta se si vuole sovrascrivere il file txt o no.
        scelta_file = input("Vuoi sovrascrivere il file esistente ('s') o aggiungere i dati in coda ('a')? [s/a]: ").strip().lower()

        if scelta_file == 's':
            modalita = 'w'  # Sovrascrive (write).
        else:
            modalita = 'a'  # Aggiunge alla fine (append).

        array_lin = np.linspace(0, 10, 50)  # 50 numeri equidistanti tra 0 e 10.
        array_rand = np.random.random(50)  # 50 numeri casuali tra 0 e 1.
        array_somma = array_lin + array_rand  # Somma elemento per elemento.
        somma_totale = np.sum(array_somma)  # Somma totale degli elementi del nuovo array.
        somma_maggiori_5 = np.sum(array_somma[array_somma > 5])  # Somma degli elementi maggiori di 5.

        # Stampa dei risultati.
        print("Array linspace (0-10):")
        print(array_lin)
        print("Array random (0-1):")
        print(array_rand)
        print("Array risultante della somma:")
        print(array_somma)
        print(f"Somma totale degli elementi del nuovo array: {somma_totale}")
        print(f"Somma degli elementi del nuovo array maggiori di 5: {somma_maggiori_5}")

        # Salvataggio dei dati su un file TXT.
        with open("dati_array.txt", modalita) as file:
            file.write("Nuovo salvataggio:")
            file.write("Array Linspace:" + str(array_lin) + "")
            file.write("Array Random:" + str(array_rand) + "")
            file.write("Array Somma:" + str(array_somma) + "")
            file.write(f"Somma Totale: {somma_totale}")
            file.write(f"Somma Maggiori di 5: {somma_maggiori_5}")
        
        print("Dati salvati su 'dati_array.txt'.")

        # Richiesta se si vuole ripetere il processo.
        continua = input("Vuoi eseguire nuovamente il processo? [s/n]: ").strip().lower()
        if continua != 's':
            print("Processo terminato.")
            break

# Avvio del programma.
main()

