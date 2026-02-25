'''
Esercizio 2: Manipolazione e Aggregazione dei Dati

Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con pandas.
Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse città,
includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.

1. Caricare i dati in un DataFrame.
2. Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra Quantità e Prezzo Unitario.
3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.
4. Trovare il prodotto più venduto in termini di Quantità.
5. Identificare la città con il maggior volume di vendite totali.
6. Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es., 1000 euro).
7. Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.
8. Visualizzare il numero di vendite per ogni città.
'''

import pandas as pd
import random

# Creazione di un file csv.
def prepara_file_vendite():
    prodotti = ["Laptop", "Smartphone", "Tablet", "Monitor", "Tastiera"]
    citta = ["Roma", "Milano", "Napoli", "Torino", "Bologna"]

    # Generazione di dati casuali per le vendite.
    dati_vendite = {
        "Prodotto": [random.choice(prodotti) for _ in range(20)],
        "Quantità": [random.randint(1, 5) for _ in range(20)],
        "Prezzo Unitario": [random.choice([50, 150, 300, 800, 1200]) for _ in range(20)],
        "Città": [random.choice(citta) for _ in range(20)]
    }

    # Salvataggio nel file.
    pd.DataFrame(dati_vendite).to_csv("vendite_hardware.csv", index=False)
    print("File 'vendite_hardware.csv' creato con successo.")

prepara_file_vendite()

# 1. Caricare i dati in un DataFrame.
print("1. Caricamento dati.")
df = pd.read_csv("vendite_hardware.csv")
print(df.head())

# 2. Aggiungere la colonna "Totale Vendite".
print("\n2. Calcolo Totale Vendite.")
df["Totale Vendite"] = df["Quantità"] * df["Prezzo Unitario"]
print(df[["Prodotto", "Quantità", "Prezzo Unitario", "Totale Vendite"]].head())

# 3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite.
print("\n3. Totale vendite per prodotto.")
vendite_per_prodotto = df.groupby("Prodotto")["Totale Vendite"].sum()
print(vendite_per_prodotto)

# 4. Trovare il prodotto più venduto in termini di Quantità.
print("\n4. Prodotto più venduto in termini di Quantità.")
quantita_per_prodotto = df.groupby("Prodotto")["Quantità"].sum()
prodotto_top = quantita_per_prodotto.idxmax()
quantita_top = quantita_per_prodotto.max()
print(f"Il prodotto più venduto è '{prodotto_top}' con {quantita_top} unità vendute.")

# 5. Identificare la città con il maggior volume di vendite totali.
print("\n5. Città con il maggior volume di vendite totali.")
vendite_per_citta = df.groupby("Città")["Totale Vendite"].sum()
citta_top = vendite_per_citta.idxmax()
fatturato_top = vendite_per_citta.max()
print(f"La città con il maggior volume di vendite totali è '{citta_top}' con un fatturato di {fatturato_top} euro.")

# 6. Creare un nuovo DataFrame che mostri solo le vendite superiori a 1000 euro.
print("\n6. Vendite superiori a 1000 euro.")
df_superiori_1000 = df[df["Totale Vendite"] > 1000]
print(df_superiori_1000)

# 7. Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.
print("\n7. DataFrame ordinato per Totale Vendite (decrescente).")
df.sort_values(by="Totale Vendite", ascending=False, inplace=True)
print(df.head())

# 8. Visualizzare il numero di vendite per ogni città.
print("\n8. Numero di vendite per ogni città.")
transazioni_citta = df["Città"].value_counts()
print(transazioni_citta)