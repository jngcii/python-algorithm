def solution(cookie):
    
    for i in range(len(cookie), 1, -1):
        
        res = 0
    
        for j in range(len(cookie) - i + 1):

            c = cookie[j:j+i]
            
            for q in range(1, len(c)):
                if sum(c[:q]) == sum(c[q:]): res = max(res, sum(c[:q]))
            
        if res != 0: return res
    
    return 0