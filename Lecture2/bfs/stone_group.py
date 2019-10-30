from collections import deque
import sys


a, b, c = map(int, input().split())

sum = a+b+c
if sum%3 != 0:
    print(0)
    sys.exit(0)
    

check = [[False] * 1500 for _ in range(1500)]

check[a][b] = True

q = deque()

q.append((a, b))

res = 0

while q:
    pa, pb = q.popleft()

    if pa == pb and pb == sum-pa-pb:
        res = 1
        break

    if pa <= 0 or pb <= 0 or sum-pa-pb <= 0: break
    
    if pa>pb:
        na = pa-pb
        nb = pb*2

    elif pa<pb:
        na = pa*2
        nb = pb-pa

    else:
        na = pa
        nb = pb

    if check[na][nb] == False:
        check[na][nb] = True
        q.append((na, nb))
        
    
    if pa>sum-pa-pb:
        na = pa - (sum-pa-pb)
        nb = pb
    elif pa<sum-pa-pb:
        na = pa*2
        nb = pb
    else:
        na = pa
        nb = pb
    
    if check[na][nb] == False:
        check[na][nb] = True
        q.append((na, nb))

    
    if pb>sum-pa-pb:
        na = pa
        nb = pb-(sum-pa-pb)
    elif pb<sum-pa-pb:
        na = pa
        nb = pb*2
    
    if check[na][nb] == False:
        check[na][nb] = True
        q.append((na, nb))



print(res)