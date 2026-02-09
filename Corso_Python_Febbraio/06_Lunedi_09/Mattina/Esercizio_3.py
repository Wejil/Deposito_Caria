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
        anno = int(input("Anno: "))
    elif scelta == "2": # Mostra tutti i libri.
        biblioteca.stampa_tutti_libri()
    elif scelta == "3": #Esci.
        break
    else:
        print("Scelta non valida.")