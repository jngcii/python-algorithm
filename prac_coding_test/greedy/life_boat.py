def solution(people, limit):
    n = len(people)
    people.sort(reverse=True)
    c = [False]*n
    
    res = 0
    
    j = n-1
    
    for i in range(n):
        cur = people[i]
        if c[i]: continue
        
        c[i] = True
        
        while j>=0 and cur + people[j] <= limit:
            if c[j]:
                j -= 1
                continue
            c[j] = True
            cur += people[j]
            j -= 1
        
        res += 1
        
        
    return res