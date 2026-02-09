'''Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base.
Requisiti:
1. Definizione della Classe:
- Creare una classe chiamata Ristorante.
- La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e tipo_cucina (tipo di cucina offerta).
- Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere impostato su False di default (cioè, il ristorante è chiuso).
- Una Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante
2. Metodi della Classe:
- descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
- stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
- apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
- chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
- aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
- togli_dal_menu(): Un metodo per togliere piatti al menu
- stampa_menu(): Un metodo per stampare il menu
3. Testare la Classe:
- Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
- Testare tutti i metodi creati per assicurarsi che funzionino come previsto.
'''

class Ristorante: # Classe ristorante.
    def __init__(self, nome, tipo_cucina): # Costruttore che inizializza il ristorante. Parametri: nome, tipo di cucina.
        self.nome = nome # Nome del ristorante.
        self.tipo_cucina = tipo_cucina # Tipo di cucina del ristorante.
        self.aperto = False # Di default il ristorante è chiuso. Booleano (True/False) per lo stato di apertura
        self.menu = [] # Lista vuota per i piatti e prezzi.
    def descrivi_ristorante(self): # Stampa una descrizione del ristorante. Il nome e il tipo di cucina.
        print(f"Ristorante: {self.nome}")
        print(f"Tipo cucina: {self.tipo_cucina}")
    def stato_apertura(self): # Stampa se il ristorante risulta aperto o chiuso. Controlla se True = aperto. Se False = chiuso.
        if self.aperto:
            print(f"{self.nome} è aperto.")
        else:
            print(f"{self.nome} è chiuso.")
    def apri_ristorante(self): # Apre il ristorante.
        self.aperto = True
        print(f"{self.nome} è ora aperto, benvenuti.")
    def chiudi_ristorante(self): # Chiude il ristorante.
        self.aperto = False
        print(f"{self.nome} è ora chiuso, a presto.")
    def aggiungi_al_menu(self, piatto, prezzo): # Aggiunge un piatto al menu, parametri:piatto e prezzo.
        nuovo_piatto = [piatto, prezzo]
        self.menu.append(nuovo_piatto)
        print(f"'{piatto}' aggiunto al menu (€{prezzo})")
    def togli_dal_menu(self, piatto): # Rimuove un piatto dal menu, parametri: piatto (da rimuovere).
        for item in self.menu: # Cerca il piatto nel menu.
            if item [0] == piatto:
                self.menu.remove(item)
                print(f"'{piatto}' rimosso dal menu")
                return # Esce dalla funzione.
        print(f"'{piatto}' non è stato trovato nel menu")
    def stampa_menu(self): # Stampa tutto il menu
        print(f"Menu di {self.nome.upper()}")

        if len(self.menu) == 0:
            print("Menu vuoto, nessun piatto disponibile.")
        else:
            for i, item in enumerate(self.menu, 1):
                piatto, prezzo = item
                print(f"{i}. {piatto:<30} €{prezzo:.2f}")

print("Sistema di gestione del ristorante)") # Programma principale per la gestione del ristorante.
# Crea un'istanza della classe ristorante
nome = input("Nome del ristorante: ")
cucina = input("Tipo di cucina: ")
ristorante = Ristorante(nome, cucina)
print(f"Ristorante '{nome}' creato con successo.")

while True: # Menu principale.
    print("Menu gestione.")
    print("1. Descrivi il ristorante.")
    print("2. Controlla stato (aperto/chiuso)")
    print("3. Apri ristorante.")
    print("4. Chiudi ristorante.")
    print("5. Aggiungi piatto al menu.")
    print("6. Rimuovi piatto dal menu.")
    print("7. Visualizza menu completo.")
    print("8. Esci.")
    scelta = input("Scegli un'opzione (1-8): ")
    if scelta == "1": # Descrivi il ristorante.
        ristorante.descrivi_ristorante()
    elif scelta == "2": # Stato apertura.
        ristorante.stato_apertura()
    elif scelta == "3": # Apri il ristorante.
        ristorante.apri_ristorante()
    elif scelta == "4": # Chiudi il ristorante.
        ristorante.chiudi_ristorante()
    elif scelta == "5": # Aggiungi un piatto.
        print("Aggiungi un piatto.")
        piatto = input("Nome piatto: ")
        prezzo_str = input("Prezzo (€): ")
        if prezzo_str.replace(".", "", 1).isdigit(): # Converte in numero.
            prezzo = float(prezzo_str)
            ristorante.aggiungi_al_menu(piatto, prezzo)
        else:
            print("Prezzo non valido.")
    elif scelta == "6": # Rimuovi un piatto.
        ristorante.stampa_menu()
        piatto = input("Nome piatto da rimuovere: ")
        ristorante.togli_dal_menu(piatto)
    elif scelta == "7": # Visualizza menu.
        ristorante.stampa_menu()
    elif scelta == "8": # Esci.
        print(f"Arrivederci.")
        break
    else:
        print("Opzione non valida.")
    input("[Premi INVIO per continuare.]")