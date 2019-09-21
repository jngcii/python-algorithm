from collections import deque

n, m = map(int, input().split())

c = [False] * 100000


def bfs(x, m, cnt):
    
    q = deque()
    q.append((x, 0))


    while q:
        p, idx = q.popleft()

        if p == m:
            return idx

        c[p] = True

        for i in [p+1, p-1, p*2]:
            if 0 <= i < 100000:
                if c[i] == False:
                    q.append((i, idx+1))
                    c[i] = True

res = bfs(n, m, -1)

print(res)