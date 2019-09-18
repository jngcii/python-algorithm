from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

res = 0

def bfs(a):
    b = [[0]*m for _ in range(n)]

    q = deque()

    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
            if b[i][j] == 2:
                q.append((i,j))

    while q:
        (x,y) = q.popleft()
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if 0 <= ny < n and 0 <= nx < m and b[ny][nx] == 0:
                b[y][x] = 2
                q.append((ny, nx))
        
    cnt = 0

    for i in range(n):
        for j in range(m):
            if b[i][j]==0:
                cnt += 1

    return cnt

for y1 in range(n):
    for x1 in range(m):
        if a[y1][x1] != 0: continue

        for y2 in range(n):
            for x2 in range(m):
                if a[y2][x2] != 0: continue

                for y3 in range(n):
                    for x3 in range(m):
                        if a[y3][x3] != 0: continue

                        if y1 == y2 and x1 == x2: continue
                        if y1 == y3 and x1 == x3: continue
                        if y2 == y3 and x2 == x3: continue

                        a[y1][x1]=1
                        a[y2][x2]=1
                        a[y3][x3]=1

                        cur = bfs(a)

                        if res < cur: res = cur

                        a[y1][x1]=0
                        a[y2][x2]=0
                        a[y3][x3]=0

print(cnt)