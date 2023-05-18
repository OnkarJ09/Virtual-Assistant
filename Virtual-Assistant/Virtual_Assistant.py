from features import weather, websearch, wishme
from features.wishme import speak
from webbrowser import open
import speech_recognition as sr
import webbrowser


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1             #for pausing after how many second's
        r.adjust_for_ambient_noise(source) #For noise cancelation
        audio = r.listen(source)
    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print('---')
        return '---'
    return f"{query}"



class Pragati():
    def pragati(audio):
        wishme.greetuser()
        print("I am Pragati ai your personal virtual assistant")
        speak("I am Pragati ai your personal virtual assistant")
        print("How can I help you?")
        speak("How can I help you?")

        if __name__ == "__main__":
            while True:
                query = takecommand().lower()
                print(query)

                ################    Greet-User/Wishme   ################
                if "good morning" in query:
                    wishme.greetuser()
                    print(wishme.greetuser())
                    return 'good morning,Sir!'
                
                elif "good afternoon" in query:
                    wishme.greetuser()
                    print(wishme.greetuser())
                    return 'good afternoon'
                
                elif "good evening" in query:
                    wishme.greetuser()
                    print(wishme.greetuser())
                    return 'good evening'

                elif "good night" in query:
                    wishme.greetuser()
                    print(wishme.greetuser())
                    return 'good night'

                ################    Date & Time    #################
                elif "date" in query:
                    wishme.date()
                    return 'date'

                elif "time" in query:
                    wishme.time()
                    return 'time'
