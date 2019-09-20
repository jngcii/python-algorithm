n, m = map(int, input().split())

a = [[] for _ in range(m)]

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

color = [0]*n

def dfs(x, c):
    color[x] = c

    for y in a[x]:
        if color[y] == 0:
            if not dfs(y, 3-c):
                return False
        elif color[x] == color[y]:  #해당 칸이 이미 지나가서 생기 정해져있으면 색깔 비교해서 다른지만 확인!
            return False
    return True

dfs(i, 1)