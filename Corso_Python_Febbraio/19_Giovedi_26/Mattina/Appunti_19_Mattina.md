**Serie Temporali**: strumento specifico per manipolare date e tempi, dunque permette di analizzare serie temporali, cambiare la frequenza dei dati e generare periodi di tempo.



**Resample**: prende dei dati e li riformatta per il mese, il giorno, ecc. Li ridimensiona, specificando l'intervallo desiderato ('D' = day, 'M' = month, 'H' = hour).



**Shift**: sposta i valori lungo l'asse temporale dei periodi. Capacità di spostare un arco temporale da tasso di variazione giornaliera, mensile, ecc. (es. quanto ho venduto giorno x, ecc.)



**Rolling**: calcola le statistiche mobili su una finestra temporale scorrevole. Ad esempio, rispetto ad un dato x dentro una colonna y, vado a creare un nuovo valore tramite il rolling e gli si può chiedere media, somma, ecc.



**Visualizzazione dei dati**: insieme delle capacità per esplorare i dati dal punto di vista visivo e dal punto di vista matematico.



**Principi base** nel creare visualizzazioni efficaci e comprensibili:

* **Informativo**: fornire dati chiari e precisi per supporto decisioni;
* **Esplorativo**: usato in fase di analisi per scoprire pattern, correlazioni e outlier nei dati;
* **Narrativo**: per raccontare una storia o presentare una sequenza di eventi o risultati in modo coinvolgente.



Matlib serve a fare grafici e altro, mentre Searborn è la sua evoluzione (integrato con Pandas e NumPy) e consente una personalizzazione stilistica specifica degli elementi.



Componenti Principali di Matplotlib:

* **Figure**: rappresentano l'intero grafico o gli interi grafici.
* **Axes**: è una parte della figura in cui c'è un grafico, delle coordinate.
