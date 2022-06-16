# Cheong Poh Kwan
# June 13 2022
# Homework 2, Part 1

# Lists

# make a list of numbers
numbers = [22, 90, 0, -10, 3, 22, 48]

# print number of elements in list
print(len(numbers))

# print 4th element in list
print(numbers[3])

# print sum of 2nd and 4th element in list
print(numbers[1]+numbers[3])

# print 2nd largest value in list
sorted = sorted(numbers)
print(sorted[1])

# print last element of unsorted list
print(numbers[-1])

# print sum of all numbers divided by 2
sum = numbers[0] + numbers[1] + numbers [2] + numbers [3] + numbers [4] + numbers [5] + numbers [6]
print(sum/2)

# print whether median or mean of the numbers is higher
mean = sum/7
median = sorted[3]

if mean > median:
    print(f"The mean is higher than the median of the list of numbers.")
elif mean == median:
    print(f"The mean is the same as the median of the list of numbers.")
else: 
    print(f"The median is higher than the mean of the list of numbers.")

# Dictionaries

# create a dictionary called movie 
movie = {
    "title": "Top Gun: Maverick",
    "year": 2022,
    "director": "Joseph Kosinski"
}

print("My favourite movie is", movie["title"], "which was released in", movie["year"], "and was directed by", movie["director"])

# add new keys to the dictionary
# revenue is updated as of June 13 2022
movie["budget"] = 170000000
movie["revenue"] = 747000000

# print difference between budget and revenue
difference = movie["revenue"]-movie["budget"]
print(difference)

# print if the movie is a good, bad or okay investment
if movie["budget"] > movie["revenue"]:
    print("That was a bad investment")
elif movie["revenue"] / movie["budget"] > 5:
    print("That was a great investment")
else: 
    print("That was an okay investment")

# create a dictionary for the population in NYC boroughs
pop_nyc = {
    "Manhattan": 1600000,
    "Brooklyn": 2600000,
    "Bronx": 1400000,
    "Queen": 2300000,
    "Staten Islan": 470000
}

# print population of Brooklyn
pop_nyc["Brooklyn"]

# create new variable 'total' to store combined population of all 5 boroughs
total = sum(pop_nyc.values())
print(total)

# print percentage of NYC's population who live in Manhattan (round to 1 decimal place)
print(round(pop_nyc["Manhattan"]/total*100,1))
