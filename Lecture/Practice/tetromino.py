dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
shape = [(0,0)] * 4

res = 0

def go(y, x, a, sum, idx):

    global res

    if idx == 3:
        if y < n-1 and x < m-2: # ㅜ
            sum = max(sum, a[y][x] + a[y][x+1] + a[y][x+2] + a[y+1][x+1])
        
        if y > 0 and x < m-2: #ㅗ
            sum = max(sum, a[y][x] + a[y][x+1] + a[y][x+2] + a[y-1][x+1])

        if y < n-2 and x > 0: #ㅓ
            sum = max(sum, a[y][x] + a[y+1][x] + a[y+2][x] + a[y+1][x-1])

        if y < n-2 and x < m-1: #ㅏ
            sum = max(sum, a[y][x] + a[y+1][x] + a[y+2][x] + a[y+1][x+1])

        res = max(res, sum)
        return
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in shape:
            shape[idx] = (y, x)
            go(ny, nx, a, sum + a[ny][nx], idx + 1)
        
for y1 in range(n):
    for x1 in range(m):
        go(y1, x1, a, a[y1][x1], 0)

print(res)