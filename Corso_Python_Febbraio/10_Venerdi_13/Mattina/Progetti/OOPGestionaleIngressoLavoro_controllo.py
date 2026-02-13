# Gestione della logica dei log riguardo entrata/uscita.
from datetime import datetime

class RegistroAccessi:
    def __init__(self):
        self.__log = [] # Incapsulamento. La lista dei log è protetta.
    
    def registra_movimento(self, dipendente, tipo):
        orario = datetime.now().strftime("%H:%M:%S")    # Ora, minuto e secondo dell'ingresso.
        entry = {
            "orario": orario,
            "dipendente": dipendente.descrizione(),
            "tipo": tipo,
            "permessi": dipendente.livello_accesso()    # Polimorfismo.
        }
        self.__log.append(entry)
        print(f"[{orario}] {tipo.upper()}: {dipendente.nome} - {dipendente.livello_accesso()}")
    
    def mostra_report(self):
        print("Report accessi aziendali.")
        for record in self.__log:
            print(f"{record['orario']} | {record['tipo']} | {record['dipendente']}")