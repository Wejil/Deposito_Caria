'''
Esercizio Medio: Normalizzazione dei Dati

Testo dell'esercizio:
Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo di persone,
normalizza i dati di altezza e peso usando la normalizzazione min-max (ridimensiona i valori in modo che varino tra 0 e 1).
Assicurati di lasciare inalterata la colonna età; mostra il DataFrame originale e quello modificato.

Fornisci un codice che:
1. Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un DataFrame chiamato df).
2. Applichi la normalizzazione min-max alle colonne altezza e peso.
3. Stampa sia il DataFrame originale sia quello modificato per compararli.
'''
import pandas as pd
import matplotlib.pyplot as plt

# Creazione del DataFrame di esempio.
dati = {
    'altezza': [160, 175, 180, 155, 190], # Altezza in cm
    'peso': [60, 75, 82, 55, 95],  # Peso in kg
    'età': [25, 30, 22, 28, 35] # Età in anni
}
df = pd.DataFrame(dati)

print("Dataframe originale:")
print(df)

# Creazione di una copia del DataFrame per poter fare il confronto.
df_modificato = df.copy()

# Selezione delle colonne da scalare.
colonne_da_scalare = ['altezza', 'peso']

for col in colonne_da_scalare:
    # Calcolo del minimo e del massimo per la colonna.
    minimo = df_modificato[col].min()
    massimo = df_modificato[col].max()

    # Applicazione della formula del min-max scaling.
    df_modificato[col] = (df_modificato[col] - minimo) / (massimo - minimo)

print("\nDataframe modificato (Normalizzato):")
print(df_modificato)

# Creazione di una tela abbastanza larga per ospitare due grafici affiancati.
plt.figure(figsize=(12, 5))

# 1. Istogramma dei dati ORIGINALI (a sinistra)
plt.subplot(1, 2, 1) # (1 riga, 2 colonne, posizione 1)
# Uso di bins=4 per raggruppare i nostri 5 valori in 4 "scaglioni".
plt.hist(df['altezza'], bins=4, color='blue', edgecolor='black')
plt.title('Istogramma Altezza Originale')
plt.xlabel('Altezza (cm)')
plt.ylabel('Frequenza (Numero di persone)')

# 2. Istogramma dei dati NORMALIZZATI (a destra).
plt.subplot(1, 2, 2) # (1 riga, 2 colonne, posizione 2)
plt.hist(df_modificato['altezza'], bins=4, color='green', edgecolor='black')
plt.title('Istogramma Altezza Normalizzata')
plt.xlabel('Altezza (Scala 0.0 - 1.0)')
plt.ylabel('Frequenza (Numero di persone)')

# Mostro i grafici.
plt.tight_layout() # Evita che i titoli e gli assi si sovrappongano.
plt.show()