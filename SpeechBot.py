import tkinter as tk
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import threading
import requests  # For fetching weather and news data
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to fetch weather information
def get_weather():
    # Replace with your own API key from OpenWeatherMap
    API_KEY = 'your_openweathermap_api_key'
    CITY = 'Cairo'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            main = data['main']
            weather_desc = data['weather'][0]['description']
            temp = main['temp']
            return f'The current temperature in {CITY} is {temp}°C with {weather_desc}.'
        else:
            return "Sorry, I couldn't retrieve the weather information."
    except Exception as e:
        return f"An error occurred: {e}"

# Function to fetch news headlines
def get_news():
    # Replace with your own API key from NewsAPI
    API_KEY = 'your_newsapi_key'
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        articles = response.json().get('articles', [])
        if articles:
            headlines = [article['title'] for article in articles[:5]]
            return "Here are the latest news headlines: " + ", ".join(headlines)
        else:
            return "Sorry, I couldn't retrieve the news."
    except Exception as e:
        return f"An error occurred: {e}"

# Function to tell a random joke
def tell_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, and now it won't stop sending me to the beach!",
        "Why don’t scientists trust atoms? Because they make up everything!"
    ]
    return random.choice(jokes)

# Speech recognition logic
def recognize_speech():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('Adjusting for ambient noise... Please wait.')
        rec.adjust_for_ambient_noise(source, duration=1)  # Adjust to ambient noise level
        speak('Hello sir, how may I help you, sir.')

        while True:
            try:
                # Listen to the audio with a timeout
                audio = rec.listen(source, timeout=5, phrase_time_limit=5)
                text = rec.recognize_google(audio)
                print(text)
                # Display recognized text in the GUI
                output_text.insert(tk.END, f'You: {text}\n')
                
                # Check if specific keywords exist in the recognized text
                if 'stop' in text:
                    speak('Bye sir, have a nice day.')
                    break
                elif any(greeting in text for greeting in ['hello', 'hi', 'hey']):
                    response = 'Hello sir, how may I assist you today?'
                    speak(response)
                    output_text.insert(tk.END, f'Bot: {response}\n')
                elif 'how are you' in text:
                    response = 'I am fine, thank you. What about you?'
                    speak(response)
                    output_text.insert(tk.END, f'Bot: {response}\n')
                elif 'fine' in text:
                    response = 'That is great to hear.'
                    speak(response)
                    output_text.insert(tk.END, f'Bot: {response}\n')
                elif 'time' in text:
                    current_time = datetime.now().strftime('%H:%M')
                    response = f'The current time is {current_time}.'
                    speak(response)
                    output_text.insert(tk.END, f'Bot: {response}\n')
                elif 'date' in text:
                    current_date = datetime.now().strftime('%A, %B %d, %Y')
                    response = f'Today is {current_date}.'
                    speak(response)
                    output_text.insert(tk.END, f'Bot: {response}\n')

                elif 'weather' in text:
                    weather_response = get_weather()
                    speak(weather_response)
                    output_text.insert(tk.END, f'Bot: {weather_response}\n')
                elif 'news' in text:
                    news_response = get_news()
                    speak(news_response)
                    output_text.insert(tk.END, f'Bot: {news_response}\n')
                elif 'joke' in text:
                    joke_response = tell_joke()
                    speak(joke_response)
                    output_text.insert(tk.END, f'Bot: {joke_response}\n')
                else:
                    response = 'I did not understand that. Can you please rephrase?'
                    speak(response)
                    output_text.insert(tk.END, f'Bot: {response}\n')

            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start.")
                
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

# Function to start speech recognition in a new thread
def start_recognition():
    recognition_thread = threading.Thread(target=recognize_speech)
    recognition_thread.start()

# Create the main window
root = tk.Tk()
root.title("SpeechBot Helper")
root.geometry("400x400")

# Create a text area for displaying recognized speech
output_text = tk.Text(root, height=15, width=50)
output_text.pack(pady=10)

# Create a button to start recognition
start_button = tk.Button(root, text="Start Listening", command=start_recognition)
start_button.pack(pady=5)

# Create a button to close the application
close_button = tk.Button(root, text="Exit", command=root.quit)
close_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
