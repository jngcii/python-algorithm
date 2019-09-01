def change(x, n):
    if x==0: return "0"
    
    res = ""
    
    while x > 0:
        remain = x % n
        remain = str(remain)
        
        if remain == "10": remain = "A"
        elif remain == "11": remain = "B"
        elif remain == "12": remain = "C"
        elif remain == "13": remain = "D"
        elif remain == "14": remain = "E"
        elif remain == "15": remain = "F"
            
        x = x // n
        
        res = remain + res
    
    return res
    

def solution(n, t, m, p):
    
    allNum = t*m
    
    string = ""
    answer = ""
    
    for i in range(allNum):
        num = change(i, n)
        string += num
        
    i = 0
    while len(answer) < t:
        if i%m == p-1:
            answer += string[i]
        i += 1
            
    return answer
        