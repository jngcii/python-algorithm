def solution(budgets, M):
    
    small = M//len(budgets)
    big = max(budgets)
    
    if sum(budgets) <= M: return max(budgets)
    
    tmp = big
    
    while True:
        avg = (small + big)//2
        print(small, avg, big)
        s = 0
        
        for b in budgets:
            if b > avg:
                s += avg
            else:
                s += b
        if s > M:
            big = avg
        else:
            if tmp == avg:
                return avg
            tmp = avg
            small = avg