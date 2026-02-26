'''
Esercizio Facile: Calcolo di Statistiche di Base

Testo dell'esercizio:
Hai a disposizione un dataset, che devi autogenerare, contenuto in un DataFrame pandas
con una singola colonna temperature che rappresenta la temperatura giornaliera in una città per un mese.

Scrivi un programma Python che calcoli e stampi le seguenti statistiche:
- La temperatura massima
- La temperatura minima
- La temperatura media
- La mediana delle temperature
'''

import matplotlib.pyplot as plt
import numpy as np

# Generazione dei dati.
# Creazione di 30 giorni (da 1 a 30) per l'asse x.
x = np.arange(1, 31)
# Generazione di 30 temperature casuali tra 15 e 35 gradi per l'asse Y.
y = np.random.uniform(15, 35, 30).round(1)


# Calcolo e stampa delle statistiche di base.
print("Temperatura Massima:", np.max(y))
print("Temperatura Minima:", np.min(y))
print("Temperatura Media:", np.mean(y).round(1))
print("Temperatura Mediana:", np.median(y))


# Creazione del Grafico (lineare).

plt.figure()
plt.plot(x, y)
plt.title('Andamento Temperature Mensili')
plt.xlabel('Giorno del Mese')
plt.ylabel('Temperatura (°C)')
plt.show()


# Grafico 2.
import numpy as np
import matplotlib.pyplot as plt

print("1. Generazione dataset meteo.")
giorni = np.arange(1, 31)
temperature = np.random.uniform(15.0, 35.0, 30).round(1)

print("2. Calcolo statistiche.")
temp_massima = np.max(temperature)
temp_minima = np.min(temperature)
temp_media = np.mean(temperature)
temp_mediana = np.median(temperature)

print(f"Temperatura Massima: {temp_massima} °C")
print(f"Temperatura Minima: {temp_minima} °C")
print(f"Temperatura Media: {temp_media:.2f} °C")
print(f"Temperatura Mediana: {temp_mediana} °C")

print("3. Visualizzazione grafico.")
plt.figure(figsize=(10, 5))
# Linea principale delle temperature. "marker='o'" aggiunge un punto per ogni giorno, "linestyle='-'" collega i punti con una linea, "color='b'" imposta il colore blu, e "label" fornisce una legenda.
plt.plot(giorni, temperature, marker='o', linestyle='-', color='b', label='Temperatura Giornaliera')

# Linea orizzontale rossa per la temperatura media.
plt.axhline(temp_media, color='r', linestyle='--', label=f'Temperatura Media: {temp_media:.2f} °C')

plt.title('Andamento delle Temperature nel mese')
plt.xlabel('Giorno del Mese')
plt.ylabel('Temperatura (°C)')

# Aggiunta della griglia e della legenda.
plt.grid(True)
plt.legend()

plt.show()