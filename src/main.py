from ors_lib import ORS
from osm_lib import OSM
from owm_lib import OWM

def main():
    print("START")
    
    stages = []
    
    response = ""
    while response != "done":
        response = input("Insert a city: ")
        if response != "done":
            stages.append(response)
            
    print(stages)
    
    # find the coordinates of the two cities
    for i in stages:
        osm = OSM()
        city = osm.getCity(i)
        print(city)
        # TODO gestire il json di risposta
    # find the distance between the two cities
    # I look for the weather of those cities for the current day


if __name__ == "__main__":
    main()
