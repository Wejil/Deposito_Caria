'''
Esercizio 1: Analisi di Vendite Fittizie.
Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite generato casualmente,
applicando le tecniche di pivot e groupby.

Descrizione: Gli studenti dovranno generare un DataFrame di vendite che include i seguenti
campi: "Data", "Città", "Prodotto" e "Vendute". I dati devono essere generati per un periodo
di un mese, con vendite registrate per tre diverse città e tre tipi di prodotti.

1. Generazione dei Dati: Utilizzare numpy per creare un set di dati casuali.
2. Creazione della Tabella Pivot: Creare una tabella pivot per analizzare le vendite
medie di ciascun prodotto per città.
3. Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le vendite
totali per ogni prodotto.
'''

import pandas as pd
import numpy as np

# 1. Generazione dei Dati
print("1. Generazione dei dati casuali.")
np.random.seed(42)

# Definisco i domini da cui estrarre i dati.
citta_lista = ['Roma', 'Milano', 'Napoli']
prodotti_lista = ['Laptop', 'Smartphone', 'Tablet']
# Genero le date per un mese.
date_mese = pd.date_range(start='2024-01-01', end='2024-01-31')

# Genero 100 righe di transazioni tramite NumPy.
num_transazioni = 100
dati = {
    "Data": np.random.choice(date_mese, num_transazioni),
    "Città": np.random.choice(citta_lista, num_transazioni),
    "Prodotto": np.random.choice(prodotti_lista, num_transazioni),
    "Vendute": np.random.randint(1, 21, size=num_transazioni) # Vendite tra 1 e 20.
}

# DataFrame e ordine per data.
df = pd.DataFrame(dati).sort_values(by="Data").reset_index(drop=True)

print("Prime 5 righe del DataFrame generato:")
print(df.head())

print("2. Tabella Pivot (Media vendite per prodotto in ogni città).")
tabella_pivot = pd.pivot_table(
    df,
    values='Vendute',
    index='Città',
    columns='Prodotto',
    aggfunc='mean', # Calcola la media delle vendite.
)

print(tabella_pivot.round(2)) # Arrotondo a 2 decimali per una migliore leggibilità.

print("3. GroupBy (Vendite totali per prodotto).")
# Raggruppo per prodotto e sommo le vendite.
vendite_totali = df.groupby("Prodotto")["Vendute"].sum()
print(vendite_totali)