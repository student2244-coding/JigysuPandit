import requests

# Function to fetch weather data
def get_weather(city_name, api_key):
    # Base URL for OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    # Sending a request to the API
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London&appid=abcdef12345&units=metric"
)
    
    # Checking if the response is successful
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()
        
        # Extracting relevant information
        city = data['name']
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Display the weather information
        print(f"Weather Report for {city}:")
        print(f"Description: {weather_description.capitalize()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error: Unable to fetch data.")

# Example usage
city_name = input("Enter the city name: ")
api_key = "YOUR_API_KEY"  # Replace with your actual API key
get_weather(city_name, api_key)
