# install necessary libraries for this app

from flask import Flask, jsonify, request, render_template
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the API key from the environment variable
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def home():
    return render_template('index.html')  # Render the front-end template

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')  # Get city name from URL query parameter
    if not city:
        return render_template('index.html', error='Please provide a city name')  # Return error to front-end

    try:
        # Call OpenWeatherMap API
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        data = response.json()

        # Check if the response is successful
        if response.status_code != 200:
            return render_template('index.html', error=data.get("message", "Error fetching weather data"))
        
        # Print weather data in terminal in JSON format
        print(f"Weather data for {city}: {data}")

        # Prepare weather data for front-end
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"]  # Get weather icon from OpenWeatherMap
        }

        return render_template('index.html', weather=weather_info)  # Display weather data on the front-end
    
    except Exception as e:
        return render_template('index.html', error=str(e))  # Handle exceptions

if __name__ == '__main__':
    app.run(debug=True)
