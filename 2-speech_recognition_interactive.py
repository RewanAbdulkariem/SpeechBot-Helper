import speech_recognition as sr

# Initialize recognizer
rec = sr.Recognizer()

# Reduce background noise by calibrating to the environment
with sr.Microphone() as source:
    print('Adjusting for ambient noise... Please wait.')
    rec.adjust_for_ambient_noise(source, duration=1)  # Adjust to the ambient noise level

    print('You can speak now.')

    while True:
        try:
            # Listen to the audio with a timeout
            print('me: ')
            audio = rec.listen(source, timeout=5, phrase_time_limit=5)

            # Recognize speech using Google
            text = rec.recognize_google(audio)
            print(f"You said: {text}")

            # Check if specific keywords exist in the recognized text
            if 'stop' in text:
                break
            elif any(greeting in text for greeting in ['hello', 'hi', 'hey']):
                print('Hello sir, how may I help you?')
            elif 'how are you' in text:
                print('I am fine, thank you.\nWhat about you?')
            elif 'fine' in text:
                print('That is great to hear.')
            else:
                print('I did not get that.')
        
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
        
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
