from email.mime import audio
from features import weather, websearch, wishme, opening_web_sites, wikipedia
from features.wishme import speak
from features.AppOpener import appopener_open, appopener_close, appopener_list
import speech_recognition as sr
import webbrowser
import time
import pyautogui
import os
import wikipedia as wiki


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
        speak('please say that again')
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

                ################    Wikipedia   ###################
                elif "wikipedia" in query:
                    wikipedia.wikipedia()
                    query = query.replace('search wikipedia for','')
                    results = wiki.summary(query, sentences=3)
                    speak(f"according to wikipedia {results}")
                    print(f"according to wikipedia {results}")

                ################    Opening Web-Sites   ####################
                elif "youtube" in query:
                    speak("what you want to search")
                    print("what you want to search?")
                    query = query.replace("search youtube","")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                    speak(f"searching on youtube for {query}")

                elif "w3schools" in query:
                    opening_web_sites.w3schools()

                elif "my learning" in query:
                    opening_web_sites.my_learning()

                elif "facebook" in query:
                    opening_web_sites.facebook()
                
                elif "instagram" in query:
                    opening_web_sites.instagram()

                elif "whatsapp" in query:
                    opening_web_sites.whatsapp()

                elif "telegram" in query:
                    opening_web_sites.telegram()

                elif "github" in query:
                    opening_web_sites.github()

                elif "replit" in query:
                    opening_web_sites.replit()

                elif "gmail" in query:
                    opening_web_sites.gmail()

                elif "google" in query:
                    opening_web_sites.google()

                elif "calendar" in query:
                    opening_web_sites.calendar()

                elif "python packages" in query:
                    opening_web_sites.pypi()

                elif "chat g p t" in query:
                    opening_web_sites.chatgpt()

                ################    Windows Automation    ##################
                elif "maximize this window" in query:
                    pyautogui.hotkey('win','up')

                elif "minimize this window" in query:
                    pyautogui.hotkey('win','down')

                elif "shift this window" in query:   
                    #this will shift windows on the top
                    if "shift this window to right" in query:
                        pyautogui.hotkey('win','right')

                    elif "shift this window to left" in query:
                        pyautogui.hotkey('win','left')

                    elif "shift this window to top right" in query:
                        with pyautogui.hold('win'):
                            pyautogui.press(['right','up'])

                    elif "shift this window to top left" in query:
                        with pyautogui.hold('win'):
                            pyautogui.press(['left','up'])

                    elif "shift this window to bottom right" in query:
                        with pyautogui.hold('win'):
                            pyautogui.press(['right','down'])

                    elif "shift this window to bottom left" in query:
                        with pyautogui.hold('win'):
                            pyautogui.press(['left','down'])

                










Pragati.pragati(audio)
