from email.mime import audio
from features import weather, websearch, wishme, opening_web_sites
from features.wishme import speak
from features.AppOpener import appopener_open, appopener_close, appopener_list
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
                
                elif "good afternoon" in query:
                    wishme.greetuser()
                
                elif "good evening" in query:
                    wishme.greetuser()

                elif "good night" in query:
                    wishme.greetuser()

                ################    Date & Time    #################
                elif "date" in query:
                    wishme.date()

                elif "time" in query:
                    wishme.time()

                ################    Search Engine   #################
                elif "search for" in query:
                    querys = query.replace('search for','')
                    websearch.search_and_open(querys)
                    search_url = f"https://www.google.com/search?={querys}"
                    webbrowser.open(search_url)
                    speak(f"ok, searching for {querys}")

                ################    Weather    ##################
                elif "weather" in query:
                    q = weather.get_weather("Nagpur")
                    speak(q)
                    print(q)

                ################    Open/Close Different apps   ####################
                elif "open" in query:
                    inp = query
                    appopener_open(inp)

                elif "close" in query:
                    inp = query
                    appopener_close(inp)

                elif "list of apps" in query:
                    inp = query
                    appopener_list(inp)

                ################    Opening Web-Sites   ####################
                elif "youtube" in query:
                    opening_web_sites.youtube()

                elif "w3schools" in query:
                    opening_web_sites.w3schools()

                elif "my learning" in query:
                    opening_web_sites.my_learning()









Pragati.pragati(audio)
