from features.wishme import speak
from webbrowser import open, open_new, open_new_tab
import webbrowser

def youtube():
    url = "https://www.youtube.com"
    open(url)
    speak('opening youtube')

def w3schools():
    url = "https://www.w3schools.com"
    open(url)
    speak('opening w3schools')

def my_learning():
    url = "https://my-learning.w3schools.com/"
    open(url)
    speak('opening your programming learning')