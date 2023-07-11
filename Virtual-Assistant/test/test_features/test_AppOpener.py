from AppOpener import open, close, mklist, give_appnames
import os
import pytest



@pytest.fixture(autouse=True)
def inp():
    return "hiii"


def test_appopener_open(inp):
    app_name = inp.replace('open', '')
    open(app_name, match_closest=True)
    assert app_name.__contains__(app_name)

def test_appopener_close(inp):
    app_name = inp.replace('close', '')
    close(app_name, match_closest=True, output=False)
    assert app_name.__contains__(app_name)

def test_appopener_list(inp):
    mklist(name='app_data.json')
    give_appnames()
    assert os.path.exists("G:/PCP/A.I/Virtual-Assistant/Virtual-Assistant/app_data.json")


    
    
    
     