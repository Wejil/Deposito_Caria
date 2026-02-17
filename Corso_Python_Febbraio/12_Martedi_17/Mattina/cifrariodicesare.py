'''Scrivete un programma che utilizza il cifrario di Cesare per criptare una
parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
di posti corrispondente alla chiave.'''
#parole=['ciao','gg','tutti']
risultato = ""
alfabeto='abcdefghijklmnopqrstuwxyz'
parola=input('inserisci una parola:')
scelta=input('decriptare o criptare')
#index=0
for lettera in parola:
    if lettera in alfabeto:
        posizione=alfabeto.index(lettera)
        #nuova_posizione = (posizione + 3) % len(alfabeto)
        if scelta=='criptare':
            #posizione+=3
            nuova_posizione = (posizione + 3) % len(alfabeto)
            risultato += alfabeto[nuova_posizione]
        else:
             nuova_posizione = (posizione - 3) % len(alfabeto)        
             risultato += alfabeto[nuova_posizione]
            
    else:
        print("non c'è")
print("Risultato finale:", risultato)

'''while index<len(parole):
            if lettera[index] in alfabeto:  
                print(parole,lettera[index],index)
            index+=1'''

'''def muovi(parola, posizione):
    return parola + posizione
muovi('ciao','3')'''