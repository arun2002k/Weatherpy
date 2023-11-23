import requests

# Your api key from OpenWeathermap
api_key = " " 
api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter the city : ")

response = requests.get(
    url = api_url,
    params = {
        "q": city,
        "appid" : api_key,
        "units" : "metric",
    }
)

weather_data = response.json()
# weather qualities like humidity, Moisture, cloud, rainfall etc can be printed here only temperature is printed.
print(city, "temperature is", weather_data['main']['temp'], "°c")