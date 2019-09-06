def solution(n, interval, limit, timetable):
    result = -1
    limitation = n * limit
    INIT_TIME = 9*60
    
    timetable = [int(i.split(":")[0])*60 + int(i.split(":")[1]) for i in timetable]
    bus_time = [(i-1)*interval + INIT_TIME for i in range(n, 0, -1)]
    
    last_bus = bus_time[0]

    
    while True:
        this_bus = bus_time.pop()
        
        if this_bus == last_bus:
            for i in range(limit):
                if timetable:
                    person = min(timetable)
                    if person <= this_bus:
                        if i == limit - 1:
                            result = person - 1
                            break
                        timetable.remove(person)
                else: break
            if result == -1:
                result = this_bus
            break
                
        else:
            for i in range(limit):
                if timetable:
                    person = min(timetable)
                    if person <= this_bus:
                        if limitation == 1:
                            result = person - 1
                            break
                        else:
                            limitation -= 1
                            timetable.remove(person)

            if result != -1: break
            else: limitation = len(bus_time)*limit
                
    R_HH = result // 60
    R_MM = result % 60
    
    if R_HH <10:
        R_HH = "0" + str(R_HH)
    else: R_HH = str(R_HH)
        
    if R_MM <10:
        R_MM = "0" + str(R_MM)
    else: R_MM = str(R_MM)
        
    return R_HH+":"+R_MM