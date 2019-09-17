from math import sqrt

def solution(brown, red):
    arr = []
    
    for i in range(1, int(sqrt(red))+1):
        if red % i == 0:
            arr.append((i, red//i))
            
    
    for a in arr:
        if a[0] * 2 + (a[1] + 2) * 2 == brown:
            return [a[1] + 2, a[0] + 2]
    
    
    answer = []
    return answer