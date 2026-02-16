'''
Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l'utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10
'''

registro = {}   # Dizionario vuoto per il registro.

print("Inseriscici i dati degli alunni. Scrivi 'media' per vedere i risultati e uscire.")

while True:
    nome = input("Nome alunno (o 'media'): ")
    if nome.lower() == "media": # Controllo per uscire dal ciclo e calcolare la media.
        break

    # Voti (separati da uno spazio) che diventeranno una lista di numeri.
    stringa_voti = input(f"Inserisci i voti di {nome} separati da uno spazio: ")
    voti_numerici = []
    for i in stringa_voti.split():
        voti_numerici.append(float(i))

    registro[nome] = voti_numerici # Salvo nel dizionario: Nome > Lista dei voti.

print("Risultati.")

for nome, lista_voti in registro.items():
    if len(lista_voti) > 0:
        media = sum(lista_voti) / len(lista_voti)   # Somma dei voti / numero dei voti.
        print(f"Nome: {nome}, Media: {media}")
    else:
        print(f"Nome: {nome}, Nessun voto inserito.")