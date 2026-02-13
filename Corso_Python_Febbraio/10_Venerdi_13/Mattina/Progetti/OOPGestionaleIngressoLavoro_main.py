'''
Realizza un gestionale per l'ingresso a lavoro (accesso dipendenti, badge, turni, ecc.) utilizzando la programmazione ad oggetti.
Obiettivo generale:
Progettare e implementare un piccolo sistema software che gestisca la logica di ingresso in azienda (ad esempio persone, ruoli, badge, turni, controlli di accesso, log di entrata/uscita, ecc.), usando in modo evidente tutte e quattro le regole principali dell'OOP:
- Astrazione
- Ereditarietà
- Incapsulamento
- Polimorfismo
Il progetto dovrà:
- essere organizzato nella cartella indicata all'interno della vostra repository
- contenere più file e/o moduli coerenti con l'idea di gestionale per l'ingresso a lavoro",
- mostrare chiaramente nel codice la struttura, dove e come vengono applicate le quattro regole OOP.

Non ci sono altre regole specifiche obbligatorie: siete voi a dover definire quali oggetti esistono, come interafiscono, quali responsabilità hanno e come dimostrare in modo chiaro l'uso di astrazione, ereditarietà, incapsulamento e polimorfismo.
'''

# Gestione del programma.
from OOPGestionaleIngressoLavoro_utenti import Operaio, Manager
from OOPGestionaleIngressoLavoro_controllo import RegistroAccessi

def main(): # Creazione del sistema di controllo.
    tornello = RegistroAccessi()

    mario = Operaio("Mario", "Rossi", "MR007")
    sara = Manager("Sara", "Bianchi", "SB001")

    print("Simulazione ingressi aziendali.")

    # Registrazione ingressi (polimorfismo), il metodo registra_movimento che accetta qualsiasi Dipendente e gestisce i permessi diversi.
    tornello.registra_movimento(mario, "entrata")
    tornello.registra_movimento(sara, "entrata")

    # Registrazione di un'uscita.
    tornello.registra_movimento(mario, "uscita")

    # Log finale delle entrate/uscite.
    tornello.mostra_report()

if __name__ == "__main__":
    main()