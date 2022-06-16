# Cheong Poh Kwan
# June 15 2022
# Homework 3, Part 1

# PART ONE: Pokemon API

import requests

# 1. What is the URL to the documentation?
# https://pokeapi.co/api/v2/pokemon/{id or name}/

url = "https://pokeapi.co/api/v2/pokemon/"

response = requests.get(url)

data = response.json()

print(data)
# data is a dictionary

print(data.keys())
# keys are ['count', 'next', 'previous', 'results']

print(data["results"])
# results is a list with 'name' and 'url'
# 'url' ends with id

# 2. What pokemon has the ID of 55?

url_55 = "https://pokeapi.co/api/v2/pokemon/55"

response_55 = requests.get(url_55)

data_55 = response_55.json()

print(data_55)

# data_55 is a dictionary

print(data_55.keys())
# keys are ['abilities', 'base_experience', 'forms', 'game_indices', 'height', 'held_items', 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'past_types', 'species', 'sprites', 'stats', 'types', 'weight']

print(data_55["name"])
print("The name of the pokemon with ID 55 is Golduck.")

# 3. How tall is that pokemon?

print(data_55["height"])
print("Golduck is 17 decimeteres.")

# 4. How many versions of Pokemon games have been released?
# https://pokeapi.co/api/v2/version/{id or name}/

url_version = "https://pokeapi.co/api/v2/version/"

response_version = requests.get(url_version)

data_version = response_version.json()

print(data_version)

# data version is a dictionary, results is a key in the dictionary. 
# printing results gives a list of dictionaries, with name and url as the key-value pair
# print(data_version["results"][0]["name"])

versions = [version["name"] for version in data_version["results"]]
print(versions)

print(len(versions), "versions of Pokemon games have been released.")

# 5. Print out the name of every electric-type pokemon.

# url: https://pokeapi.co/api/v2/type/{id or name}/

url_type = "https://pokeapi.co/api/v2/type/"

response_type = requests.get(url_type)

data_type = response_type.json()

print(data_type)

print(data_type["results"])

# Found this key-value pair in the results list
# 'name': 'electric', 'url': 'https://pokeapi.co/api/v2/type/13/'

url_electric = "https://pokeapi.co/api/v2/type/13/"

response_electric = requests.get(url_electric)

data_electric = response_electric.json()

print(data_electric.keys())
# ['damage_relations', 'game_indices', 'generation', 'id', 'move_damage_class', 'moves', 'name', 'names', 'past_damage_relations', 'pokemon']

print(data_electric["pokemon"])

electric_pokemons = [electric_pokemon["pokemon"]["name"] for electric_pokemon in data_electric["pokemon"]]
print(electric_pokemons)

# ['pikachu', 'raichu', 'magnemite', 'magneton', 'voltorb', 'electrode', 'electabuzz', 'jolteon', 'zapdos', 'chinchou', 'lanturn', 'pichu', 'mareep', 'flaaffy', 'ampharos', 'elekid', 'raikou', 'electrike', 'manectric', 'plusle', 'minun', 'shinx', 'luxio', 'luxray', 'pachirisu', 'magnezone', 'electivire', 'rotom', 'blitzle', 'zebstrika', 'emolga', 'joltik', 'galvantula', 'tynamo', 'eelektrik', 'eelektross', 'stunfisk', 'thundurus-incarnate', 'zekrom', 'helioptile', 'heliolisk', 'dedenne', 'charjabug', 'vikavolt', 'togedemaru', 'tapu-koko', 'xurkitree', 'zeraora', 'yamper', 'boltund', 'toxel', 'toxtricity-amped', 'pincurchin', 'morpeko-full-belly', 'dracozolt', 'arctozolt', 'regieleki', 'rotom-heat', 'rotom-wash', 'rotom-frost', 'rotom-fan', 'rotom-mow', 'thundurus-therian', 'ampharos-mega', 'manectric-mega', 'pikachu-rock-star', 'pikachu-belle', 'pikachu-pop-star', 'pikachu-phd', 'pikachu-libre', 'pikachu-cosplay', 'pikachu-original-cap', 'pikachu-hoenn-cap', 'pikachu-sinnoh-cap', 'pikachu-unova-cap', 'pikachu-kalos-cap', 'pikachu-alola-cap', 'raichu-alola', 'geodude-alola', 'graveler-alola', 'golem-alola', 'vikavolt-totem', 'oricorio-pom-pom', 'pikachu-partner-cap', 'togedemaru-totem', 'pikachu-starter', 'pikachu-world-cap', 'toxtricity-low-key', 'morpeko-hangry', 'pikachu-gmax', 'toxtricity-amped-gmax', 'toxtricity-low-key-gmax']


# 6. What are electric-type Pokemon called in the Korean version of the game?

print("This question cannot be answered using the API.")



# 7. Who has a higher speed stat, Eevee or Pikachu?

url_eevee = "https://pokeapi.co/api/v2/pokemon/eevee/"
response_eevee = requests.get(url_eevee)
data_eevee = response_eevee.json()

url_pikachua = "https://pokeapi.co/api/v2/pokemon/pikachu/"
response_pikachu = requests.get(url_pikachua)
data_pikachu = response_pikachu.json()

print(data_eevee.keys())

print(data_eevee["stats"])

print("This question cannot be answered using the API.")
