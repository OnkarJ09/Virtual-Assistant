import webbrowser

def search_and_open(querys):
    search_url = f"https://www.google.com/search?q={querys}"
    webbrowser.open(search_url)
