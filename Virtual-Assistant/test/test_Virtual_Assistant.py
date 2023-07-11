from test_features import test_wishme, test_weather, test_websearch
from test_features.test_wishme import test_speak
from test_features.test_AppOpener import test_appopener_open, test_appopener_close, test_appopener_list
import speech_recognition as sr
import webbrowser
import pyautogui
import pytest



@pytest.fixture(autouse=True)
def audio():
    return "hiii"

@pytest.fixture(autouse=True)
def inp():
    return "hiii"



def test_takecommand():
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
    assert f"{query}"





class TestPragati():
    def test_pragati(audio):
        test_wishme.test_greetuser()
        print("I am Pragati ai your personal virtual assistant")
        test_speak("I am Pragati ai your personal virtual assistant")
        print("How can I help you?")
        test_speak("How can I help you?")

        if __name__ == "__main__":
            while True:
                query = test_takecommand().lower()
                print(query)

                ################    Greet-User/Wishme   ################
                if "good morning" in query:
                    test_wishme.test_greetuser()
                    assert test_wishme.test_greetuser().__contains__("good")
                
                elif "good afternoon" in query:
                    test_wishme.test_greetuser()
                    assert test_wishme.test_greetuser().__contains__("good")
                
                elif "good evening" in query:
                    test_wishme.test_greetuser()
                    assert test_wishme.test_greetuser().__contains__("good")

                elif "good night" in query:
                    test_wishme.test_greetuser()
                    assert test_wishme.test_greetuser().__contains__("good")

                ################    Date & Time    #################
                elif "date" in query:
                    test_wishme.test_date()
                    assert test_wishme.test_date().__contains__(",")

                elif "time" in query:
                    test_wishme.test_time()
                    assert test_wishme.test_date().__contains__(":")

                ################    Search Engine   #################
                elif "search for" in query:
                    querys = query.replace('search for','')
                    test_websearch.search_and_open(querys)
                    search_url = f"https://www.google.com/search?={querys}"
                    webbrowser.open(search_url)
                    test_speak(f"ok, searching for {querys}")
                    return query

                ################    Weather    ##################
                elif "weather" in query:
                    q = test_weather.get_weather("Nagpur")
                    test_speak(q)
                    print(q)
                    return query

                ################    Open/Close Different apps   ####################
                elif "start" in query:
                    inp = query
                    test_appopener_open(inp)
                    return query

                elif "close" in query:
                    inp = query
                    test_appopener_close(inp)
                    return query

                elif "list of apps" in query:
                    inp = query
                    test_appopener_list(inp)
                    return query

                ################    Opening Youtube_search   ####################
                elif "youtube" in query:
                    test_speak("what you want to search")
                    print("what you want to search?")
                    query = query.replace("search youtube","")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                    test_speak(f"searching on youtube for {query}")
                    assert query.__contains__("youtube")

                ################    Opening Different Web-sites    ######################

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
                            test_speak(f"opening {site[0]}")
                            webbrowser.open(site[1])

                ################    Windows Automation    ##################
                elif "maximize this window" in query:
                    pyautogui.hotkey('win','up')
                    assert query.__contains__("window")

                elif "minimize this window" in query:
                    pyautogui.hotkey('win','down')
                    assert query.__contains__("window")

                elif "shift this window" in query:   
                    #this will shift windows on the top
                    if "shift this window to right" in query:
                        pyautogui.hotkey('win','right')
                        assert query.__contains__("window")

                    elif "shift this window to left" in query:
                        pyautogui.hotkey('win','left')
                        assert query.__contains__("window")

                    elif "shift this window to top right" in query:
                        with pyautogui.hold('win'):
                            pyautogui.press(['right','up'])
                            assert query.__contains__("window")

                    elif "shift this window to top left" in query:
                        with pyautogui.hold('win'):
                            pyautogui.press(['left','up'])
                            assert query.__contains__("window")

                    elif "shift this window to bottom right" in query:
                        with pyautogui.hold('win'):
                            pyautogui.press(['right','down'])
                            assert query.__contains__("window")

                    elif "shift this window to bottom left" in query:
                        with pyautogui.hold('win'):
                            pyautogui.press(['left','down'])
                            assert query.__contains__("window")
        