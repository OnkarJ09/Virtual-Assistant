import datetime
import pyttsx3


engine = pyttsx3.init('sapi5')  #initilize pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)   #Change the voice of the Assistant
engine.getProperty('rate')
engine.setProperty('rate', 150)


def speak(audio):          # Simple speak function for pyttsx3 run and wait
    engine.say(audio)
    engine.runAndWait()

def greetuser():            # It will wish the user according to the Time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        a = "Good Morning"
        print(a)
        speak(a)
    elif hour > 12 and hour <= 17:
        a = "Good Afternoon"
        print(a)
        speak(a)
    elif hour > 17 and hour <= 20:
        a = "Good Evening"
        print(a)
        speak(a)
    else:
        a = "Good Night"
        print(a)
        speak(a)


def time():
    time = datetime.datetime.now().strftime('%H:%M')
    speak(time)
    print(time)


def date():
    date = datetime.datetime.now().strftime('%B %d,%Y')
    speak(date)
    print(date)

