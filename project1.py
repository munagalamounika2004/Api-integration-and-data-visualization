# Import required libraries
import requests
import matplotlib.pyplot as plt

# OpenWeatherMap API Key (Replace with your own)
API_KEY = "e7aa6379766251b44e3053010a4c6afa"  # TODO: Hide this API key before uploading to GitHub

# Specify the city for which we want weather data
city = "Hyderabad"  

# Construct the API request URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Fetch data from the API
response = requests.get(url)

# Convert response to JSON format
data = response.json()

# Check if the API request was successful
if response.status_code == 200:
    # Extract relevant weather details
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather = data["weather"][0]["description"]

    # Print the extracted data in a readable format
    print("=" * 40)
    print(f"🌍 Weather Report for {city.upper()} 🌍")
    print("=" * 40)
    print(f"🌦 Condition   : {weather.capitalize()}")
    print(f"🌡 Temperature : {temperature}°C")
    print(f"💧 Humidity    : {humidity}%")
    print(f"🔽 Pressure    : {pressure} hPa")
    print("=" * 40)

    # Visualizing the data using a bar chart
    categories = ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"]
    values = [temperature, humidity, pressure]

    # Create the bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(categories, values, color=["orange", "blue", "green"])
    plt.title(f"Weather Conditions in {city}")
    plt.ylabel("Value")
    plt.show()

else:
    # Print an error message if API request fails
    print("❌ Error fetching weather data!")
    print("🔹 Reason:", data.get("message", "Unknown error"))
