x = 4
y = "pippo"
z = True

lista = [x, y, z]

numeri = [1, 2, 3, 4, 5] # Insieme di liste numeriche
nomi = ["Alice", "Bob", "Charlie"] # Insieme di liste letterali
misto = [1, "due", True, 4.5] # Insieme di liste miste

print(numeri[0]) # Output: 1, poiché 1 in posizione 0.
print(numeri[2]) # Output: 3, poiché 3 in posizione 2.

print(lista[4]) # IndexError: list index out of range. Poiché la lista ha meno di 5 elementi (cioè se non esiste l'indice 4).

# Metodi incorporati per lavorare con le liste
numeri = [3, 1, 4, 2, 5]
print(len(numeri)) # Per ottenere la lunghezza della lista, dunque output: 5.
numeri.append(6)
print(numeri) # Per aggiungere un elemento alla fine della lista, dunque all'output si aggiunge il 6.
numeri.insert(2,10)
print(numeri) # Per aggiungere uno o più elementi (2 e 10) in una posizione specifica, dunque l'output sarà [3, 1, 10, 4, 2, 5, 6]
numeri.remove(4)
print(numeri) # Per rimuovere uno o più elementi (4), dunque l'output sarà senza il numero 4.
numeri.sort()
print(numeri) # Per ordinare gli elementi della lista.

# Tuple
punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

# Non si può assegnare un nuovo valore alla posizione
punto = (3, 4)
punto[0] = 5 # Dà errore: TypeError: 'tuple' object does not support item assignment. Si corregge trasformando la tupla in una lista. La tupla ha dei meccanismi nascosti.

# Creazione di tuple senza parentesi tonde
punto = 3, 4 # Tuple packing
x, y = punto # Tuple unpaking
print (x, y) # Darà come output 3 e 4.

# Trasformare una tupla in una lista
tupla = 2, 3, 4
lista = list(tupla) # Dunque ora sarà modificabile.

# Insiemi
set1 = set([1, 2, 3, 4, 5])
set2 = {4, 5, 6, 7, 8}
# Gli insiemi non contengono elementi duplicati e se si prova ad aggiungerli, verranno ignorati.
set3 = {1, 2, 3, 3, 4, 4, 5}
print(set3) # Darà come output {1, 2, 3, 4, 5} ignorando i dpulicati.

# Unione, intersezione, differenza e differenza simmetrica.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}. Ignorerà i duplicati.
print(set1.intersection(set2)) # Output: {4, 5}. Manderà solo i numeri comuni.
print(set1.difference(set2)) # Output: {1, 2, 3}. Manderà solo quelli non presenti nel secondo insieme, ma presenti nell'insieme di partenza.
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}. Manderà gli elementi presenti in uno dei due insiemi, ma non in entrambi.