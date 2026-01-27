import os
import requests

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,  # original
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        return f"Sorry, I couldn’t fetch the weather for {city}."

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    return (
        f"🌤 Weather in {city}:\n"
        f"Temperature: {temp}°C\n"
        f"Condition: {description}\n"
        f"Humidity: {humidity}%"
    )
