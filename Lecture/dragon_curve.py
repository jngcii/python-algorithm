dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

c = [[False]*21 for _ in range(21)]

def curve(d, g):
    res = [d]
    
    for _ in range(1, g+1):
        tmp = res
        tmp.reverse()
        for ti in range(len(tmp)):
            tmp[ti] = (tmp[ti] + 1)%4
        res += tmp

    return res




n = int(input())

for _ in range(n):
    x, y, d, g = map(int, input().split())
    dirs = curve(d, g)

    c[y][x] = True
    for dir in dirs:
        x += dx[dir]
        y += dy[dir]
        c[y][x] = True

res = 0

for ci in c:
    print(ci)

for i in range(20):
    for j in range(20):
        if c[i][j] and c[i][j+1] and c[i+1][j] and c[i+1][j+1]: res += 1

print(res)