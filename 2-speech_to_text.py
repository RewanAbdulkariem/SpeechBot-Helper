import speech_recognition as sr

# Initialize recognizer
rec = sr.Recognizer()

# Reduce background noise by calibrating to the environment
with sr.Microphone() as source:
    while True:
        print('You can speak now.')
        try:
            audio = rec.listen(source, timeout=5, phrase_time_limit=5)
            # Recognize speech using Google
            text = rec.recognize_google(audio)
            print(f"You said: {text}")
        except:
            print("Sorry, I did not understand that.")