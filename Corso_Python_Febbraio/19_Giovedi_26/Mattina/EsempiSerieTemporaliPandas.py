import pandas as pd

# Generazione di una serie di date.
date_range = pd.date_range(start='2021-01-01', periods=10, freq= 'M')

# Resampling dei dati di una serie temporale.
df_resampled = date_range.resample('M').mean()

# Esempio rolling.
# Finestra mobile di 7 giorni: media e deviazione standard.
'''df'''
date_range['rolling_mean7'] = date_range['value'].rolling(window=7).mean()
'''df'''
date_range['rolling_std7'] = date_range['value'].rolling(window=7).std()