import requests
from key import ORSKey

class ORS:
    def __init__(self):
        self.key = ORSKey
        
    def getRoute(self, start, end):
        url = 'https://api.openrouteservice.org/v2/directions/driving-car'
        headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        }
        params = {'api_key': self.key,
                'start': start,
                'end': end,
                'headers': headers}
        response = requests.get(url, params=params)
        
        if(response.status_code != 200):
            print(response.status_code)
            print(response.content)
            print(response.url)
            return "Error"
        else:
            data = response.json()
            return data