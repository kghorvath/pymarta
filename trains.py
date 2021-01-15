import sys
from stations import stations
from lines import lines

refresh = 10

try:
    if sys.argv[1] == "-s":
        try:
            sys.argv[2]
        except:
            station = "f"
        else:
            station = sys.argv[2]
        stations(station,refresh)
    elif sys.argv[1] == "-l":
        lines(sys.argv[2],refresh)
except:
    print("Usage: python3 trains.py [OPTION] Argument \n")
    print("This tool prints a live display of MARTA trains. Data is sourced using the MARTA Rail Realtime \n RESTful API. Be sure to obtain an API key from https://www.itsmarta.com/developer-reg-rtt.aspx \n and export it to the MARTA_API_KEY environment variable. \n")
    print(" -s <station code>         Show trains by station. Valid inputs are MARTA station codes, \n for example \"n11\" or \"w4\". Entering no station code will display results for Five Points Station. \n")
    print(" -l <line>                 Show trains by line. Valid inputs are \"red\", \"gold\", \"blue\", or \"green\". ")