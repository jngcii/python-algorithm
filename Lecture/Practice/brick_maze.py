from collections import deque

n, m = map(int, input().split())

a = [list(map(int, list(input()))) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):

    q = deque()

    q.append((y, x, 1, 1))
    a[y][x] = -1

    while q:
        y, x, r, c = q.popleft()

        if y == n-1 and x == m-1: return c

        for k in range(4):

            ny, nx = y+dy[k], x+dx[k]

            if 0 <= ny < n and 0 <= nx < m:
                if r == 0:
                    if a[ny][nx] == 0:
                        q.append((ny, nx, 0, c+1))
                        a[ny][nx] = -1
                else:
                    if a[ny][nx] == 1:
                        q.append((ny, nx, r-1, c+1))
                        a[ny][nx] = -1
                    elif a[ny][nx] == 0:
                        q.append((ny, nx, r, c+1))
                        a[ny][nx] = -1

print(bfs(0,0))