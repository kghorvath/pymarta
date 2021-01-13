import os
import curses
import station_codes
from curses import wrapper
from time import sleep
from marta.api import get_trains

os.system("")

#Display refresh rate in seconds
refresh = 10

#Input of station name
station = input("Enter Station: ")

#We add "Station" to the end here so the user doesn't have to type it out
station = str(station + " Station")

#Define our header rows here
header = ['LINE', 'DESTINATION', 'ARRIVAL']
header_row = str("{: <8} {: <25} {: <15}".format(*header))
station_row = str("MARTA - " + station)

def main(screen):
    
    #Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    #Loop until the user kills the program
    while True:
        screen.clear()
        screen.addstr(0,0,station_row, curses.A_UNDERLINE)
        screen.addstr(1,0,header_row, curses.A_BOLD)
    
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
            if trains[i].line == "RED":
                c = 1
            elif trains[i].line == "GOLD":
                c = 2
            elif trains[i].line == "BLUE":
                c = 3
            elif trains[i].line == "GREEN":
                c = 4
            screen.addstr(i+2,0,nexttrain_row, curses.color_pair(c))
            screen.refresh()
        sleep(refresh) #Sleep for display refresh

wrapper(main)