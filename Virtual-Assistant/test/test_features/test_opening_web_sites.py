from test_features.test_wishme import test_speak
from webbrowser import open, open_new, open_new_tab
import webbrowser
import pytest


@pytest.fixture(autouse=True)
def audio():
    return "hiii"

def test_youtube():
    url = "https://www.youtube.com"
    open(url)
    test_speak('opening youtube')
    assert url.__contains__("youtube")

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