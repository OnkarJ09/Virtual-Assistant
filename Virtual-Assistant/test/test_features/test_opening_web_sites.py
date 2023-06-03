from test_features.test_wishme import test_speak
from webbrowser import open, open_new, open_new_tab
import webbrowser
import pytest


@pytest.fixture(autouse=True)
def audio():
    return "hiii"

def test_w3schools():
    url = "https://www.w3schools.com"
    open(url)
    test_speak('opening w3schools')
    assert url.__contains__("w3schools")

def test_my_learning():
    url = "https://my-learning.w3schools.com/"
    open(url)
    test_speak('opening your programming learning')
    assert url.__contains__("my-learning")

def test_facebook():
    url = "https://www.facebook.com/"
    open(url)
    test_speak('opening facebook')
    assert url.__contains__("facebook")

def test_instagram():
    url = "https://www.instagram.com/"
    open(url)
    test_speak('opening instagram')
    assert url.__contains__("instagram")

def test_whatsapp():
    url = "https://web.whatsapp.com/"
    open(url)
    test_speak('opening whatsapp')
    assert url.__contains__("whatsapp")

def test_telegram():
    url = "https://web.telegram.org/"
    open(url)
    test_speak('opening telegram')
    assert url.__contains__("telegram")

def test_github():
    url = "https://github.com/"
    open(url)
    test_speak('opening github')
    assert url.__contains__("github")

def test_replit():
    url = "https://replit.com/"
    open(url)
    test_speak('opening replit')
    assert url.__contains__("replit")

def test_gmail():
    url = "https://mail.google.com/"
    open(url)
    test_speak('opening gmail')
    assert url.__contains__("mail")

def test_google():
    url = "https://www.google.com"
    open(url)
    test_speak('opening google')
    assert url.__contains__("google")

def test_calendar():
    url = "https://calendar.google.com/"
    open(url)
    test_speak('opening calendar')
    assert url.__contains__("calendar")

def test_pypi():
    url = "https://pypi.org/"
    open(url)
    test_speak('opening python packages website')
    assert url.__contains__("pypi")

def test_chatgpt():
    url = "https://chat.openai.com/"
    open(url)
    test_speak('opening chat g p t')
    assert url.__contains__("chat")