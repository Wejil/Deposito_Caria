"""Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in caso non fosse presente vi permetterà di catturarlo salvando le caratteristiche.
(Sul sistema API sono presenti poco più di 1000 pokemon)"""

import requests as r
import json as j
import random as rd

FILE_NAME = r"Corso_Python_Febbraio\15_Venerdi_20\Mattina\pokedex.json"

#creazione del pokedex
def write_pokedex(pokedex):
    with open(FILE_NAME, "w") as f:
        j.dump(pokedex, f, indent=4)

#lettura del pokedex
def read_pokedex():
    try:
        with open(FILE_NAME, "r") as f:
            return j.load(f)
    except FileNotFoundError:
        return None

#aggiunta di un pokemon al pokedex
def append_pokedex(pokedex):
    current_pokedex = read_pokedex()
    if current_pokedex is not None:
        current_pokedex["pokemon"].append(pokedex["pokemon"])
        write_pokedex(current_pokedex)
    else:
        write_pokedex(pokedex)

#estrazione di un pokemon randomico
def random_pokemon():
    num = rd.randint(1, 1025)
    return num

#recupero informazioni del pokemon
def get_pokemon(num):
    url = f"https://pokeapi.co/api/v2/pokemon/{num}"
    try:
        response = r.get(url)
        response.raise_for_status()
    except r.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")
        return None
    return response.json()

def pokemon_info(pokemon):
    info = {
        "name": pokemon["name"],
        "id": pokemon["id"],
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "types": [t["type"]["name"] for t in pokemon["types"]],
        "abilities": [a["ability"]["name"] for a in pokemon["abilities"]],
    }
    return info

# cattura del pokemon
def random_choice():
    choice = [True, False]
    return rd.choice(choice)

#verifica se il pokemon è presente nel pokedex
def check_pokedex(pokedex, pokemon):
    pokedex_d = j.dumps(pokedex, indent=4, sort_keys=True)
    if pokemon['name'] in pokedex_d:
        print(f"{pokemon['name']} è già presente nel tuo pokedex!")
        return True
    else:
        print(f"{pokemon['name']} non è presente nel tuo pokedex!")
        return False

# main del programma
def main():
    if read_pokedex() == None:
        print("Il tuo pokedex è vuoto, cattura il tuo primo pokemon!")
        write_pokedex({"pokemon": []})
    else:
        print("Benvenuto nel tuo pokedex, continua a catturare pokemon!")
        
    while True:
        scelta = input(
            "\n--- POKEDEX ---"
            "\nPuoi:"
            "\n1. Incontra un Pokemon random"
            "\n2. Mostra il tuo Pokedex"
            "\n3. Cerca/Incontra un Pokemon per numero"
            "\n4. Uscita"
            "\nIndica il numero corrispondente\n> "
        )
        match scelta:
            case "1":
                num = random_pokemon()
                pokemon = get_pokemon(num)
                if pokemon is not None:
                    print(f"Hai incontrato {pokemon['name']}!")
                    if not check_pokedex(read_pokedex(), pokemon):
                        if random_choice():
                            print(f"Hai catturato {pokemon['name']}!")
                            append_pokedex({"pokemon": pokemon_info(pokemon)})
                        else:
                            print(f"{pokemon['name']} è scappato!")
            case "2":
                pokedex = read_pokedex()
                if pokedex is not None and pokedex["pokemon"]:
                    print("Il tuo Pokedex contiene:")
                    for p in pokedex["pokemon"]:
                        print(f"- {p['name']}")
                else:
                    print("Il tuo Pokedex è vuoto.")
            case "3":
                num = input("Inserisci il numero del Pokemon che vuoi cercare: ")
                if num.isdigit() and 1 <= int(num) <= 1025:
                    pokemon = get_pokemon(num)
                    if pokemon is not None:
                        print(f"Hai incontrato {pokemon['name']}!")
                        if not check_pokedex(read_pokedex(), pokemon):
                            if random_choice():
                                print(f"Hai catturato {pokemon['name']}!")
                                append_pokedex({"pokemon": pokemon_info(pokemon)})
                            else:
                                print(f"{pokemon['name']} è scappato!")
                else:
                    print("Numero non valido. Inserisci un numero tra 1 e 1025.")
            case "4":
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida. Riprova.")


if __name__ == "__main__":
    main()