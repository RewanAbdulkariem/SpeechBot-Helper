# Overview
SpeechBot Helper is an interactive voice assistant application that utilizes text-to-speech and speech recognition technologies to respond to user queries and commands.

## Features

- Text-to-speech conversion using `gTTS` and `pyttsx3`
- Speech recognition for user commands
- Interactive responses based on user input
- Capability to tell the current time

## Prerequisites

- Python 3.x
- Required libraries:
  - `gTTS`
  - `pyttsx3`
  - `SpeechRecognition`
  
You can install the necessary libraries using pip:

```bash
pip install gTTS pyttsx3 SpeechRecognition
```

## Installation

Clone the repository:

```bash
git clone https://github.com/RewanAbdulkariem/SpeechBot-Helper.git
```
Navigate to the project directory:

```bash
cd SpeechBot-Helper
```
Install the required packages (if not already installed):

```bash
pip install gTTS pyttsx3 SpeechRecognition
```
## Running the Application
### Option 1: Running from Source
Clone this repository:
```bash
git clone https://github.com/RewanAbdulkariem/SpeechBot-Helper.git
```
Navigate to the project directory:
```bash
cd SpeechBot-Helper
```
Run the Python script:
```bash
python speech_bot.py
```
### Option 2: Running the Executable

- Navigate to the dist folder where the executable is located.
- Double-click the speech_bot.exe file to run the application.
## Usage
The project consists of four main components, each serving a specific functionality. You can run each script independently.

#### 1. Text to Speech using gTTS
Filename: [1-text_to_audio.py](1-text_to_audio.py)

This script converts a predefined text message into speech using the **gTTS** library and plays the generated audio. It's a simple demonstration of converting text to speech in a standalone manner.

#### 2. Text to Speech using pyttsx3 with File Input
Filename: [1-text_to_speech.py](1-text_to_speech.py)

This script reads text from a specified text file and converts it to speech using the **pyttsx3** library. This allows for flexibility in audio generation, as you can easily change the text content by editing the file.

#### 3. Speech Recognition Listening Loop
Filename:  [2-speech_to_text.py](2-speech_to_text.py)
This script initializes a speech recognition loop that listens for audio input from the user. It prints out the recognized text, providing a basic foundation for further interaction. This can be a good starting point for implementing more complex features based on user speech.

#### 4. Enhanced Speech Recognition with Responses and Time
Filename:[2-speech_recognition_interactive](2-speech_recognition_interactive.py)

This script offers an interactive experience where the assistant responds to user commands. 
### Final project
Filename:[SpeechBot.py](SpeechBot.py)


## Acknowledgements
- gTTS: Google Text-to-Speech API
- pyttsx3: Text-to-Speech conversion library
- SpeechRecognition: Library for performing speech recognition
### Summary of Updates:
- Each script is given a professional description, explaining its purpose and functionality in the context of the project.
- This detailed overview enhances the professionalism of the README and helps users understand the capabilities and structure of the project more clearly.