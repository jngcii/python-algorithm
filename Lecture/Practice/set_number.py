from collections import deque

n = int(input())

a = [list(map(int, list(input()))) for _ in range(n)]

c = [[0] * n for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

res = []

def bfs(y, x, res):

    q = deque()
    q.append((y, x))
    asdf = 1

    while q:
        y, x = q.popleft()

        a[y][x] = 0

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                if a[ny][nx] == 1:
                    q.append((ny, nx))
                    a[ny][nx] = 0
                    asdf += 1
       
    res.append(asdf)


for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            bfs(i, j, res)

res.sort()

print(len(res))
print(res)