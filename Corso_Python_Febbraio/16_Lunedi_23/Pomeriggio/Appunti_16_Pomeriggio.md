**Pip** = "Pip Installer Packages" o "Preferred Installer Program".

È il sistema di gestione di librerie utilizzato da Python.

* Permette allo sviluppatore di installare pacchetti aggiuntivi (librerie) all'interno del contesto Python, da fonti esterne, da PyPI o GitHub;
* Installa automaticamente tutti gli elementi, logiche e funzionalità laterali del pacchetto principale;
* Rimuove e aggiorna i pacchetti;
* È capace di scegliere downgrade, upgrade e struttura con la quale andare ad integrarsi in libreria;
* Funziona bene con ambienti virtuali, permettendo agli sviluppatori di creare ambienti isolati per gestire le dipendenze dei loro progetti in modo indipentente.



**Array**: modificabile, ordinato, eterogeneo, tipo di dato arr\[] o tonde () + \[].



**NumPy**: "Numerical Python", è una libreria fondamentale per il calcolo scientifico.

Porta in campo strutture vettoriali ed array.

* Supporto per array multidimensionali (ndarray);
* Funzioni matematiche avanzabili per operare sugli array;
* Integrabile con C, C++ e Fortran.



**Keyword**:

* ndarray: oggetto array multidimensionale principale. Più veloci ed efficienti rispetto alle liste native di Python;
* dtype: specifica il tipo di dato degli elementi di un array, che includono int, float, bool, etc.
* shape: proprietà che restituisce le dimensioni dell'array. Ad esempio un array con 3 righe e 4 colonne avrà una shape di (3, 4);
* arange: simile alla funzione range() di Python, ma restituisce un array invece di una lista;
* reshape: cambia la shape di un array senza modificarne i dati;
* linspace: genera un array di numeri equamente distribuiti tra un valore iniziale e finale;
* random: modulo per generare array con valori casuali, distribuzioni numerali e uniformi;
* sum, mean, std: funzione per calcolare rispettivamente la somma, la media e la deviazione standard degl elementi di un array.



**Indexing e Slicing**: tecniche per gestire l'indicizzazione di NumPy o dei suoi array.



**Slicing**: tecnica utilizzata per estrarre una parte di un array o di una sequenza.

È simile a quello delle liste in Python, ma è molto più potente e versatile. Permette di ottenere subarray di una array esistente senza copiare i dati, dunque efficiente in termini di memoria.



* start: l'indice di inizio dello slicing (inclusivo). Se omesso, il valore predefinito è 0;
* stop: l'indice di fine dello slicing (esclusivo). Se omesso, il valore predefinito è la somma dell'array;
* step: il passo tra un indice e l'altro. Se omesso, valore predefinito: 1.



Differenza tra **Slicing e Fancy Indexing**: a livello logico utilizza indici interi, non ne crea una copia. Lo slicing utilizza indici di inizio, fine e passo. Il fancy index utilizza array di indici interi.

