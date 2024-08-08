import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
# import smtplib
# import comtypes

# installing sapi 5 api of microsoft
engine = pyttsx3.init('sapi5')

# now creating a voice to get property voices
voices = engine.getProperty('voices')

# setting voices property
engine.setProperty('voice',voices[0].id)
# print(voices[0].id)


# Now writing speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Now experimentally creating a wish function to wish me
def wish_me():
    hour = int(datetime.datetime.now().hour)

    # now speaking in order of day and night with if else statement
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, sir")

    else:
        speak("Good Evening, Sir")

    speak("My name is Aegis , How May I assist you Today?")


# Now we are writing the take command function which is used to take commands from user through microphone in the speech form and returns output in string 
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Always try to listen best...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing.....")
        query = recognizer.recognize_google(audio, language= 'en-in')

        print("user said:" , query)
        
    except Exception as e:
        print(f"Error: {e}")
        # now say that again
        print("say that again please...")
        return "none"
    return query


# def send_email(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     # loading password from the file
#     with open('X:\\Web Projects-20220717T100137Z-001\\Projects\\Python _Project\\Artificial Intelligence_Project\\passwrd.txt', 'r') as file:
#         password = file.read().strip()
#     server.login('h847448@gmail.com', 'X:\\Web Projects-20220717T100137Z-001\\Projects\\Python _Project\\Artificial Intelligence_Project\\passwrd.txt')
#     server.sendmail('h847448@gmail.com', to ,content)
#     server.close()


# now  __name__ = = '__main__' is equal to 
if __name__ == "__main__":
    speak("Hello World!, I am the world's first AGI... aka, 'Artificial General Intelligence'... ") 
    wish_me()
    while True:
    # if 1:
        query = take_command().lower()

    # now implementing logic to execute task based on query
        if 'wikipedia' in query:
            speak("searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 5)
            speak("According to wikipedia")
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
            project = "X:\\Web Projects-20220717T100137Z-001\\Projects\\Python _Project\\Artificial Intelligence_Project"
            os.startfile(project)

        # elif 'send email' in query:
        #     try:
        #         speak("what should i write for an e-mail,sir... ")
        #         content = take_command()
        #         to = "devashishgautam8@gmail.com"
        #         send_email(to, content)
        #         speak("sir, email has been sent! ")
        #     except Exception as e:
        #         print(e)
        #         speak("sorry for the inconvenience")
                