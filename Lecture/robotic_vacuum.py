n, m = map(int, input().split())
y, x, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0

while True:
    if a[y][x] == 0:
        a[y][x] = 2

    if a[y+1][x] != 0 and a[y-1][x] != 0 and a[y][x+1] != 0 and a[y][x-1] != 0:
        if a[y-dy[d]][x-dx[d]] == 1: break
        else:
            y -= dy[d]
            x -= dx[d]

    else:
        d = (d+3) % 4
        if a[y+dy[d]][x+dx[d]] == 0:
            y += dy[d]
            x += dx[d]
    
for i in range(n):
    for j in range(m):
        if a[i][j] == 2: cnt += 1

print(cnt)