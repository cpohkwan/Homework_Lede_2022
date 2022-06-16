#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[2]:


url = "https://api.weatherapi.com/v1/current.json?key=34c667f0717b4b7cb0d165543221306&q=Singapore"


# In[3]:


response = requests.get(url)


# In[4]:


data = response.json()


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[5]:


print(data)


# In[6]:


current_wind_speed = data["current"]["wind_kph"]
print(f"The current wind speed in Singapore is {current_wind_speed} km/hour.")


# In[7]:


current_temp = data["current"]["temp_c"]
feels_like_temp = data["current"]["feelslike_c"]
difference = feels_like_temp - current_temp
print(f"It feels {difference:.2f} degrees C warmer than it actually is.")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[8]:


url = "https://api.weatherapi.com/v1/astronomy.json?key=34c667f0717b4b7cb0d165543221306&q=Singapore&dt=2022-06-17"


# In[9]:


response = requests.get(url)


# In[10]:


data = response.json()


# In[11]:


moon_phase = data["astronomy"]["astro"]["moon_phase"]
moon_illumination = data["astronomy"]["astro"]["moon_illumination"]
print(f"{moon_illumination} per cent of the moon will be visible tomorrow.")


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[12]:


url = "https://api.weatherapi.com/v1/forecast.json?key=34c667f0717b4b7cb0d165543221306&q=Singapore&days=1"
response = requests.get(url)
data = response.json()


# In[13]:


max_temp = data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
min_temp = data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
print(f"The difference between the highest and lowest temperatures for today is {max_temp-min_temp:.2f} deg C.")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# I can rename the data variables to 1) data_current, 2) data_astronomy, 3) data_forecast 

# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[19]:


url = "https://api.weatherapi.com/v1/forecast.json?key=34c667f0717b4b7cb0d165543221306&q=Singapore&days=3"
response = requests.get(url)
data_3day = response.json()


# In[85]:


dates = data_3day["forecast"]["forecastday"]
for date in dates:
    if date["day"]["maxtemp_c"] >= 25:
        print(date["date"], "-", date["day"]["maxtemp_c"], "deg C", "It's warm.")
    else: 
        print(date["date"], "-", date["day"]["maxtemp_c"], "deg C", "It's cold.")


# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[57]:


url = "https://api.weatherapi.com/v1/forecast.json?key=34c667f0717b4b7cb0d165543221306&q=Singapore&days=7&aqi=yes"
response = requests.get(url)
data_7day = response.json()


# In[59]:


# dates = data_7day["forecast"]["forecastday"][3]
# print(dates)


# **"IndexError: list index out of range"** - 
# I can print only 3 days worth of weather forecase on the free plan. 

# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[62]:


print("The hottest day is June 16, with temperature going as high as 28.8 deg C. But it's actually considered a relatively cooling day going by the norm in tropical climate.")


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[64]:


url = "https://api.weatherapi.com/v1/forecast.json?key=34c667f0717b4b7cb0d165543221306&q=Miami&days=1"
response = requests.get(url)
data_miami = response.json()


# In[84]:


miami_1day = data_miami["forecast"]["forecastday"]
for day in miami_1day:
    # print(day.keys())
    # print(day["hour"])
    for hour in day["hour"]:
        if hour["cloud"] > 50:
            print(hour["time"], "-", hour["temp_c"], "deg C", "and cloudy")
        else: 
            print(hour["time"], "-", hour["temp_c"], "deg C")  


# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[99]:


# 85 deg F is about 29.4 deg C

temp_hot = 0

for day in miami_1day:
    for hour in day["hour"]:
        if hour["temp_c"] > 29.4:
            temp_hot = temp_hot + 1 
    print(f"For {temp_hot/24*100} per cent of the time in the next 24 hours or so in Miami, the temperature will be above 29.4 deg C, or 85 deg F.")


# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# US$4/month

# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# I guess I'll have to sign up for another account to get another API key, or work on getting rich!
