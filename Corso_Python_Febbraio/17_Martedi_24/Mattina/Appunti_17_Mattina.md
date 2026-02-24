* **Array N-dimensionali**: NumPy introduce l'oggetto ndarray, una struttura di dati N-dimensionale che è una generalizzazione degli array unidimensionali e bidimensionali
* **Operazioni vettoriali**: operazioni aritmetiche su array di NumPy eseguite in modo vettoriale. Operazioni come somma, sottrazione, moltiplicazione e divisione possono essere applicate a interi array senza loop espliciti.
* **Funzioni Universali** (ufuncs): NumPy fornisce funzioni universali che effettuano operazioni element-wise su array. Operazioni come sin, cos, exp, ecc.





* **Operazioni aritmetiche** (vettoriali): np.add(), np.subtract(), np. multiply(), np.divide().
* **Funzioni matematiche** (sia vettoriali che universali): np.sin(), np.cos(), np.exp(), np.log().
* **Statistica** (universale): np.mean(), np.mean(), np.std(), np.var().



**Broadcasting**: funzione di NumPy che permette di eseguire operazioni aritmetiche su array di forme diverse. Riduce la necessità di creare array di dimensioni compatibili per le operazioni.

**Principi del Broadcasting**:

* **Allineamento delle Dimensioni**: possiamo avere due elementi uguali o coerenti quando uno dei due è 1;
* **Espansione delle Dimensioni**: se le dimensioni non sono compatibili, numPy espande le dimensioni di uno degli array automaticamente. L'array con la dimensione 1 viene espanso per avere la stessa dimensione dell'altro array;
* **Applicazione dell'Operazione**: non genera valori, ma li spalma. L'array più piccolo viene replicato per riempire l'array più grande.
