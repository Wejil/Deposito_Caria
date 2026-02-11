**Incapsulamento**: la capacità di nascondere i dettagli interni dell'implementazione di una classe ed espone ciò che e necessario.



**Metodi dell'Incapsulamento**:

* **Attributi Privati** (\_\_attributo): con due undersore prima del nome dell'attributo, l'attributo diventa privato (non viene ereditato) e significa che non può essere accesso dall'esterno della classe.
* **Attributi Protetti** (\_attributo): ponendo solo un underscore prima del nome dell'attributo, diventa considerato protetto. È visibile ai figli, serve a creare la classe base dove non ci sono i valori.
* **Metodi Getter e Setter**: forniscono un controllo maggiore sull'accesso alla modifica dei dati. Attributi che permettono di ottenere (get) e modificare (set) gli attributi privati di una classe.



**Livello di visibilità** (o scope delle variabili): 

* **Globale**: conosciuta e dichiarata fuori dalle funzioni
* **Locale**: le variabili locali sono dichiarate all'interno della funione e sono accessibili all'interno di quella funzione.
* **Non-locale**: si applica nelle funzioni annidate.
