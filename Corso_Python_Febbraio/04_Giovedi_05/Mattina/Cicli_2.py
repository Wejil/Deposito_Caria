# Controllori dei cicli

# break(for)
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        break
    print(numero)

# continue(for)
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        continue
    print(numero)

# pass(for)
if True:
    # Qui si abbina un commento del tipo "qui andrà un controllo su..."
    pass
while True:
    # Qui si abbina un commento del tipo "qui andrà un controllo su..."
    pass

for i in range(5):
    if i == 3:
        pass
    print(i)

# Operatore splat
numeri = [*range(1, 11)]
print(numeri) # L'output sarà: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]