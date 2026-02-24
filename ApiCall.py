# How to connect to an API using Python
import requests 

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}" # Full URL
    response = requests.get(url)
    print(response) 

    if response.status_code == 200:
        print(f"Data retrieved successfully")
        pokemon_data = response.json() # Converting data into JSON format
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = input("Please insert pokemon name: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"ID          : {pokemon_info["id"]}")
    print(f"Name        : {pokemon_info["name"].capitalize()}")
    print(f"Height      : {pokemon_info["height"]}")
    print(f"Weight      : {pokemon_info["weight"]}")
    
    types = [t['type']['name'] for t in pokemon_info['types']]
    print(f"Types       : {', '.join(types)}")

    abilities = [a['ability']['name'] for a in pokemon_info['abilities']]
    print(f"Abilities   : {', '.join(abilities)}")