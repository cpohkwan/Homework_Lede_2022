# how old the user is

year = input("What year were you born in?")
year = int(year)

# keep asking until the year is less than 2022
while year > 2022:
    if year > 2022:
        year = input("Hello future! Would you please enter the correct year?")
        year = int(year)

age = 2022 - year
age = date.today().year - year

# how many times the user's heart has beaten
# Source: https://my.clevelandclinic.org/health/diagnostics/17402-pulse--heart-rate
# Adult heart rate is normally between 60 and 100 times per minute for adults. I take the average of 80 times per minute.

human_heartbeats = 80 * 60 * 24 * 365 * age
print(f"Your heart has beaten {human_heartbeats:,} times.")

# how many times a blue whale's heart has beaten 

whale_heartbeats = 11 * 60 * 24 * 365 * age
print(f"Your heart has beaten {whale_heartbeats:,} times.")

# how many times a rabbit's heart has beaten

rabbit_heartbeats = 340 * 60 * 24 * 365 * age

if rabbit_heartbeats > 1000000:
    rabbit_million = rabbit_heartbeats / 1000000
    print(f"A rabbit's heart has beaten {rabbit_million,.2f} million times.")

# how many times there has been a president from Democratic Party in office since they were born

if year <= 1960:
    num_presidents = 6
elif year <= 1962:
    num_presidents = 5
elif year <= 1976:
    num_presidents = 4
elif year <= 1992:
    num_presidents = 5
elif 
