from tkinter import Tk, Text, Button, END
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from threading import Thread
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

def handle_response(text):
    response_map = {
        'hello': 'Hello sir, how may I assist you today?',
        'how are you': 'I am fine, thank you. What about you?',
        'fine': 'That is great to hear.',
        'time': f'The current time is {datetime.now().strftime("%H:%M")}.',
        'date': f'Today is {datetime.now().strftime("%A, %B %d, %Y")}.',
        'joke': tell_joke(),
        'bye': 'Goodbye sir, have a great day!',
    }
    for key, response in response_map.items():
        if key in text:
            return response
    return 'I did not understand that. Can you please rephrase?'
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

                # Display recognized text in the GUI
                output_text.insert(END, f'You: {text}\n')
                response = handle_response(text)
                speak(response)
                output_text.insert(END, f'Bot: {response}\n')
                if 'bye' in text:
                    break
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start.")
                
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

# Function to start speech recognition in a new thread
def start_recognition():
    recognition_thread = Thread(target=recognize_speech)
    recognition_thread.start()

# Create the main window
root = Tk()
root.title("SpeechBot Helper")
root.geometry("400x400")

# Create a text area for displaying recognized speech
output_text = Text(root, height=15, width=50)
output_text.pack(pady=10)

# Create a button to start recognition
start_button = Button(root, text="Start Listening", command=start_recognition)
start_button.pack(pady=5)

# Create a button to close the application
close_button = Button(root, text="Exit", command=root.quit)
close_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
