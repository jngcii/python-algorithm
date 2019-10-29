from collections import deque


def bfs(ladders, snakes, c):
    cnt = 0
    q = deque()
    q.append(1)
    c[1] = 0

    while q:
        p = q.popleft()

        for i in range(1, 7):
            np = p + i
            
            if np > 100: break

            for s in snakes:
                if np == s[0]:
                    np = s[1]
            for l in ladders:
                if np == l[0]:
                    np = l[1]

            if c[np] != -1: continue
            else: c[np] = c[p] + 1

            if np == 100:
                return
            else:
                q.append(np)


n, m = map(int, input().split())

ladders = []
snakes = []

for _ in range(n):
    x, y = map(int, input().split())
    ladders.append([x, y])

for _ in range(m):
    u, v = map(int, input().split())
    snakes.append([u, v])

check = [-1]*101

bfs(ladders, snakes, check)

print(check[100])