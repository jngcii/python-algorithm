def solution(priorities, location):
    
    sortedP = sorted(priorities, reverse=True)
    
    i = 0
    while sortedP != priorities:
        if max(priorities[i:]) != priorities[i]:
            priorities.append(priorities.pop(i))
            if location == i:
                location = len(priorities)-1
            else: location -= 1

        else:
            if location == i: return locat
            i += 1
        
    print(priorities)
        
    return location+1
