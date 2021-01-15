import os
from station_codes import station_code
from marta.api import get_trains

station = os.environ.get('MARTA_STATION')
t1 = 0
t2 = 0
def nexttrain():
    trains = get_trains(station=station)
    print(trains)
    for i in range(0,20):
        print(trains[i].direction)
        if t1 == 0:
            if trains[i].direction == "N":
                direction1 = "Northbound"
                time1 = trains[i].waiting_time
                t1 = 1
            if trains[i].direction == "E":
                direction1 = "Eastbound"
                time1 = trains[i].waiting_time
                t1 = 1
        if t2 == 0:
            if trains[i].direction == "S":
                direction2 = "Southbound"
                time2 = trains[i].waiting_time
                t2 = 0
            if trains[i].direction == "W":
                direction2 = "Westbound"
                time2 = trains[i].waiting_time
                t2 = 0
nexttrain()    
print("Next " + direction1 + " train arrives in " + time1)
print("Next " + direction2 + " train arrives in " + time2)
