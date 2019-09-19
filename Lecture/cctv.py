n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

cctv = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check(a, b, x, y, dir):
    i, j = x, y
    while 0 <= i < n and 0 <= j < m:
        if a[i][j] == 6: break
        b[i][j] = a[x][y]
        i += dx[dir]
        j += dy[dir]

def go(a, cctv, index, dirs):
    if len(cctv) == index:  #index가 cctv개수가 되었다. : cctv만큼 루프 했다.
        b = [row[:] for row in a]   # a를 깊은 복사

        for i, (what, x, y) in enumerate(cctv):
            if what == 1:
                check(a, b, x, y, dirs[i])
            elif what == 2:
                check(a, b, x, y, dirs[i])
                check(a, b, x, y, (dirs[i]+2)%4)
            elif what == 3:
                check(a, b, x, y, dir[i])
                check(a, b, x, y, (dirs[i]+1)%4)
            elif what == 4:
                check(a, b, x, y, dir[i])
                check(a, b, x, y, (dirs[i]+1)%4)
                check(a, b, x, y, (dirs[i]+2)%4)
            elif what == 5:
                check(a, b, x, y, dir[i])
                check(a, b, x, y, (dirs[i]+1)%4)
                check(a, b, x, y, (dirs[i]+2)%4)
                check(a, b, x, y, (dirs[i]+3)%4)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if b[i][j] == 0:
                    cnt += 1

        return cnt

    
    res = 100

    for i in range(4):
        tmp = go(a, cctv, index+1, dirs + [i])
        if tmp < res: res = tmp

    return res



for i in range(n):
    for j in range(m):
        if 1 <= a[i][j] <= 5: cctv.append((a[i][j], i, j))

print(go(a, cctv, 0, []))