import requests
from key import OWMKey

class OWM:
    def __init__(self):
        self.key = OWMKey
        
    def getWeather(self, lat, lon):
        url = 'https://api.openweathermap.org/data/2.5/weather'
        
        params = {'lat': lat,
                'lon': lon,
                'appid': self.key,
                'units': 'metric',
                'lang': 'it'}
        response = requests.get(url, params=params)
        
        if(response.status_code != 200):
            print(response.status_code)
            print(response.content)
            print(response.url)
            return "Error"
        else:
            data = response.json()
            return data