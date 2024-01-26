# pip install sppech_recognition
# pip instal pyttsx3
#pip install pywhatkit
# pip install wikipedia
# pip install pyaudio

import speech_recognition as sr
import pyttsx3
import pywhatkit

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Function to capture audio and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"User: {command}")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            command = ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            command = ""

        return command

def process_command(command):
    """Function to process user commands."""
    if "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif "stop" in command:
        speak("Stopping playback.")
        pywhatkit.stop_playback()
    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching for {query}")
        pywhatkit.search(query)
    else:
        speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        command = take_command()
        if "exit" in command:
            speak("Goodbye!")
            break
        process_command(command)
