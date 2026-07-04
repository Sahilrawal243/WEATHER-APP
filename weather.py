import requests

# Your OpenWeatherMap API Key
API_KEY = "29025a28dc0d45e08b5a7793c0f1e97d"

# Ask the user for a city name
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    print("\n===== Weather Report =====")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"].title())
    print("Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("\n❌ Error:", data.get("message", "Unable to fetch weather data."))
