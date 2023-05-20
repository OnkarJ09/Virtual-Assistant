import datetime
import pyttsx3
import pytest

engine = pyttsx3.init('sapi5')  #initilize pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)   #Change the voice of the Assistant
engine.getProperty('rate')
engine.setProperty('rate', 150)



@pytest.fixture(autouse=True)
def audio():
    return "hiii"

def test_speak(audio):          # Simple speak function for pyttsx3 run and wait
    engine.say(audio)
    engine.runAndWait()

def test_greetuser():            # It will wish the user according to the Time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        a = "Good Morning"
        print(a)
        test_speak(a)
    elif hour > 12 and hour <= 17:
        a = "Good Afternoon"
        print(a)
        test_speak(a)
    elif hour > 17 and hour <= 20:
        a = "Good Evening"
        print(a)
        test_speak(a)
    else:
        a = "Good Night"
        print(a)
        test_speak(a)
    assert a.__contains__("Good")


def test_time():
    time = datetime.datetime.now().strftime('%H:%M')
    test_speak(time)
    print(time)
    assert time.__contains__(":")


def test_date():
    date = datetime.datetime.now().strftime('%B %d,%Y')
    test_speak(date)
    print(date)
    assert date.__contains__(",")

