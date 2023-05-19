import requests
import json

def test_get_weather(location):
    api_key = 'YOUR_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': location, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()
    temperature = str(data['main']['temp'])
    humidity = str(data['main']['humidity'])
    weather_conditions = str(data['weather'][0]['description'])
    a = f"the weather condition in '{location}' city is:'{weather_conditions}' tempearture is:'{temperature}�C' and humidity is:'{humidity}%'"
    print(a)
    assert a.__contains__("the weather condition in")
    

