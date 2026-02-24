'''
Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D.
Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie
operazioni sulla matrice. Le operazioni disponibili includono, ogni volta che il sistema
conclude un calcolo va salvato su un file txt:
1. Creare una nuova matrice 2D di dimensioni specificate da utente con numeri casuali.
2. Estrarre e stampare la sotto-matrice centrale.
3. Trasporre la matrice e stamparla.
4. Calcolare e stampare la somma di tutti gli elementi della matrice.
5. Uscire dal programma o ripetere.

Parte DUE: Andare a specializzare per aggiungere nuove operazioni:
6. Moltiplicazione Element-wise con un'altra Matrice: l'utente può scegliere di creare una
seconda matrice delle stesse dimensioni della prima e moltiplicarle elemento per elemento
e stampare il risultato.
7. Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di
tutti gli elementi della matrice.

Extra:
Determinante della Matrice: Calcolare e stampare il determinante della matrice (solo se la
matrice è quadrata).
'''

import numpy as np

def salva_su_file(titolo_operazione, risultato):
    with open("risultati_operazioni.txt", "a") as file:
        file.write(f"{titolo_operazione}")
        file.write(str(risultato)+ "\n")

def main():
    print("Gestore di Matrici 2D con NumPy.")
    matrice = None # Inizializzo la matrice come vuota.

    while True:
        print("Menu interattivo:")
        print("1. Crea una nuova matrice 2D (scegli dimensioni).")
        print("2. Estrai e stampa la sotto-matrice centrale.")
        print("3. Trasponi la matrice.")
        print("4. Calcola la somma di tutti gli elementi.")
        print("5. Moltiplicazione Element-wise con un'altra matrice.")
        print("6. Calcola la media degli elementi.")
        print("7. Calcola il determinante (solo se quadrata).")
        print("0. Esci dal programma.")

        scelta = input("Scegli un'operazione (0-7): ").strip()

        if scelta == "0":
            print("Uscita dal programma.")
            break
        elif scelta == "1":
            try:
                righe = int(input("Inserisci il numero di righe: "))
                colonne = int(input("Inserisci il numero di colonne: "))
                matrice = np.random.randint(1, 11, size=(righe, colonne))
                print("Matrice creata:")
                print(matrice)
                salva_su_file("Creazione matrice originale", matrice)
            except ValueError:
                print("Input non valido.")

        elif scelta == "2":
            if matrice.shape[0] > 2 and matrice.shape[1] > 2:
                sotto_matrice = matrice[1:-1, 1:-1]
                print("Sotto-matrice centrale:")
                print(sotto_matrice)
                salva_su_file("Sotto-matrice centrale", sotto_matrice)
            else:
                messaggio = "La matrice è troppo piccola per estrarre una sotto-matrice centrale."
                print(f"{messaggio}")
                salva_su_file("Errore sotto-matrice centrale", messaggio)
        
        elif scelta == "3":
            trasposta = matrice.T # Traspongo la matrice usando .T.
            print("Matrice trasposta:")
            print(trasposta)
            salva_su_file("Matrice trasposta", trasposta)
        
        elif scelta == "4":
            somma = np.sum(matrice)
            print(f"La somma di tutti gli elementi è: {somma}")
            salva_su_file("Somma di elementi", somma)
        
        elif scelta == "5":
            # Moltiplicazione Element-wise.
            print("Generazione di una nuova matrice delle stesse dimensioni.")
            matrice_2 = np.random.randint(1, 11, size=matrice.shape)
            print("Seconda matrice:")
            print(matrice_2)

            moltiplicazione = matrice * matrice_2
            print("Risultato della moltiplicazione element-wise:")
            print(moltiplicazione)
            
        elif scelta == "6":
            media = np.mean(matrice)
            print(f"La media di tutti gli elementi è: {media}")
            salva_su_file("Media di elementi", media)
        
        elif scelta == "7":
            # Calcolo del determinante solo se la matrice è quadrata.
            righe, colonne = matrice.shape
            if righe == colonne:
                determinante = round(np.linalg.det(matrice), 2) # Calcolo il determinante e lo arrotondo a 2 decimali.
                print(f"Il determinante della matrice è: {determinante}")
            else:
                messaggio = f"Impossibile calcolare il determinante: la matrice non è quadrata (dimensioni: {righe}x{colonne})."
                print(messaggio)
                salva_su_file("Errore determinante", messaggio)
        
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()