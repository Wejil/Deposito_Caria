# Definizione di funzione
def saluta(nome):
    print("Ciao,", nome)
def somma(a, b):
    risultato = a + b
    print("La somma è: ", risultato)
saluta("Alice")

# Funzione riutilizzabile
def stampaSingola_lista(listaX):
    for i in listaX:
        print(i)
lista = [*range(0, 20, 2)]
stampaSingola_lista(lista)

lista2 = [*range(1, 20, 2)]
stampaSingola_lista(lista2)

def ricalcoloValore(x:int):
    return x*7
numero = 10
numero = ricalcoloValore(numero)
print(numero)
print(ricalcoloValore(5))

def quadrato(numero):
    return numero * numero
risultato = quadrato(4)
print(risultato)
