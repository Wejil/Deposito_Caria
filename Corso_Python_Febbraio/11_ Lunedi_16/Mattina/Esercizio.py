'''
Create un programma che richiede all'utente tre numeri e verifica la presenza di almeno due numeri uguali, se non ci sono ci restituisce il numero più grande dei tre.
'''
# Input
n1 = float(input("Inserisci il primo numero: "))
n2 = float(input("Inserisci il secondo numero: "))
n3 = float(input("Inserisci il terzo numero: "))

# Controllo delle uguaglianze
if n1 == n2 or n1 == n3 or n2 == n3:    # Uguaglianza con or
    print("Ci sono almeno due numeri uguali.")
else:
    if n1 > n2 and n1 > n3:
        piu_grande = n1
    elif n2 > n1 and n2 > n3:
        piu_grande = n2
    else:
        piu_grande = n3
    
    print(f"Tutti i numeri sono diversi. Il più grande è: {piu_grande}")