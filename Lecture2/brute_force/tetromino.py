dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
res = 0
res2 = []

def go(cnt, n, m, y, x, s):
    global res

    if cnt == 4 and s > res:
        res = s
        print(res2)
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0<=ny<n and 0<=nx<m and c[ny][nx] == False:
            c[ny][nx] = True
            res2.append((ny, nx))
            go(cnt+1, n, m, ny, nx, s+a[ny][nx])
    c[ny][nx] = False
    res2.pop()

n, m = map(int, input().split())

a=[list(map(int, input().split())) for _ in range(n)]
c=[[False]*m for _ in range(n)]


for i in range(n):
    for j in range(m):
        res2 = [(i, j)]
        go(1, n, m, i, j, a[i][j])
        
        if i-1>=0 and j+2<m:
            r = a[i][j] + a[i-1][j+1] + a[i][j+1] + a[i][j+2]
            res = max(r, res)
        if i+1<n and j+2<m:
            r = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1]
            res = max(r, res)
        if i+2<n and j-1>=0:
            r = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j-1]
            res = max(r, res)
        if i+2<n and j+1<m:
            r = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j+1]
            res = max(r, res)

print(res)