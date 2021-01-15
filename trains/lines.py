import curses
from station_codes import station_code
from curses import wrapper
from time import sleep
from marta.api import get_trains

#station_header = str(station + " " + code.upper())

def lines(line,refresh):
    def board(screen):
        #Initialize colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)

        #Loop until the user kills the program
        while True:
            screen.clear()
            for j in range(0,refresh):
                
                #Our pretty MARTA banner :)
                screen.addstr(0,0,"/", curses.color_pair(1) | curses.A_BOLD)
                screen.addstr(0,1,"/", curses.color_pair(2) | curses.A_BOLD)
                screen.addstr(0,2,"/", curses.color_pair(3) | curses.A_BOLD)
                screen.addstr(0,4,"MARTA - ", curses.A_BOLD | curses.A_UNDERLINE)
                screen.addstr(0,12,line.capitalize() + " Line", curses.A_BOLD | curses.A_UNDERLINE)

                screen.addstr(1,0,"TRAIN", curses.A_BOLD)
                screen.addstr(1,7,"DIRECTION", curses.A_BOLD)
                screen.addstr(1,20,"NEXT STATION", curses.A_BOLD)
                screen.addstr(1,50,"ARRIVAL", curses.A_BOLD)

                #Get our train objects using the MARTA API
                trains = get_trains(line=line)
                trainid = []
                #Display up to 50 next trains unless there are fewer in the data
                a = len(trains)
                #Get rid of duplicates
                for i in range(0,a):
                    if trains[i].train_id not in trainid:
                        trainid.append(trains[i].train_id)
                        if trains[i].line == "RED":
                            c = 1
                        elif trains[i].line == "GOLD":
                            c = 2
                        elif trains[i].line == "BLUE":
                            c = 3
                        elif trains[i].line == "GREEN":
                            c = 4
                        
                        #Translate direction
                        if trains[i].direction == "N":
                            trains[i].direction = "Northbound"
                        if trains[i].direction == "S":
                            trains[i].direction = "Southbound"
                        if trains[i].direction == "E":
                            trains[i].direction = "Eastbound"                
                        if trains[i].direction == "W":
                            trains[i].direction = "Westbound"

                        screen.addstr(i+2,0,trains[i].train_id[0:3],curses.color_pair(c))
                        screen.addstr(i+2,7,trains[i].direction)
                        screen.addstr(i+2,20,trains[i].station.title())
                        screen.addstr(i+2,50,trains[i].waiting_time)
                screen.addstr(15,0,"Next update in (" + str(refresh-j) + ") second(s)   ")
                screen.refresh()
                sleep(1) #Sleep for display refresh
    wrapper(board)
