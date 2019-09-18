dy = [0,0,1,-1]
dx = [1,-1,0,0]

n,m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

c = [[False]*m for _ in range(n)]

res = 0

def go(y, x, sum, cnt):
    if cnt == 4:
        global res
        if res < sum:
            res = sum
            return

    if y < 0 or x < 0 or y >= n or x >= m: return

    if c[y][x]: return

    c[y][x] = True

    for k in range(4):
        go(y+dy[k], x+dx[k], sum + a[y][x], cnt+1)
    
    c[y][x] = False


for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)

        if j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2]
            if i-1 >= 0:
                tmp2 = tmp + a[i-1][j+1]
                if res < tmp2: res = tmp2
            if i+1 <= n:
                tmp2 = tmp + a[i+1][j+1]
                if res < tmp2: res = tmp2
        if i+2 < n:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j]
            if j-1 > 0:
                tmp2 = tmp + a[i+1][j-1]
                if tmp2 > res: res = tmp2
            if j+1 < m:
                tmp2 = tmp + a[i+1][j+1]
                if tmp2 > res: res = tmp2

print(res)
