import speech_recognition as sr
import pyttsx3
import requests
import pywhatkit as kit
import wikipedia

engine = pyttsx3.init()

def speak(text):

    print(f"Assistant: {text}")  # Print the assistant's response to the console
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Could you please repeat?")
            return None
        return command





API_KEY = 'e89156462c6ae7c9615dc0fceda2d571'


def get_weather(city_name):
    """Fetch weather data from OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get('cod') != 200:
        print(f"API Response: {data}")
        speak("Weather data is not available. Please try again later.")
        return

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    speak(
        f"The weather in {city_name} is currently {weather_description} with a temperature of {temperature} degrees Celsius.")


def get_time_date(command):
    from datetime import datetime
    if "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

def search_wikipedia(topic):
    try:
        summary = wikipedia.summary(topic, sentences=1)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"Your query is ambiguous. Here are some options: {e.options}")
    except wikipedia.exceptions.PageError:
        speak("The page does not exist.")

def search_google(query):
    kit.search(query)
    speak(f"Searching Google for {query}")
