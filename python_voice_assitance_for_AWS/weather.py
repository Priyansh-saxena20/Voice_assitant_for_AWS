import requests
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)   # here you can change voice

def speak(audio):
    '''
    This function let your AI to speak
    '''
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    '''
    this function will take voice command from user
    and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1   # this will help user to take 1 sec pause so that AI will not complete the voice in middle
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "none"
    return query

def get_weather(api_key, city):
    # API endpoint URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        # Send a GET request to the API
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            # Extract relevant weather information
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            # Print the weather information
            print(f"Weather in {city}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {int(temperature-276)} ºC")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(" Failed to retrieve weather information.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Set your OpenWeatherMap API key
API_KEY = "90fae44a573e63fae6ac460676146dbb"

# Get weather information for a specific city
speak("Tell me the city")
city_name = takeCommand().lower()
get_weather(API_KEY, city_name)
