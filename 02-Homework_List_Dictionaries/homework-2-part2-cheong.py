# Cheong Poh Kwan
# June 13 2022
# Homework 2, Part 2

# Lists

# create a list called countries
countries = ["Indonesia", "Brunei", "Malaysia", "Singapore", "Vietnam", "Cambodia", "Thailand"]

# print each element of the list using for loop
for country in countries:
    print(country)

# sort the list permanently
countries.sort()

# print first element of the list
countries[0]

# print second-to-last element of the list
print(countries[1:])

# delete a country from the list using its name
countries.remove("Brunei")

for country in countries:
    print(country.upper())

# Dictionaries

# create a dictionary called tree
tree = {
    "name": "Tree of Life",
    "species": "Mesquite",
    "age": 400,
    "location_name": "Bahrain",
    "latitude": 25.994073,
    "longitude": 50.583235 
}

print(f'{tree["name"]} is a {tree["age"]}-year-old tree that is in {tree["location_name"]}.')

# NYC's coordinates: 40.7128, -74.0059
# check if tree is south of NYC

if tree["latitude"] < 40.7128:
    print(f'{tree["name"]} in {tree["location_name"]} is south of NYC.')
else: 
    print(f'{tree["name"]} in {tree["location_name"]} is north of NYC.')

# ask for user's age
user_age = input("How old are you?")
user_age = int(user_age)

# print if user is older or younger than tree
if user_age >= tree["age"]:
    print(f'You are {user_age - tree["age"]} older than {tree["name"]}.')
else:
    print(f'{tree["name"]} was {tree["age"] - user_age} years old when you were born.')

# Lists of dictionaries

# create a list of dictionaries of 5 cities and their latitude

cities = [
    {"name": "Moscow", "latitude": 55.7558},
    {"name": "Tehran", "latitude": 35.7219},
    {"name": "Falkland Islands", "latitude": -51.7963},
    {"name": "Seoul", "latitude": 37.5665},
    {"name": "Santiago", "latitude": -33.4489}
    ]


# print city's name and whether it's above or below equator

for city in cities:
    if str(city["latitude"]).startswith("-"):
        print(city["name"], "is on the south of equator.")
    else:
        print(city["name"], "is on the north of equator.")

# anotehr method

for city in cities:
    if city["latitude"] > 0:
        print(city["name"], "is on the north of equator.")
    if city["latitude"] < 0:
        print(city["name"], "is on the south of equator.")
    if city["name"] == "Falkland Islands":
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

# print whether city is on the north/south of Tree of Life, whose latitude is 25.994073

for city in cities:
    if float(city["latitude"]) > 25.994073:
        print(city["name"], "is on the north of Tree of Life.")
    else:
        print(city["name"], "is on the south of Tree of Life.")
