'''
Esercizio 1: Analisi Esplorativa dei Dati
Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati usando pandas.
Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni di un gruppo di persone: Nome, Età, Città e Salario.

1. Caricare i dati in un DataFrame autogenerandoli casualmente.
2. Visualizzare le prime e le ultime cinque righe del DataFrame.
3. Visualizzare il tipo di dati di ciascuna colonna.
4. Calcolare statistiche descrittive di base per le colonne numeriche (media, mediana, deviazione standard).
5. Identificare e rimuovere eventuali duplicati.
5. Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna.
6. Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18 anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
7. Salvare il DataFrame pulito in un nuovo file CSV.
'''

import pandas as pd
import numpy as np
import random

def prepara_file_di_partenza():
    nomi = ["Mario", "Luigi", "Giovanna", "Anna", "Paolo", "Francesca", "Elena", "Matteo"]
    citta = ["Roma", "Milano", "Napoli", "Torino", "Firenze"]
    
    # Generazione di dati casuali per il DataFrame.
    dati = {
        "Nome": [random.choice(nomi) for _ in range(12)],
        "Età": [random.randint(15, 75) for _ in range(12)],
        "Città": [random.choice(citta) for _ in range(12)],
        "Salario": [random.randint(20000, 80000) for _ in range(12)]
    }

    df_iniziale = pd.DataFrame(dati)

    # "Sporco" i file per l'esercizio.
    df_iniziale.loc[2, "Età"] = np.nan
    df_iniziale.loc[5, "Salario"] = np.nan
    df_iniziale = pd.concat([df_iniziale, df_iniziale.iloc[[0]]], ignore_index=True)

    # Salva il DataFrame in un file CSV.
    df_iniziale.to_csv("dati.csv", index=False)
    print("File di partenza 'dati.csv' creato con successo.")

prepara_file_di_partenza()


print("1. Caricamento dati dal file.")

# Leggo il csv e trasforma in tabella.
df = pd.read_csv("dati.csv")
print("Dati caricati con successo.\n")

print("2. Prime e ultime cinque righe.")
print("Prime 5 righe:")
print(df.head())
print("\nUltime 5 righe:")
print(df.tail())

print("\n3. Tipi di dati di ciascuna colonna.")
print(df.dtypes)

print("\n4. Statistiche descrittive.")
# Seleziono solo le colonne numeriche per mostrare i tipi di dati.
colonne_num = ["Età", "Salario"]
print(df[colonne_num].agg(['mean', 'median', 'std']))

print("\n5. Rimozione dei duplicati e dei valori mancanti.")
# Rimuovo i duplicati.
righe_prima = len(df)
df.drop_duplicates(inplace=True)
print(f"Rimossi {righe_prima - len(df)} record duplicati.")

# Gestisco i valori mancanti sostituendoli con la mediana.
print("\nValori mancanti prima della sostituzione:")
print(df.isnull().sum())

# Calcolo le mediane e riempio i valori mancanti.
df["Età"] = df["Età"].fillna(df["Età"].median())
df["Salario"] = df["Salario"].fillna(df["Salario"].median())

print("\nValori mancanti dopo la sostituzione:")
print(df.isnull().sum())

print("\n6. Aggiunta della colonna 'Categoria Età'.")
# Con pd.cut creo la colonna "Categoria Età" basata sui range di età.
limiti = [0, 18, 65, 120]
etichette = ["Giovane", "Adulto", "Senior"]

df["Categoria Età"] = pd.cut(df["Età"], bins=limiti, labels=etichette)
print(df[["Nome", "Età", "Categoria Età"]].head(6))

print("\n7. Salvataggio file pulito.")
df.to_csv("dati_2.csv", index=False)
print("Dati puliti salvati con successo in 'dati_2.csv'.")