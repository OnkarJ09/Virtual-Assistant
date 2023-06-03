from features.wishme import speak
import wikipedia



def wikipedia(querys):
    speak("searching wikipedia...")
    results = wikipedia.summary(querys, sentences=3)
    speak(f"according to wikipedia {results}")
    a = f"according to wikipedia {results}"
    print(a)