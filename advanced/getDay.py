def solution(a, b):
    sum = b
    
    WEEK = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    
    DAY = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    month = a-1
    
    if month != 0:
        for m in range(month):
            sum += DAY[m]

    return WEEK[((sum%7)+4)%7]
        
        