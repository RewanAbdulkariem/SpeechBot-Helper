import pyttsx3
import speech_recognition as sr
from datetime import datetime


# Initialize the converter
engine = pyttsx3.init()
# Initialize recognizer
rec = sr.Recognizer()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Reduce background noise by calibrating to the environment
with sr.Microphone() as source:
    print('Adjusting for ambient noise... Please wait.')
    rec.adjust_for_ambient_noise(source, duration=1)  # Adjust to the ambient noise level

    speak('Hello sir, how may I help you, sir.')

    while True:
        try:
            # Listen to the audio with a timeout
            print('you: ', end='')
            audio = rec.listen(source, timeout=5, phrase_time_limit=5)

            # Recognize speech using Google
            text = rec.recognize_google(audio)
            print(text)

            # Check if specific keywords exist in the recognized text
            if 'stop' in text:
                speak('Bye sir, have a nice day.')
                break
            elif any(greeting in text for greeting in ['hello', 'hi', 'hey']):
                speak('Hello sir, how may I assist you today?')
            elif 'how are you' in text:
                speak('I am fine, thank you. What about you?')
            elif 'fine' in text:
                speak('That is great to hear.')
            elif 'time' in text:
                current_time = datetime.now().strftime('%H:%M')
                speak(f'The current time is {current_time}.')
            else:
                speak('I did not understand that. Can you please rephrase?')
        
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
        
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
