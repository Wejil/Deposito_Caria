**Modulo**: un file che contiene definizioni di variabili, funzioni e classi che possono essere usate in altri programmi Python.

Ogni modulo deve avere una sua logica unitaria. Si divide per obiettivo (ES.: qual è l'obiettivo di questo codice? Creare pacchi, ecc.).



**3 regole dell'OOP**: tre regole paritarie di stesso livello che funzionano in maniera ausiliaria una con l'altra. Funzionano tutte e tre contemporaneamente. Se manca una di loro le altre "crollano". Una basilare, fondamentale, senza la quale non possono funzionare le altre: l'astrazione.

* **Ereditarietà**: più in mano al programmatore 75%, 25% implicita. È la capacità di una classe di avere un padre o un figlio che può ereditare i suoi elementi se vogliamo. Un padre può avere infiniti figli. Infiniti padri per ogni figlio. **Multiereditarietà**: Python.
* **Incapsulamento**: 50% implicito (macchina), 50% utente. Nasconde i dettagli di una classe per esporre solo quelli che interessano e con cui interagire, lasciando il codice pulito e sicuro.
* **Polimorfismo**: 75% implicito, 25% in mano all'utente. È la capacità di cambiare forma e/o comportamento ad un elemento senza cambiarne il tipo.



**Ereditarietà**: classe padre (si dice superclasse o padre), classe figlio (si dice sottoclasse o figlio). Ogni classe figlio può ereditare dal padre attributi e metodi. I figli possono diventare padri.

**3 modi di utilizzo**:

* **Metodo super**: permettere di utilizzare il costruttore della classe padre esattamente com'è scritta;
* **Sovrascrittura**: sovrascriviamo i metodi del padre;
* **Ereditarietà multipla**: Python supporta l'ereditarietà multipla, permettendo a una classe figlia di ereditare da più classi padri.
