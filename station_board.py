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

header = ['LINE', 'DESTINATION', 'ARRIVAL']
print("\n" + COLOR["HEADER"] + "{: <8} {: <20} {: <15}".format(*header) + COLOR["RESET"])

if len(trains) < 5:
    a = len(trains)
else:
    a = 5
for i in range(0,a):
    nexttrain = [trains[i].line, trains[i].destination, trains[i].waiting_time]
    print(COLOR[trains[i].line] + "{: <8} {: <20} {: <15}".format(*nexttrain))
