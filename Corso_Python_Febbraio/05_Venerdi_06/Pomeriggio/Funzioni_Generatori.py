'''def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b'''

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a  # Invece di 'return', 'congela' la funzione e restituisce il valore.
        a, b = b, a + b

# Per usare un generatore, dobbiamo iterare (quindi ciclarci sopra).
limite = 100
print(f"Sequenza di Fibonacci fino a {limite} (usando yield):")

for numero in fibonacci(limite):
    print(numero, end=" ")

def contatore_fino_a(n):
    # Generatore che produce 1, 2, 3, ..., n.
    i = 1
    while i <= n:
        yield i 
        i += i
print(contatore_fino_a(10)) # Ogni giro, prima fa il processo e crea la lista, poi torna sul print.

def catena_generatori():
    yield from range (1, 4) # Prima produce 1...3
    yield from range (10, 13) # Poi 10...12
print(list(catena_generatori()))

# Decoratori
def decoratore(funzione): # 1.@decoratore
    def wrapper(): # 2. def saluta():
        print("Prima dell'esecuzione della funzione.") # 3. print("Ciao")
        funzione()
        print("Dopo l'esecuzione della funzione") # 5. Saluta()
    return wrapper

# Esempio di decoratore, tentativo

# 1. Definiamo il decoratore
def annuncia_esecuzione(funzione_originale):
    def wrapper(*args, **kwargs):
        print(f"--- Avvio della funzione: {funzione_originale.__name__} ---")
        risultato = funzione_originale(*args, **kwargs)
        print("--- Esecuzione completata! ---")
        return risultato
    return wrapper

# 2. Applichiamo il decoratore con la sintassi @
@annuncia_esecuzione
def fibonacci(n):
    a, b = 0, 1
    sequenza = []
    while a <= n:
        sequenza.append(a)
        a, b = b, a + b
    return sequenza

# 3. Chiamata alla funzione
risultato = fibonacci(50)
print(f"Risultato: {risultato}")

def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b
print("risultato è ", somma(3, 4))

def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper

@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
print(moltiplica(3, 4))


