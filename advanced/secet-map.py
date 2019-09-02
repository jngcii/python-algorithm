def solution(n, arr1, arr2):
    binArr1 = []
    for a1 in arr1:
        b1 = ""
        
        for i in range(n):
            rest = a1%2
            a1=a1//2
            b1 = str(rest) + b1
        
        binArr1.append(b1)
        
    binArr2 = []
    for a2 in arr2:
        b2 = ""
        
        for i in range(n):
            rest = a2%2
            a2=a2//2
            b2 = str(rest) + b2
        
        binArr2.append(b2)
    
    res = []
    for i in range(n):
        r = ""
        for j in range(n):
            if binArr1[i][j] == "1" or binArr2[i][j] == "1":
                r += "#"
            else: r += " "
                
        res.append(r)
        
    return res
    