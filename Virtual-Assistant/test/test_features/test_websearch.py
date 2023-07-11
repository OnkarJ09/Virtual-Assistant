import webbrowser
import pytest


@pytest.fixture(autouse=True)
def querys():
    return "hiii"

def test_search_and_open(querys):
    search_url = f"https://www.google.com/search?q={querys}"
    webbrowser.open(search_url)
    assert f"{querys}"