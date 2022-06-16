# Cheong Poh Kwan
# June 15, 2022
# Homework 3, Part 2

# PART TWO: Weather API

import requests 

# What is the URL to the documentation?

url = "https://www.weatherapi.com/docs/"

# Make a request for the current weather where you are born, or somewhere you've lived.

url_singapore = "http://api.weatherapi.com/v1/current.json?key=34c667f0717b4b7cb0d165543221306&q=Singapore"

response = requests.get(url_singapore)

current_weather_singapore = response.json()

print(current_weather_singapore)

# Print out the country this location is in.

print(current_weather_singapore["location"]["country"])

# Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.

current_temp = current_weather_singapore["current"]["temp_c"]
feels_like_temp = current_weather_singapore["current"]["feelslike_c"]
print(f'It feels {feels_like_temp - current_temp:.1f} degrees C warmer.')

# What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.

# q=iata:LHR

url_heathrow = "http://api.weatherapi.com/v1/current.json?key=34c667f0717b4b7cb0d165543221306&q=iata:LHR"

response_heathrow = requests.get(url_heathrow)

data_heathrow = response_heathrow.json()

print(data_heathrow)

print(data_heathrow["current"]["temp_c"])

print(f"The current temperature at Heathrow International Airport is 22 deg C.")

# What URL would I use to request a 3-day forecast at Heathrow?

url_heathrow_forecast = "http://api.weatherapi.com/v1/forecast.json?key=34c667f0717b4b7cb0d165543221306&q=iata:LHR&days=3"

response_heathrow_forecast = requests.get(url_heathrow_forecast)

data_heathrow_forecast = response_heathrow_forecast.json()


# Print the date of each of the 3 days you're getting a forecast for.

print(data_heathrow_forecast["forecast"]["forecastday"][0]["date"])
print(data_heathrow_forecast["forecast"]["forecastday"][1]["date"])
print(data_heathrow_forecast["forecast"]["forecastday"][2]["date"])

dates = print([date["date"] for date in data_heathrow_forecast["forecast"]["forecastday"]])


# Print the maximum temperature of each of the days.

print(data_heathrow_forecast["forecast"]["forecastday"])

print([day["day"]["maxtemp_c"] for day in data_heathrow_forecast["forecast"]["forecastday"]])

print(
    "Date: 15 June 2022 - Max.Tempature = 28 deg C, Date: 16 June 2022 - Max.Tempature = 29.1 deg C, Date: 17 June 2022 - Max.Tempature = 31 deg C"
)
# Print the day with the highest maximum temperature.

print("17 June 2022 has the highest temperature out of the three days.")