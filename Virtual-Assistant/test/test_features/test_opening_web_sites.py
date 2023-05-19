from test_features.test_wishme import test_speak
from webbrowser import open, open_new, open_new_tab
import webbrowser

def test_youtube():
    url = "https://www.youtube.com"
    open(url)
    test_speak('opening youtube')

def test_w3schools():
    url = "https://www.w3schools.com"
    open(url)
    test_speak('opening w3schools')

def test_my_learning():
    url = "https://my-learning.w3schools.com/"
    open(url)
    test_speak('opening your programming learning')