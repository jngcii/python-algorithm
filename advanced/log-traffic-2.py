def solution(lines):
    
    result = 0
    
    for idx, line in enumerate(lines):
        (DATE, TIME, CONST) = line.split(" ")
        CONST = float(CONST[:-1])
        
        (HH, MM, SS) = TIME.split(":")
        
        END_TIME = round((float(HH)*3600 + float(MM)*60 + float(SS)),3)
        
        START_TIME = round((END_TIME - CONST + 0.001),3)
        
        lines[idx] = [START_TIME, END_TIME]
    
    lines.sort(key=lambda x : x[0])
    
    for line in lines:
        i = 0
        maxim = 0
        
        MY_END = line[1]
        
        while i<len(lines) and round((MY_END + 0.999),3) >= lines[i][0]:
            
            CUR_LINE = lines[i]
            
            if MY_END <= CUR_LINE[1]: maxim += 1
            
            i += 1
                
        if maxim > result: result = maxim
            
    return result