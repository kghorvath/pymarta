import os
import curses
import station_codes
from time import sleep
from marta.api import get_trains

os.system("")

#Display refresh rate in seconds
refresh = 10

#Define our line colors
COLOR = {
        "HEADER": "\033[1m",
        "BLUE": "\033[94m",
        "GREEN": "\033[92m",
        "RED": "\033[91m",
        "GOLD": "\033[93m",
        "RESET": "\033[0m",
        }

#Input of station name
station = input("Enter Station: ")

#We add "Station" to the end here so the user doesn't have to type it out
station = str(station + " Station")

screen = curses.initscr()

#Define our header rows here
header = ['LINE', 'DESTINATION', 'ARRIVAL']
header_row = str("{: <8} {: <25} {: <15}".format(*header))
station_row = str("MARTA - " + station)

#Loop until the user kills the program
while True:
    screen.clear()
    screen.addstr(0,0,station_row)
    screen.addstr(1,0,header_row)
    
    #Get our train objects using the MARTA API
    trains = get_trains(station=station)
    
    #Display up to 5 next trains unless there are fewer in the data
    if len(trains) < 5:
        a = len(trains)
    else:
        a = 5
    
    for i in range(0,a):
        nexttrain = [trains[i].line, trains[i].destination, trains[i].waiting_time]
        nexttrain_row = str("{: <8} {: <25} {: <15}".format(*nexttrain))
        screen.addstr(i+2,0,nexttrain_row)
        screen.refresh()
    sleep(refresh) #Sleep for display refresh

curses.endwin()
