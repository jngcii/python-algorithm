def solution(foods, limit):
    
    past = 0
    j = 0
    
    if sum(foods) <= limit: return -1
    
    while past < limit:
        foods[j%len(foods)] -= 1
        
        j += 1
        past += 1
        
        while foods[j%len(foods)] == 0:
            j += 1
                
    return (j%len(foods)) + 1