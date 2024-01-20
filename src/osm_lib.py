import requests

class OSM:
    
    def __init__(self):
        self.key = None
        
    def getCity(self, cityName):
        url = f'https://nominatim.openstreetmap.org/search?q={cityName}&format=json&addressdetails=1'
        
        response = requests.get(url)
        
        if(response.status_code != 200):
            print(response.status_code)
            print(response.content)
            print(response.url)
            return "Error"
        else:
            data = response.json()
            return data