# Cheong Poh Kwan
# June 8 2022
# Homework 1 - Updated

# Ask for user's year of birth
year = input("Hi there! In which year were you born?")
year = int(year)

# Ask user to enter year of birth again if they come from the future
while year > 2022:
    if year > 2022:
    print("Hello future!")
    year = int(input"Could you please enter the correct year?")

# Print user's age
age = 2022 - year
print(f"You are {age} years old.")

# Print user's heartbeat
# A adult's heart beats between 60 and 100 times per minute. I'll take the average - 80 times per minute. 
# Source: https://my.clevelandclinic.org/health/diagnostics/17402-pulse--heart-rate
human_heartbeat = 80 * 60 * 24 * 365 * age 
print(f"Your heart has beaten {human_heartbeat:,} times")

# Print blue whale's heartbeat
# A Blue whale's heart rate can go from 2 to 37 beats per minute depending whether they're diving or not. 
# Source: https://news.stanford.edu/2019/11/25/first-ever-recording-blue-whales-heart-rate/
whale_heartbeat_low = 2 * 60 * 24 * 365 * age
whale_heartbeat_high = 37 * 60 * 24 * 365 * age
print(f"A blue whale's heart has beaten from {whale_heartbeat_low:,} times to {whale_heartbeat_high:,} times.")

# Print rabbit's heartbeat
# A rabbit's resting heart rate is between 140 to 180 beats per minute. I'll take the average at 160. 
# https://www.medivet.co.uk/pet-care/pet-advice/heart-disease-in-rabbits/
rabbit_heartbeat = 160 * 60 * 24 * 365 * age
if rabbit_heartbeat >= 1000000:
    rabbit_million = rabbit_heartbeat / 1000000
print(f"A rabbit's heart has beaten {rabbit_million:.2f} million times.")

# Print user's age in Venus years
print(f"On Venus, you are {age/0.6152:.1f} years old.")

# Print user's age in Neptune years
print(f"On Neptune, you are {age/165:.1f} years old.")

# Print user's age difference from mine
if age == 37:
    print(f"You're as young as me!")
elif age < 37:
    print(f"You're {37 - age} younger than me.")
else:
    print(f"You're {age - 37} older than me.")

# Was user born in an odd or even year?
if year % 2 == 0: 
    print("You're born in an even year.")
else:
    print("You're born in an odd year.") 

# How many Democratic Presidents since user was born (from 1960 onwards) 
# Source: Wikipedia
# 1960-Nov 1963: Kennedy, Nov 1963-1969: Johnson, 1977-1981: Carter, 1993-2001: Clinton, 2009-2017: Obama, 2021-present: Biden
if year <= 1963: 
    num_president = 6
elif year <= 1969:
    num_president = 5
elif year <= 1981:
    num_president = 4   
elif year <= 2001:
    num_president = 3 
elif year <= 2017:
    num_president = 2 
elif year <= 2022:
    num_president = 1 

print(f"There have been {num_president} Democratic Presidents in office since you're born.")

# Which US President was in office when user was born?
# Not the best list because many Presidents take office in late January, so if someone was born in Jan 1 2021, it's still President Trump technically before Joe Biden was inaugurated on Jan 20. 
if year < 1960:
    name_president = "I can't recall"
elif year <= 1963: 
    name_president = "John F Kennedy"
elif year <= 1969:
    name_president = "Lyndon B Johnson"
elif year <= 1974:
    name_president = "Richard Nixon"
elif year <= 1977:
    name_president = "Gerald Ford"
elif year <= 1981:
    name_president = "Jimmy Carter"
elif year <= 1989:
    name_president = "Ronald Reagan"   
elif year <= 1993:
    name_president = "George H W Bush"   
elif year <= 2001:
    name_president = "Bill Clinton"
elif year <= 2009:
    name_president = "George W Bush"
elif year <= 2017:
    name_president = "Barack Obama"
elif year <= 2021:
    name_president = "Donald Trump"
elif year <= 2022:
    name_president = "Joe Biden"

print(f"When you were born, {name_president} was in office.")