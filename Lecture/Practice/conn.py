from collections import deque


n, m = map(int, input().split())

a = [[] for _ in range(n+1)]
c = [False] * (n+1)
c[0] = True

res = 0


for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)


def bfs(x):
    c[x] = True

    q = deque()
    q.append(x)

    while q:
        p = q.popleft()
        
        for i in a[p]:
            if c[i] == False:
                c[i] = True
                q.append(i)

for k in range(1, n+1):
    if c[k] == False:
        res += 1
        bfs(k)
            
print(res)
