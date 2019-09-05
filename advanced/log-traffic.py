def solution(lines):
    
    for idx, line in enumerate(lines):
        (DAY, TIME, TT) = line.split(" ")
        TT = float(TT[:-1])
        
        (HH, MM, SS) = TIME.split(":")
        
        ET = float(HH)*3600 + float(MM)*60 + float(SS)
        ST = ET - TT
        ST -= 0.001
        
        lines[idx] = [ST, ET]
        
    lines.sort(key=lambda x : x[0])
    
    print(lines)
    
    result = 0
    
    for idx, line in enumerate(lines):
        maxim = 1
        
        MY_ST = line[0]
        MY_ET = line[1]
        
        i = 0
        while i < len(lines) and round(lines[i][0],3) < round(MY_ET+0.998,3):
            if len(lines)==2:print(lines[i][0], MY_ET+0.998)
                
            if i == idx:
                i += 1
                continue
            
            if round(lines[i][1], 3) >= round(MY_ET,3):
                maxim += 1
            i += 1
                
        if maxim > result: result = maxim
            
    
    return result