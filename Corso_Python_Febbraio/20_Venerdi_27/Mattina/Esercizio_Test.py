'''
Simulazione vendite giornaliere di Smartphone e Laptop in un negozio per l'anno 2025.
Calcolo il ricavo totale giornaliero, campioni di dati usando slicing e fancy indexing per controlli,
visualizzazione dell'andamento annuale e dei ricavi medi mensili per capire i trend di acquisto.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Generazione dei dati.
giorni = 365

# Creazione date per l'indice.
date_vendite = pd.date_range(start='2025-01-01', periods=giorni, freq='D')

# Uso di NumPy per generare numeri interi casuali (quindi la quantità vendute ogni giorno).
vendite_smartphone = np.random.randint(10, 50, size=giorni) # Venduti tra 10 e 50 smartphone al giorno.
vendite_laptop = np.random.randint(2, 15, size=giorni)  # Venduti tra 2 e 15 laptop al giorno.

# Prezzi dei prodotti (fissi).
prezzo_smartphone = 800
prezzo_laptop = 1200

# Creazione DataFrame con Pandas.
df = pd.DataFrame({
    'Qta_Smartphone': vendite_smartphone,
    'Qta_Laptop': vendite_laptop
}, index=date_vendite)

# Calcolo del ricavo totale giornaliero.
df['Ricavo_Totale'] = df['Qta_Smartphone'] * prezzo_smartphone + df['Qta_Laptop'] * prezzo_laptop

print("Dimostrazione estrazione dati con slicing e fancy indexing:")
prima_settimana = df.iloc[0:7]  # Slicing per la prima settimana. .iloc è usato per indicizzare per posizione (da indice 0 a indice 7 escluso).
print("Vendite della prima settimana:")
print(prima_settimana[['Ricavo_Totale']])

giorni_specifici = ['2025-02-14', '2025-08-15', '2025-12-25']  # Giorni specifici (San Valentino, Ferragosto, Natale).
giorni_campione = df.loc[giorni_specifici]
print("\nVendite nei giorni specifici (San Valentino, Ferragosto, Natale):")
print(giorni_campione[['Ricavo_Totale']])

# Analisi dei dati mensili. Calcolo della media mobile a 14 giorni per vedere il trend.
df['Media_Mobile_Ricavo'] = df['Ricavo_Totale'].rolling(window=14).mean()

df['Mese'] = df.index.month # Estraggo il mese dall'indice datetime per il raggruppamento.
ricavo_medio_mensile = df.groupby('Mese')['Ricavo_Totale'].mean()

# Visualizzazione di due grafici in un'unica figura.
sns.set_theme(style="darkgrid")

plt.figure('Analisi Vendite Store', figsize=(14, 10), dpi=100)

# Grafico 1: trend dei ricavi giornalieri (sopra).
plt.subplot(2, 1, 1)
plt.plot(df.index, df['Ricavo_Totale'], color='lightgrey', label='Ricavo Singolo Giorno', alpha=0.7)
plt.plot(df.index, df['Media_Mobile_Ricavo'], color='blue', linewidth=2, label='Trend (Media Mobile 14 giorni)')

plt.title('Andamento Ricavi Giornalieri nel 2025', fontsize=16)
plt.xlabel('Data')
plt.ylabel('Ricavo Totale (€)')
plt.legend()

# Grafico 2: ricavo medio mensile (sotto).
plt.subplot(2, 1, 2)
mesi_nomi = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
sns.barplot(x=mesi_nomi, y=ricavo_medio_mensile.values, palette='magma')

plt.title('Ricavo Medio Giornaliero per Mese', fontsize=16)
plt.xlabel('Mese')
plt.ylabel('Ricavo Medio (€)')

plt.tight_layout()
plt.show()