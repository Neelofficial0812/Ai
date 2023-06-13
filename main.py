import pyttsx3
import datetime
import smtplib
import wikipedia
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if len(voices) >= 2:
        engine.setProperty('voice', voices[1].id)  # Select the second voice
    else:
        print("Not enough voices found. Using the default voice.")

    engine.say(text)
    engine.runAndWait()

def about_you():
    speak("I am an AI assistant powered by neha. I am designed to provide helpful information and assist with various tasks.")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_google():
    webbrowser.open("https://www.google.com")

# Example usage:
speak("Hello, I am neha. How can I assist you today? sir")

# Example usage:
while True:
    user_input = input("You: ")

    if "time" in user_input.lower():
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak("The current time is " + current_time)
    elif "date" in user_input.lower():
        current_date = datetime.date.today().strftime("%B %d, %Y")
        speak("Today's date is " + current_date)
    elif "about you" in user_input.lower():
        about_you()
    elif "country" in user_input.lower():
        speak("Your country is India and I also live in India, on your PC.")
    elif "wikipedia" in user_input.lower():
        speak("Searching Wikipedia...")
        user_input = user_input.replace("wikipedia", "")
        results = wikipedia.summary(user_input, sentences=4)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif "open youtube" in user_input.lower():
        speak("Opening YouTube...")
        open_youtube()
    elif "open google" in user_input.lower():
        speak("Opening Google...")
        open_google()
    elif "play music" in user_input.lower():
        music_dir = 'C:\\Users\\PLAYTIME\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music...")
    elif "play songs" in user_input.lower():
        music_dir = 'C:\\Users\\PLAYTIME\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music...")
    elif "play song" in user_input.lower():
        music_dir = 'C:\\Users\\PLAYTIME\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music...")
    elif "play a songs" in user_input.lower():
        music_dir = 'C:\\Users\\PLAYTIME\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music...")
    elif "music" in user_input.lower():
        music_dir = 'C:\\Users\\PLAYTIME\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music...")
    elif 'open audacity' in user_input.lower():
        coodPath = "C:\\Program Files\Audacity\\Audacity.exe"
        os.startfile(coodPath)
        speak("opening audacity")

    else:
        speak("You said: " + user_input)
