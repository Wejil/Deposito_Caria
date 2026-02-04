# While (finché)
conteggio = 0 # Conteggio da 0 a finché il while dice non dice True.
while conteggio < 5:
    print(conteggio)
    conteggio += 1 # Logica di rottura, per smettere di ripetere. Altrimenti darebbe sempre 0.

# Ciclo booleano
controllore = True
while controllore:
    print("oh no")

    esci = input("Vuoi uscire? si - no")
    if esci.lower() == "si":
        controllore = False # Dunque finché il booleano (True) non diventa "False" grazie al "si", lui ripeterà all'infinito.
    else:
        controllore = True
else:
    print("While 1 - Il controllore era False.") # Si può usare l'else per entrare nel while. Diventa dunque un auto-debug.

# For
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero) # Numero è un placeholder. Si può mettere anche una lettera o qualsiasi cosa, che però poi deve essere messo anche dentro il print.

stringa = "Giulio" # In questo caso stamperà lettera per lettera.
for parola in stringa: # Il for è deterministico, non può andare in loop (a meno che forzato).
    print(parola)

# range()
# range([start], stop, [step])

for i in range(5):
    print(i)

for c in range(5, 21, 3):
    print(c)

# Impostare un limite che non verrà raggiunto.
limite = int(input("Scegli il tuo limite che non verra' raggiunto: limite"))
for c in range(limite):
    print(c)

