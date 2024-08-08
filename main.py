import os
import sys
import pyaudio
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random

# initializing sapi5 for Windows text-to-speech
engine = pyttsx3.init('sapi5')

# getting the available voices
voices = engine.getProperty('voices')

# setting the voice property to the first available voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Wish the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Sir")
    else:
        speak("Good Evening, Sir")
    speak("My name is Vortex, How may I assist you today?")

def take_command():
    """Take voice commands from the user and return them as a string."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Always try to listen best...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("User said:", query)
    except sr.UnknownValueError:
        print("Sorry, I did not get that. Please say that again...")
        return "none"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "none"
    return query

# if __name__ == '__main__' block to run the assistant
if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("https://www.stackoverflow.com")
        elif 'open music' in query:
            groove_dir = 'P:\\groove_dir\\Ringtones'
            songs = os.listdir(groove_dir)
            print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(groove_dir, random_song))
        elif 'current time' in query:
            string_time = datetime.datetime.now().strftime('%H:%M:%S')
            print(string_time)
            speak(f"Sir, the current time is {string_time}")
        elif 'open project' in query:
            project = ("X:\\Web Projects-20220717T100137Z-001\\Projects\\Python _Project\\Artificial "
                       "Intelligence_Project")
            os.startfile(project)
