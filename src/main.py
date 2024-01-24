from ors_lib import ORS
from osm_lib import OSM
from owm_lib import OWM
osm = OSM()
ors = ORS()
owm = OWM()
def main():
    global osm
    global ors
    global owm
    print("START")
    nTappe = int(input("Inserire il numero di tappe: "))
    
    stages = []
    
    for i in range(0,nTappe):
        places = []
        city = input("Inserire la città: ")
        places = osm.getCity(city)
        for y in range(0,len(places)):
            print(str(y) + " - " + places[y]["display_name"] + " - " + places[y]["addresstype"])
            y+=1
            
        city = int(input("Inserire il numero della città desiderata: "))
        
        stages.append(places[city])
        
    # print(stages)
    print("--------------------------------------------------")
    
    for i in range(0,len(stages)-1):
        # find the distance between the two cities
        print("Da: " + stages[i]["display_name"] + " \nA: " + stages[i+1]["display_name"])
        route = ors.getRoute(stages[i]["lon"] + "," + stages[i]["lat"],stages[i+1]["lon"] + "," + stages[i+1]["lat"])
        print("Distanza: " + str(route["features"][0]["properties"]["summary"]["distance"]/1000) + " km")
        # Look for the weather of those cities for the current day
        weather = owm.getWeather(stages[i]["lat"],stages[i]["lon"])
        print("Meteo: " + weather["weather"][0]["description"])
        print("--------------------------------------------------")
    

if __name__ == "__main__":
    main()
