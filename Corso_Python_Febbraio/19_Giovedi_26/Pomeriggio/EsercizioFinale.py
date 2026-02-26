'''
L'obiettivo di questo esercizio è generare un set di dati di serie temporali
utilizzando NumPy, analizzarli con pandas e visualizzare i risultati usando
Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:


Generazione dei Dati: Utilizzare NumPy per generare una serie temporale
di 365 giorni di dati, simulando il numero di visitatori giornalieri in
un parco. Assumere che il numero medio di visitatori sia 2000 con una
deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
tempo per simulare l'aumento della popolarità del parco.

Creazione del DataFrame: Creare un DataFrame pandas con le date come
indice e il numero di visitatori come colonna.

Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la
deviazione standard.

Visualizzazione dei Dati:

Creare un grafico a linee del numero di visitatori giornalieri.

Aggiungere al grafico la media mobile a 7 giorni per mostrare la
tendenza settimanale.

Creare un secondo grafico che mostri la media mensile dei visitatori.
'''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
serie temporale
di 365 giorni di dati, simulando il numero di visitatori giornalieri in
un parco. Assumere che il numero medio di visitatori sia 2000 con una
deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
tempo per simulare l'aumento della popolarità del parco.
"""
data = {
    'date': pd.date_range(start='2025-01-01', periods=365, freq='D'),
    'visitors': (2000 + np.random.normal(loc=0, scale=500, size=365) + np.arange(365) * 5).round().astype(int)
       }

# Creazione del DataFrame
df = pd.DataFrame(data)
print("DataFrame Originale:")
print(df)


# Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la deviazione standard.
df['month'] = df['date'].dt.month

#in questo caso andiamo a raggruppare per mese e calcolare media e deviazione standard dei visitatori
monthly_stats = df.groupby('month')['visitors'].agg(['mean', 'std'])
print("\nStatistiche Mensili:")
print(monthly_stats)

#creo la media mobile a 7 giorni che ci servira per il grafico a linee del numero di visitatori giornalieri
df['visitors_7d_avg'] = df['visitors'].rolling(window=7).mean()

#creazione del grafico a linee del numero di visitatori giornalieri
plt.figure('Visitatori Giornalieri', figsize=(12, 6), dpi=100)
plt.plot(df['date'], df['visitors'], label='Visitatori Giornalieri', color='blue')
plt.title('Grafico Lineare')
plt.xlabel('Date')
plt.ylabel('Visitatori')

plt.plot(df['date'], df['visitors_7d_avg'], label='Media Mobile 7 Giorni', color='red')
plt.legend()
plt.show()


# Creazione del secondo grafico che mostri la media mensile dei visitatori
plt.figure('Media Mensile Visitatori', figsize=(12, 6), dpi=100)
sns.barplot(x=monthly_stats.index, y=monthly_stats['mean'], palette='viridis')
plt.title('Media Mensile dei Visitatori')
plt.xlabel('Mese')
plt.ylabel('Media Visitatori')
plt.show()


# Uniamo i due grafici in un'unica figura
fig, axes = plt.subplots(2, 1, figsize=(12, 8), dpi=100)
# Grafico a linee del numero di visitatori giornalieri
axes[0].plot(df['date'], df['visitors'], label='Visitatori Giornalieri', color='blue')
axes[0].plot(df['date'], df['visitors_7d_avg'], label='Media Mobile 7 Giorni', color='red')
axes[0].set_title('Grafico Lineare')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Visitatori')
axes[0].legend()

# Grafico a barre della media mensile dei visitatori
sns.barplot(x=monthly_stats.index, y=monthly_stats['mean'], palette='viridis', ax=axes[1])
axes[1].set_title('Media Mensile dei Visitatori')
axes[1].set_xlabel('Mese')
axes[1].set_ylabel('Media Visitatori')
plt.tight_layout()
plt.show()