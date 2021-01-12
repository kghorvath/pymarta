import os
from marta.api import get_trains

os.system("")

COLOR = {
        "HEADER": "\033[1m",
        "BLUE": "\033[94m",
        "GREEN": "\033[92m",
        "RED": "\033[91m",
        "GOLD": "\033[93m",
        "RESET": "\033[0m",
        }

station = input("Enter Station: ")

station = str(station + " Station")
trains = get_trains(station=station)

if len(trains) < 3:
    a = len(trains)
else:
    a = 3
print(COLOR["HEADER"] + "\n=====Next",a,"trains=====" + COLOR["RESET"])
for i in range(0,a):
    destination = str("Destination: " + trains[i].destination)
    arrival = str("Arrival: " + trains[i].waiting_time)
    print(COLOR[trains[i].line], destination,"\n",arrival,"\n" + COLOR["RESET"])
