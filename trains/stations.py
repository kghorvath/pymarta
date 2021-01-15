import curses
from station_codes import station_code
from curses import wrapper
from time import sleep
from marta.api import get_trains

#station_header = str(station + " " + code.upper())

def stations(code,refresh):
    def board(screen):
        station = station_code(code)
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
                screen.addstr(0,12,station, curses.A_UNDERLINE)

                screen.addstr(1,0,"LINE", curses.A_BOLD)
                screen.addstr(1,7,"DESTINATION", curses.A_BOLD)
                screen.addstr(1,33,"ARRIVING", curses.A_BOLD)
            
                #Get our train objects using the MARTA API
                trains = get_trains(station=station)
            
                #Display up to 5 next trains unless there are fewer in the data
                if len(trains) < 5:
                    a = len(trains)
                else:
                    a = 5
            
                for i in range(0,a):
                    if trains[i].line == "RED":
                        c = 1
                    elif trains[i].line == "GOLD":
                        c = 2
                    elif trains[i].line == "BLUE":
                        c = 3
                    elif trains[i].line == "GREEN":
                        c = 4
                    if trains[i].destination == "Airport":
                        line = "✈"
                        c = 5
                    else:
                        line = "●"
                    
                    screen.addstr(i+2,0,line,curses.color_pair(c))
                    screen.addstr(i+2,7,trains[i].destination)
                    screen.addstr(i+2,33,trains[i].waiting_time)
                screen.addstr(8,0,"Next update in (" + str(refresh-j) + ") second(s)   ")
                screen.refresh()
                sleep(1) #Sleep for display refresh
    wrapper(board)
