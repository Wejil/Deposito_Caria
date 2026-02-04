**Operazioni logiche**: and, or, not. La prima cosa trasportata dal **pensiero umano** all'interno delle **macchine**.

**And**: restituisce True se entrambe le condizioni sono vere.

**Or**: restituisce True se almeno una delle condizioni è vera.

**Not**: restituisce il valore booleano opposto di ciò che segue.



**Collezioni**: insiemi di variabili salvate in un unico punto specifico in memoria (= con un unico nome).
Per le macchine = semplice. Per gli umani = è utile, una grande utility.

Si dividono in:

* **Modificabili**: puoi farci quello che vuoi, a mano: togliere i dati, modificare ecc.
* **Non modificabili**: ci metti i dati dentro, fine. Rimangono lì come snoo.
* **Dinamiche**: quegli esempi, strutture e logiche che vanno a ricrearsi quando ci sono quelle strutture che li vanno a bloccare per sempre.



**Liste**: Strutture più utilizzate in Python. È una collezione ordinata e modificabile di elementi.

È **eterogenea** (può avere tutti i tipi di dato: int, stringa, ecc.) e sono definite dal tipo "**list**" e dalle parentesi quadre \[].

Tipo list, ordinata, modificabile.



**len**() per ottenere la lunghezza della lista. Non appartiene alla lista. Funzione incorporata.

**append**() per aggiungere un elemento alla fine della lista

**insert**() per inserire un elemento in una posizione specifica

**remove**() per rimuovere un elemento

**sort**() per ordinare gli elementi della lista e molti altri



Le tre cose da chiedere: sono **modificabili**, **miste** o **ordinate**?



**Tuple**: Non modificabili una volta create (dunque modificabile una volta, quando la si crea, ma dal momento in cui si mette un valore dentro, non è modificabile). Mista e ordinata, che ha come tipo "tuple". Non usano le parentesi quadrate \[], ma tonde ().

La creazione di tuple senza parentesi ed è noto come "**tuple packing**" o "**tuple unpacking**".



**Insiemi**: Non sono ordinate, modificabile, miste (non ammettono duplicati, li ignoreranno).

Sono rappresentati dal tipo "**set**".

Possono subire tutte le operazioni algebriche e matematiche:

* **Unione** (union() o |): Restituisce un nuovo insieme contenente tutti gli elementi presenti in entrambi gli insiemi. Ignora i duplicati.
* **Intersezione** (intesection() o \&): Restituisce un nuovo insieme contenente solo gli elementi comuni in entrambi gli insiemi. Solo ciò che c'è in entrambi.
* **Differenza** (difference() o -): Restituisce un nuovo insieme contenente gli elementi presenti nell'insieme di partenza, ma non nell'altro insieme.
* **Differenza simmetrica** (symmetric\_difference() o ^): Restituisce un nuovo insieme contenente gli elementi che sono presenti in uno dei due insiemi, ma non in entrambi.

Per aggiungere un elemento ad un insieme: **add**().
Per rimuovere un elemento: **remove**() o **discard**(). Sempre meglio usare **discard**().

Per ottenere la lunghezza di un insieme: **len**().

Per avere una copia dell'insieme: **copy**().

L'operatore **in**() si occupa di controllare se un elemento è presente nell'insieme.



**Controllo del flusso**: Si riferisce al gestire le righe che vengono lette nel **come**, nel **se** e nel **quando**. Concetto principale della programmazione moderna (da C in su).

Divisi in tre categorie: **condizioni**, **cicli**, **funzioni**.



**Condizione**: controllore del flusso che decide se un pezzo di codice (blocco) viene eseguito.

**Cicli**: controllo del flusso, che condiziona quante volte viene ripetuto un blocco di codice. Da 0 a infinito.



La principale condizione si chiama "**if**". Composto dalla parola "**if**", dalla **condizione reale** (formula che deve riportare "True") e i **due punti**.

**Elif**: si possono avere infiniti in mezzo. È una condizione ausiliaria.

Un solo **If** sempre all'inizio. Si possono avere un **If** dentro l'altro.

Un solo **Else**, sempre alla fine. E ci si può mettere dentro l'**If**.

L'importante è creare una **sequenza coerente**.

