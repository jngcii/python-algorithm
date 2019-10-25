from collections import deque

cnt = 1

def bfs(a, c, K):
    global cnt
    
    q = deque()
    q.append(((1,0), 0))
    c[1] = False
    
    while q:
        p, m = q.popleft()
        
        a[p[0]].sort()
        for ai in a[p[0]]:
            if ai[1] + m <= K and c[ai[0]]:
                c[ai[0]] = False
                cnt += 1
                q.append((ai, ai[1] + m))
                

def solution(N, road, K):
    global cnt
    
    a = [[] for _ in range(N+1)]
    c = [True for _ in range(N+1)]
    
    for r in road:
        a[r[0]].append((r[1], r[2]))
        a[r[1]].append((r[0], r[2]))
        
    c[1] = False
        
    bfs(a, c, K)

    return cnt