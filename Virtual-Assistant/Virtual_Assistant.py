from email.mime import audio
from features import weather, websearch, wishme
from features.wishme import speak
from features.AppOpener import appopener_open, appopener_close, appopener_list
import speech_recognition as sr
import webbrowser
import time
import pyautogui
import os


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
                elif "start" in query:
                    inp = query
                    appopener_open(inp)

                elif "close" in query:
                    inp = query
                    appopener_close(inp)

                elif "list of apps" in query:
                    inp = query
                    appopener_list(inp)

                ################    Opening Youtube_search   ####################
                elif "youtube" in query:
                    speak("what you want to search")
                    print("what you want to search?")
                    q = takecommand().lower()
                    q = q.replace("search for","") 
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                    speak(f"searching on youtube for {query}")

                ################    Opening Different Web-sites    ##################

                elif "open" in query:
                    sites = [["youtube", 'https://www.youtube.com'], 
                             ["facebook", 'https://www.facebook.com'], 
                             ["instagram", 'https://www.instagram.com'], 
                             ["w3schools", 'https://www.w3schools.com'], 
                             ["w3schools learning", 'https://my-learning.w3schools.com'], 
                             ["whatsapp", 'https://web.whatsapp.com'], 
                             ["telegram", 'https://web.telegram.com'], 
                             ["github", 'https://github.com'], 
                             ["replit", 'https://replit.com'], 
                             ["g mail", 'https://mail.google.com'],
                             ["google", 'https://www.google.com'],
                             ["google calendar", 'https://calendar.google.com'],
                             ["online python packages", 'https://pypi.org'],
                             ["chat g p t", 'https://chat.openai.com']]
                    for site in sites:
                        if f"open {site[0]}" in query:
                            speak(f"opening {site[0]}")
                            webbrowser.open(site[1])

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
