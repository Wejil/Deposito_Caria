# Variabili e collezioni
carrello = [] # Lista vuota in cui poter salvare gli elementi.
LIMITE_ARTICOLI = 3    # Limite massimo di oggetti.
# Funzioni
def aggiungi_prodotto(prodotto):
    if len(carrello) < LIMITE_ARTICOLI: # Controllo se c'è spazio. Serve a gestire i limiti e le capacità.
        carrello.append(prodotto)
        print(f"{prodotto} aggiunto.")
        return True
    else:
        print("Carrello pieno.")
        return False
def mostra_carrello():
    print("Articoli nel carrello.")
    for articolo in carrello: # Legge ogni elemento della lista e lo ripete.
        print(f"{articolo}")
def esegui_spesa(): # Controllo di flusso: repetibilità. E si usa un ciclo per permettere all'utente di provare più volte.
    for i in range(3):
        voce = input("Cosa vuoi comprare? ")
        aggiungi_prodotto(voce)
    mostra_carrello()
esegui_spesa()