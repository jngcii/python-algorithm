n = int(input())
result = 0

def go(a, idx, my, mxm):
    
    if idx == len(a):
        global result
        if result < mxm:
            result = mxm
        return
    
    if my>0:
        go(a, idx+1, 0, mxm+a[idx]*my)

    go(a, idx+1, my+1, mxm-a[idx])
    

for ni in range(n):
    result = 0
    cnt = int(input())
    a = list(map(int, input().split()))
    my = 0
        
    go(a, 0, my, 0)
    print(f'#{ni+1} {result}')