**Funzioni generatori**: sono una classe speciale di funzioni che permettono di iterare su una serie di valori, ma anziché restituire tutti i valori in una volta, restituiscono uno alla volta. È un'idea per stampare uno alla volta gli elementi.



**Yield**: in Python è la parola chiave che trasforma una funzione in generatore.



**Decoratori**: sono uno degli aspetti più centrali della programmazione OOP di alto livello. Sono una funzione che modifica il comportamento di un'altra funzione o metodo senza modificare il codice. Sostituisce il calcolo iniziale, non rallenta il tempo di esecuzione. Si applicano anteponendo il simbolo @.

Funzioni principali:

* Le funzioni come oggetti di prima classe: possono essere usate come argomenti a patto che abbiano le parentesi;
* Funzioni annidate, cioè funzioni definite all'interno delle altre funzioni.
* Restituzione di una funzione modificata: i decoratori restituiscono una nuova funzione che sostituisce quella originale (permettendo di modificare il comportamento senza toccare le righe interne).
* Uso di \*args e \*\*kwargs: usati per garantire che il decoratore possa gestire funzioni di qualsiasi tipo, con qualsiasi numero di parametri.
* Sinsassi @decoratore: è equivalente a scrivere funzione = decoratore(funzione).



**args** e **kwargs**: servono per i parametri.



**Wrapper**: consente di eseguire codice aggiuntivo prima e dopo la funzione originale.

Può modificare gli argomenti passati alla funzione decorata o il suo risultato.

utilizza \***args** e \*\***kwargs** per garantire che possa gestire un numero variabile di argomenti posizionali e keyword, mantenendo la flessibilità della funzione originale.



**logger(funzione)**: decoratore che prende una funzione (ad esempio moltiplica) come input.



**@logger**: applica il decoratore logger alla funzione moltiplica, che significa che ogni volta che chiamiamo moltiplica, verrà eseguito il codice del wrapper.

