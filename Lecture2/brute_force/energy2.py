n = int(input())
a = list(map(int, input().split()))

def go(a):
    n = len(a)

    if n == 2:
        return 0
    
    res = 0
    for i in range(1, n-1):
        e = a[i-1]*a[i+1]
        b = a[:i] + a[i+1:]
        e += go(b)
        
        if e > res:
            res = e
        
    return res

print(go(a))