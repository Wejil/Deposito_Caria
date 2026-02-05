**Match**: lavora solo con le stringhe e controlla tutti i case.

**Match comando**: Python valuta il valore della variabile comando.

**Case "start"**: Se il valore della variabile comando corrisponde alla stringa start, esegue il blocco di codice corrispondente.

**Case "stop"**: Funzionano allo stesso modo, controllano rispettivamente per "stop" o per "pausa".

**Case \_ (caso default)**: Se nessun caso precedente corrisponde, il codice associato a questo caso di default viene eseguito. È opzionale ma consigliato.



**While (finché)**: funzione utilizzata per eseguire un blocco di codice finché una determinata condizione è vera. Prima di ogni iterazione, la funzione viene verificata e se è vera, il blocco di codice viene eseguito.



Quando usare un **while** e quando usare un **for**?

Il **while** si usa quando non posso definire o non può essere definito quante volte ripeterò un pezzo da 1 a 1000.

Si usa il **for** quando è definito o si può definire quante volte userò un pezzo.



Il **for** è un elemento autoregolante. Viene regolato mentre lo si scrive.

Vuole una sequenza o un limite di elementi.



**Elemento** - è una variabile che rappresenta l'elemento corrente della sequenza in ogni iterazione. È una variabile placeholder.

**Sequenza** - È una sequenza di elementi su cui si desidera iterare, come una lista, una stringa o l'output della funzione range(). Deve essere sempre una **lista**, una **tupla**, un'**insieme** o una **stringa**.



**range**(): È una funzione unica di Python e incorporata. Restituisce una sequenza di numeri che possono essere usati in cicli for o in altre situazioni riguardanti un insieme di valori.

I **parametri** di range() sono i seguenti:

* **start** (opzionale): il valore di partenza della sequenza. Se omesso, il valore predefinito è 0.
* **stop** (obbligatorio): il valore di fine della sequenza. Il valore stop non è inclusa nella sequenza generata.
* **step** (opzionale): la differenza tra i valori successivi nella sequenza. Se omesso, il valore predefinito è 1.
