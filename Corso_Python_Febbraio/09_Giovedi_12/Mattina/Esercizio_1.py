'''
Creare una classe base MetodoPagamento e diversi classi derivate che rappresentino metodi di pagamento.
Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento,
pur aderendo all'interfaccia comune definita dalla classe base. Va reso ripetibile.

1. Classe MetodoPagamento:
    - Metodi:
        - effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
2. Classi Derivate:
    - CartaDiCredito:
        - Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
    - PayPal:
        - Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
    - BonificoBancario:
        - Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
3. GestorePagamenti:
    - Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.
'''
# Classe base.
class MetodoPagamento:
    def effettua_pagamento(self, importo):  # Metodo che verrà sovrascritto dalle sottoclassi. Se non lo avesse, il sistema si "romperebbe".
        print(f"Elaborazione di un pagamento generico d i €{importo}")

# Classi derivate.
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"[CARTA DI CREDITO] connessione al circuito bancario.")
        print(f"Pagamento di €{importo} autorizzato.")

class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"[PAYPAL] reindirizzamento al login sicuro.")
        print(f"Transizione di €{importo} effettuata.")

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"[BONIFICO] generazione bonifico.")
        print(f"Ordine di €{importo} del bonifico preso in carico.")

# Gestore pagamenti.
class GestorePagamenti:
    def __init__(self):
        self.metodo_scelto = None
    
    def imposta_metodo(self, metodo_obj):   # Riceve un'istanza di una delle classi derivate.
        self.metodo_scelto = metodo_obj
    
    def esegui(self, importo):
        if self.metodo_scelto:  # Non si sa quale metodo sia (non gli interessa), ma solo che ha il metodo "effettua_pagamento" (sa come pagare) = Polimorfismo.
            self.metodo_scelto.effettua_pagamento(importo)
        else:
            print("Errore: nessun metodo di pagamento selezionato.")

# Menu ripetibile.
gestore = GestorePagamenti()

while True:
    print("1. Scegli Carta di Credito.")
    print("2. Scegli PayPal.")
    print("3. Scegli Bonifico Bancario.")
    print("4. Effettua Pagamento.")
    print("5. Esci.")

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        gestore.imposta_metodo(CartaDiCredito())
        print("Metodo impostato: Carta di Credito.")
    elif scelta == "2":
        gestore.imposta_metodo(PayPal())
        print("Metodo impostato: PayPal.")
    elif scelta == "3":
        gestore.imposta_metodo(BonificoBancario())
        print("Metodo impostato: Bonifico.")
    elif scelta == "4":
        imp_str = input("Inserisci l'importo da pagare (€): ")
        if imp_str.replace(".", "", 1).isdigit():   # Validazione affinché l'importo sia un numero decimale valido.
            importo_finale = float(imp_str)
            if importo_finale > 0:
                gestore.esegui(importo_finale)
            else:
                print("L'importo deve essere maggiore di zero.")
        else:
            print("Errore: inserusci un numero valido.")
    
    elif scelta == "5":
        print("Chiusura sessione, arrivederci.")
        break
    else:
        print("Scelta non valida.")