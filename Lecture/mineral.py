n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]

k = int(input())

heights = list(map(int, input().split()))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(y, x, c, group):
    if a[y][x] == ".": return
    if c[y][x]: return
    c[y][x] = True
    group.append((y,x))
    for k in range(4):
        ny, nx = y + dy[k], x+dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            dfs(ny, nx, c, group)


def simulate():
    c = [[False]*m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if a[y][x] == ".": continue
            if c[y][x]: continue

            group = []
            dfs(y,x,c,group)
            low = [-1]*m

            for gy, gx in group:
                low[gx] = max(low[gx], gy)
                a[gy][gx] = '.'

            lowest = n

            for j in range(m):
                if low[j] == -1:
                    continue
                i = low[j]
                while i < n and a[i][j] == '.':
                    i += 1
                lowest = min(lowest, i-low[j]-1)

            for gy, gx in group:
                gx += lowest
                a[gy][gx] = 'x'
                c[gy][gx] = True


for i, height in enumerate(heights):
    height = n-height

    if i%2==0:
        for j in range(m):
            if a[height][j] == "x":
                a[height][j] = '.'
                break
    else:
        for j in range(m-1, -1, -1):
            if a[height][j] == "*":
                a[height][j] = '.'
                break

    simulate()

for row in a:
    print(''.join(row))