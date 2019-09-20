import sys
from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
d = [[True] * m for _ in range(n)]
res = 10001

def bsf(y, x, cnt):

    global res

    if y == n-1 and x == m-1:
        res = min(res, cnt)

    q = deque()

    d[y][x] = False
    q.append((y, x))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if a[ny][nx] == 1 and d[ny][nx]:
                    y, x = ny, nx
                    d[y][x] = False
                    q.append((y, x))
                    bsf(y, x, cnt + 1)

bsf(0, 0, 1)

print(res)



# n-1, m-1 로 도착해야함.