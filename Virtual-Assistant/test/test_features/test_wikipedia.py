from test_features.test_wishme import test_speak
import wikipedia
import pytest


@pytest.fixture(autouse=True)
def querys():
    return "cricket"

def test_wikipedia(querys):
    test_speak("searching wikipedia...")
    results = wikipedia.summary(querys, sentences=3)
    test_speak(f"according to wikipedia {results}")
    a = f"according to wikipedia {results}"
    print(a)
    assert a.__contains__("according")