**Classi**: Fondamentali per l'OOP. La classe è la logica ripetitiva, il disegno tecnico, dell'oggetto. Possiamo avere per ogni nome una classe e infiniti oggetti che derivano da essa. Descritte dal tipo "**class**".

I **metodi** sono le funzioni dentro la classe.

Possono esserci quattro cose dentro le classi: attributi = variabili, liste o collezioni, metodi normali, metodi speciali e altre classi (una classe può stare dentro altre classi).



* Una classe definisce un tipo di oggetti nel mondo reale;
* Una classe è un modello per la creazione di oggetti (in Python);
* Oggetto = istanta di una classe, ovvero una copia univoca della classe che ha le sue proprietà uniche. Ogni oggetto è un'entità a sé stante;
* Sono definite usando la parola class seguita dal nome della classe;
* Possono contenere metodi e attributi.



**Attributi**:

* Variabili associate a una classe;
* Rappresentano le proprietà di un oggetto;
* Gli attributi di classe sono condivisi tra tutte le istanze della classe.

**Metodi**:

* Sono funzioni associate a una classe;
* Rappresentano il comportamento di un oggetto.



**\_\_init\_\_** metodo speciale, legato alla classe che anche se si cancella non sparisce. È anche detto **costruttore**: serve per definire quali variabili servono per costruire un oggetto.

**self** serve a definire qual è l'oggetto reale che stiamo creando.



Il **nome della classe** definisce il tipo dell'oggetto.

È il **nome della classe**, il **tipo degli oggetti che costruisce**, il **modo con cui richiamiamo il costruttore**.



Il costruttore = **\_\_init\_\_**



**I metodi possono essere di tre tipi**:

* **Metodi di istanza**: tutti i metodi che pososno usare gli oggetti definiti con, ad esempio, def saluta(self):
* **Metodi della classe**: non lavorano sui singoli oggetti, ma sulla classe e sono definiti dal decoratore @classmethod, non hanno il self, ma hanno il (cls) che sarebbe il nome della classe
* **Metodi statici**: funzioni non legate alla classe (ma sono dentro alla classe) e all'oggetto. Hanno un decoratore @staticmethod.
