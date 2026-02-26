'''
Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà.

Dataset:
- ID_Cliente: Identificativo unico per ogni cliente
- Età: Età del cliente
- Durata_Abbonamento: Quanti mesi il cliente è stato abbonato
- Tariffa_Mensile: Quanto il cliente paga al mese
- Dati_Consumati: GB di dati consumati al mese
- Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
- Churn: Se il cliente ha lasciato la compagnia (Sì/No)

1. Caricamento e Esplorazione Inziale:
- Caricare i dati da un file CSV.
- Utilizzare info(), describe() e value_counts() per esaminare la distribuzione dei dati e identificare colonne con valori mancanti.
2. Pulizia dei Dati:
- Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
- Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
3. Analisi Esplorativa dei Dati (EDA):
- Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
- Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abbonamento, Tariffa_mensile e la Churn.
- Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
4. Preparazione dei Dati per la Modellazione:
- Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
- Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
5. Analisi Statistica e Predittiva:
- Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata su altri fattori.
- Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve).
'''

import pandas as pd
import numpy as np

def prepara_dataset_telecom():
    np.random.seed(42)
    n_clienti = 200

    dati = {
        "ID_Cliente": range(1001, 1001 + n_clienti),
        "Età": np.random.normal(40, 15, n_clienti).astype(int),
        "Durata_Abbonamento": np.random.randint(1, 72, n_clienti).astype(float),
        "Tariffa_Mensile": np.random.uniform(9.99, 89.99, n_clienti),
        "Dati_Consumati": np.random.uniform(1.0, 100.0, n_clienti), # GB
        "Servizio_Clienti_Contatti": np.random.randint(0, 10, n_clienti),
        "Churn": np.random.choice(["Sì", "No"], n_clienti, p=[0.25, 0.75])
    }

    df_finto = pd.DataFrame(dati)

    # Introduco alcuni valori mancanti e anomalie.
    df_finto.loc[5, "Età"] = -15 # Età negativa.
    df_finto.loc[10, "Tariffa_Mensile"] = 9999.0 # Tariffa mensile irrealistica.
    df_finto.loc[20, "Durata_Abbonamento"] = np.nan # Valore mancante.
    df_finto.loc[50, "Durata_Abbonamento"] = np.nan # Valore mancante.

    df_finto.to_csv("telecom_churn.csv", index=False)
    print("Fase 0: Dataset generato e salvato come 'telecom_churn.csv'.")

prepara_dataset_telecom()

# Controllo del dataset e analisi iniziale.
print("1. Caricamento e Esplorazione Iniziale:")
df = pd.read_csv("telecom_churn.csv")
print("Informazioni sul dataset:")
df.info()

print("\nStatistiche descrittive:")
print(df.describe())

print("\nDistribuzione churn:")
print(df["Churn"].value_counts())

print("\n2. Pulizia dei Dati:")
# Gestione dei valori mancanti e sostituzione con la mediana della colonna.
mediana_durata = df["Durata_Abbonamento"].median()
df["Durata_Abbonamento"] = df["Durata_Abbonamento"].fillna(mediana_durata)

# Correzione delle anomalie, ovvero età negative e tariffe mensili irrealistiche.
# Sostituzione delle età < 18 con l'età mediana.
mediana_eta = df.loc[df["Età"] >= 18, "Età"].median()
df.loc[df["Età"] < 18, "Età"] = mediana_eta # Trova le righe in cui l'età è minore di 18; posizionati sulla colonna 'Età' di quelle righe specifiche; sovrascrivi il valore con la mediana.

# Sostituzione delle tariffe mensili > 200 con la mediana.
mediana_tariffa = df.loc[df["Tariffa_Mensile"] <= 200, "Tariffa_Mensile"].median()
df.loc[df["Tariffa_Mensile"] > 200, "Tariffa_Mensile"] = mediana_tariffa

print("Anomalie corrette e valori mancanti gestiti.")

print("\n3. Analisi Esplorativa dei Dati (EDA):")
# Creazione della colonna Costo_per_GB.
df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"]
# Relazione tra Età, Durata, Tariffa e Churn.
print("Medie raggruppate per Churn:")
colonne_analisi = ["Età", "Durata_Abbonamento", "Tariffa_Mensile"]
print(df.groupby("Churn")[colonne_analisi].mean())

# Matrice di correlazione.
print("\nMatrice di correlazione:")
colonne_numeriche = df.select_dtypes(include=[np.number]).drop(columns=["ID_Cliente"])
print(colonne_numeriche.corr())

print("\n4. Preparazione dei Dati per la Modellazione:")
# Conversione della colonna Churn in formato numerico (0 per "No", 1 per "Sì") usando il metodo map().
df["Churn"] = df["Churn"].map({"No": 0, "Sì": 1})

# Normalizzazione delle colonne numeriche usando numpy.
colonne_da_normalizzare = ["Età", "Durata_Abbonamento", "Tariffa_Mensile", "Dati_Consumati", "Servizio_Clienti_Contatti", "Costo_per_GB"]

for col in colonne_da_normalizzare:
    minimo = np.min(df[col])
    massimo = np.max(df[col])
    # Normalizzazione min-max.
    df[col] = (df[col] - minimo) / (massimo - minimo)

print("Dati preparati per la modellazione.")
print(df[["Età", "Tariffa_Mensile", "Churn", "Costo_per_GB"]].head())