def check(y, x):
    for i in range(n):
        if i == y: continue
        if a[i][x]: return False

    py = y-1
    px = x-1

    while py >= 0 and px >= 0:
        if a[py][px]: return False
        py -= 1
        px -= 1

    py = y-1
    px = x+1

    while py >= 0 and px < n:
        if a[py][px]: return False
        py -= 1
        px += 1

    return True


def go(y):
    if y == n:
        global res
        res += 1
        return

    for i in range(n):
        a[y][i] = True
        if check(y, i):    #퀸을 a[y][i]에 놓을수 있는지 확인하고 놓는다.
            go(y+1)
        a[y][i] = False



n = int(input())
res = 0
a = [[False]*n for _ in range(n)]
go(0)

print(res)