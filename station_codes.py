def station_code(code):
    if code == "n1":
        return str("Peachtree Center Station")
    elif code == "n2":
        return str("Civic Center Station")
    elif code == "n3":
        return str("North Ave Station")
    elif code == "n4":
        return str("Midtown Station")
    elif code == "n5":
        return str("Arts Center Station")
    elif code == "n6":
        return str("Lindbergh Station")
    elif code == "n7":
        return str("Buckhead Station")
    elif code == "n8":
        return str("Medical Center Station")
    elif code == "n9":
        return str("Dunwoody Station")
    elif code == "n10":
        return str("Sandy Springs Station")
    elif code == "n11":
        return str("North Springs Station")
    elif code == "ne7":
        return str("Lenox Station")
    elif code == "ne8":
        return str("Brookhaven Station")
    elif code == "ne9":
        return str("Chamblee Station")
    elif code == "ne10":
        return str("Doraville Station")
    elif code == "s1":
        return str("Garnett Station")
    elif code == "s2":
        return str("West End Station")
    elif code == "s3":
        return str("Oakland City Station")
    elif code == "s4":
        return str("Lakewood Station")
    elif code == "s5":
        return str("East Point Station")
    elif code == "s6":
        return str("College Park Station")
    elif code == "s7":
        return str("Airport Station")
    elif code == "e1":
        return str("Georgia State Station")
    elif code == "e2":
        return str("King Memorial Station")
    elif code == "e3":
        return str("Inman Park Station")
    elif code == "e4":
        return str("Edgewood Candler Park Station")
    elif code == "e5":
        return str("East Lake Station")
    elif code == "e6":
        return str("Decatur Station")
    elif code == "e7":
        return str("Avondale Station")
    elif code == "e8":
        return str("Kensington Station")
    elif code == "e9":
        return str("Indian Creek Station")
    elif code == "w1":
        return str("Omni Dome Station")
    elif code == "w2":
        return str("Vine City Station")
    elif code == "w3":
        return str("Ashby Station")
    elif code == "w4":
        return str("West Lake Station")
    elif code == "w5":
        return str("Hamilton E Holmes Station")
    elif code == "p4":
        return str("Bankhead Station")
    elif code == "f":
        return str("Five Points Station")
    else:
        raise Exception("Invalid station code!")