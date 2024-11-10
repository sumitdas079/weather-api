import requests
from loguru import logger
from icecream import ic

# get city name based on coordinates
def fetch_city_name(latitude, longitude):
    url = "https://api-bdc.net/data/reverse-geocode-client"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "localityLanguage": "en",
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        # ic(data)
        city = data.get("locality", data.get("principalSubdivision", "Unknown location"))
        return city
    
    except requests.RequestException as e:
        # print(f"An error occurred during reverse geocoding: {e}")
        logger.error(f"Cannot fetch location")
        return "Unknown location"

# fetch weather update of the city
def fetch_weather(latitude, longitude):
    city = fetch_city_name(latitude, longitude)
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    
    try:
        response = requests.get(weather_url, params=weather_params)
        response.raise_for_status()
        data = response.json()
        current_weather = data.get("current_weather", {})

        if current_weather:
            temperature = current_weather.get("temperature", "N/A")
            windspeed = current_weather.get("windspeed", "N/A")
            weather_time = current_weather.get("time", "N/A")
            
            # print(f"Current weather in {city} ({latitude}, {longitude}):")
            # print(f"Temperature: {temperature}°C")
            # print(f"Wind Speed: {windspeed} m/s")
            # print(f"Observation Time: {weather_time}")
            logger.info(f"Weather stats of {city}: Temp={temperature}°C, Wind Speed={windspeed} m/s, Observation Time: {weather_time}")
        else:
            # print("No current weather data available.")
            logger.error("No current weather data available.")
    except requests.RequestException as e:
        print(f"An error occurred while fetching weather data: {e}")

latitude = 22.5744   
longitude = 88.3629  
fetch_weather(latitude, longitude)
