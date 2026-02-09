# Crea una classe chiamata Punto. Questa classe dovrebbe avere: due attributi x e y, per rappresentare le coordinate del punto nel piano. Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori. Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0, 0) del piano. Ripetibile.
import math # Libreria math per la radice quadrata e l'operatore **2 per elevare al quadrato le coordinate.
class Punto:
    def __init__(self, x, y): # Inizializza le coordinate del punto. __init__ il costruttore. Self rappresenta l'istanza specifica del punto.
        self.x = x
        self.y = y
    def muovi(self, dx, dy): # Modifica le coordinate aggiungendo dx e dy.
        self.x += dx
        self.y += dy
        print(f"Punto spostato in: ({self.x}, {self.y})")
    def distanza_da_origine(self): # Calcola la distanza euclidea dall'origine (0, 0).
        distanza = math.sqrt(self.x**2 + self.y**2)
        return distanza
def esegui(): # Creazione fuori dal ciclo così il punto viene creato una volta sola e mantiene la memoria.
    punto_utente = Punto(0, 0)
    while True: # Per rendere il tutto ripetibile.
        print("Menu.")
        print("1. Muovi il punto.")
        print("2. Calcola la distanza dall'origine.")
        print("3. Esci.")
        scelta = input("Scegli: ")
        if scelta == "1":
            dx = float(input("Spostamento X: "))
            dy = float(input("Spostamento Y: "))
            punto_utente.muovi(dx, dy) # Qui modifichiamo i valori esistenti
            
        elif scelta == "2":
            d = punto_utente.distanza_da_origine()
            print(f"Distanza dall'origine: {d}")
        elif scelta == "3":
            break
esegui()

# Crea una classe chiamata Libro. Questa classe dovrebbe avere: tre attributi: titolo, autore e pagine. Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.". Ripetibile.
class Libro:
    def __init__(self, titolo, autore, pagine): # Metodo costruttore per inizializare gli attributi.
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    def descrizione(self): # Restituisce la stringa descrittiva del libro.
        return f"Il libro '{self.titolo} è stato descritto da {self.autore} e ha {self.pagine} pagine."

def gestore_biblioteca(): # Sistema ripetibile
    biblioteca = [] # Lista per memorizzare i libri creati
    print("Gestore libri.")

    while True:
        print("1. Aggiungi un nuovo libro.")
        print("2. Mostra tutti i libri inseriti.")
        print("3. Esci.")
        scelta = input("Scegli un opzione (1/2/3): ")

        if scelta == "1": # Raccolta dati dall'utente.
            t = input("Inserisci il titolo: ")
            a = input("Inserisci l'autore: ")
            try: # Gestione dell'errore se l'utente non inserisce un numero
                p = int(input("Inserisci il numero di pagine: "))
                nuovo_libro = Libro(t, a, p) # Creazione dell'oggetto "Libro" e aggiunta alla lista.
                biblioteca.append(nuovo_libro)
                print("Libro aggiunto.")
            except ValueError:
                print("Il numero di pagine deve essere un numero intero.")
        elif scelta == "2":
            if not biblioteca:
                print("La biblioteca è ancora vuota.")
            else:
                print("Elenco dei libri: ")
                for libro in biblioteca: # Richiamo il metodo descrizione dell'oggetto.
                    print(libro.descrizione())
        
        elif scelta == "3":
            print("Chiusura del programma.")
            break
        else:
            print("Scelta non valida.")
if __name__ == "__main__": # Avvio del programma.
    gestore_biblioteca()

# Crea una classe biblioteca che permetta di creare un libro e stamparlo. Extra: permetti di creare quanti libri vuole l'utente.
class Libro: # Classe che rappresenta un libro.
    def __init__(self, titolo, autore, anno): # Costruttore che inizializza un libro. Viene chiamato automaticamente quando si crea un oggetto e inizializza gli attributi (variabili dell'oggetto).
        self.titolo = titolo # "self" riferimento all'oggetto stesso (titolo, autore, anno)
        self.autore = autore
        self.anno = anno
    def stampa(self): # Stampa le informazioni del libro.
        print(f" Titolo: {self.titolo}")
        print(f"Autore: {self.autore}")
        print(f"Anno: {self.anno}")

class Biblioteca: # Classe che rappresenta una biblioteca.
    def __init__(self, nome): # Costruttore che inizializza la biblioteca.
        self.nome = nome # Nome della biblioteca.
        self.libri = [] # Lista vuota di libri.
    def aggiungi_libro(self, libro): # Metodo aggiungi_libro() che aggiunge un libro alla biblioteca.
        self.libri.append(libro) # Aggiunge libro alla lista self.libri.
        print(f"Libro '{libro.titolo}' aggiunto alla biblioteca.")
    def stampa_tutti_libri(self): # Stampa tutti i libri della biblioteca.
        print(f"Biblioteca: {self.nome}")
        if len(self.libri) == 0:
            print("Nessun libro presente.")
        else:
            for i, libro in enumerate(self.libri, 1):
                print(f"{i}.")
                libro.stampa() # Chiama il metodo stampa() dell'oggetto Libro.
        print(f"Totale libri: {len(self.libri)}")

print("Sistema gestione biblioteca")
nome_biblioteca = input("Nome della biblioteca: ") # Crea una biblioteca.
biblioteca = Biblioteca(nome_biblioteca)
print(f" Biblioteca '{nome_biblioteca}' creata.")

while True: # Loop per creare libri.
    print("1. Aggiungi libro.")
    print("2. Mostra tutti i libri.")
    print("3. Esci.")
    scelta = input("Scegli (1-3): ")
    if scelta == "1": # Crea un nuovo libro.
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        try:
            anno = int(input("Anno: "))
            nuovo_libro = Libro(titolo, autore, anno) # Crea oggetto "Libro".
            biblioteca.aggiungi_libro(nuovo_libro) # Aggiunge alla biblioteca.
        except ValueError:
            print("Anno non valido.")
    elif scelta == "2": # Mostra tutti i libri.
        biblioteca.stampa_tutti_libri()
    elif scelta == "3": #Esci.
        break
    else:
        print("Scelta non valida.")