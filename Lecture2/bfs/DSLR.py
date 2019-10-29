from collections import deque

def D(n):
    return n*2%10000

def S(n):
    if n == 0: return 9999
    else: return n-1

def L(n):
    return (n%1000)*10 + n//1000

def R(n):
    return n//10 + (n%10)*1000


def bfs(c, t1, t2):
    q = deque()
    q.append(t1)
    
    while q:
        p = q.popleft()

        dp = D(p)
        if c[dp] == '':
            c[dp]=c[p] + 'D'
            q.append(dp)
        
        sp = S(p)
        if c[sp] == '':
            c[sp]=c[p] + 'S'
            q.append(sp)
    
        lp = L(p)
        if c[lp] == '':
            c[lp]=c[p] + 'L'
            q.append(lp)
        
        rp = R(p)
        if c[rp] == '':
            c[rp]=c[p] + 'R'
            q.append(rp)

        if dp==t2 or sp==t2 or lp==t2 or rp==t2: return
        



n = int(input())
t = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append((a,b))

for test in t:
    c = ['' for _ in range(10001)]
    c[test[0]] = "M"
    bfs(c, test[0], test[1])
    print(c[test[1]][1:])