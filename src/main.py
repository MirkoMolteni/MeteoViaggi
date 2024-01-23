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
    print("Quante tappe si volgiono fare?")
    nTappe = int(input())
    
    stages = []
    
    for i in range(0,nTappe):
        places = []
        city = input("Inserire la città: ")
        places = osm.getCity(city)
        for y in range(0,len(places)):
            print(str(y) + " - " + places[y]["display_name"] + " - " + places[y]["addresstype"])
            y+=1
            
        print("Inserire il numero della città desiderata: ")
        city = int(input())
        
        stages.append(places[city])
        
    # print(stages)
    # find the distance between the two cities
    for i in range(0,len(stages)-1):
        print("Da: " + stages[i]["display_name"] + " \nA: " + stages[i+1]["display_name"])
        route = ors.getRoute(stages[i]["lat"] + "," + stages[i]["lon"],stages[i+1]["lat"] + "," + stages[i+1]["lon"])
        print(route["features"][0]["properties"]["summary"]["distance"])
        print(route["features"][0]["properties"]["summary"]["duration"])
        print(route["features"][0]["geometry"]["coordinates"])
        print("--------------------------------------------------")
    
    # I look for the weather of those cities for the current day


if __name__ == "__main__":
    main()
