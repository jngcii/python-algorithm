def sol(words, n):
    if len(words) <= 1: return words
    arr = []
    
    for word in words:
        if len(arr) == 0:
            arr.append([word])
        else:
            is_exist = False
            for a in arr:
                if len(word) > n and len(a[0]) > n:
                    if a[0][n] == word[n]:
                        a.append(word)
                        is_exist = True
            if is_exist==False:
                arr.append([word])
    
    words = [sol(a, n+1) for a in arr]
    
    return words

def count(res, floor):
    s = 0
    for idx, r in enumerate(res):
        if type(r[0])==list:
            result = count(r, floor+1)
            s += result
        else:
            s += floor
    return s

def solution(words):
    res = sol(words, 0)
    s = 0
    
    floor = 1
    
    return count(res, floor)