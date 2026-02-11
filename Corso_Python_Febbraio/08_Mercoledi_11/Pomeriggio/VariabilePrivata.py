class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"

    def __metodo_privato(self):
        return "Questo è un metodo privato"

obj = MiaClasse()
# Stampando direttamente la variabile privata solleverà un'eccezione
# print(obj.__variabile_privata) # AttributeError
# L'accesso corretto (che dovrebbe essere vietato) sarebbe:
print(obj._MiaClasse__variabile_privata) # Funzionerà, ma non è buona prassi.

# Metodo privato stampato in un metodo pubblico.
class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    # METODO PRIVATO
    def __crea_saluto(self):
        return f"Ciao, mi chiamo {self.nome} {self.cognome}!"
    
    # METODO PUBBLICO che stampa il risultato del metodo privato
    def presentati(self):
        messaggio = self.__crea_saluto()  # Chiama il metodo privato
        print(messaggio)

persona = Persona("Mario", "Rossi")

persona.presentati()