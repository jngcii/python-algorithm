from collections import deque

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

def bfs(n, check, r1, c1, r2, c2):
    q = deque()
    q.append((r1, c1))

    while q:
        r, c = q.popleft()

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<n and 0<=nc<n and check[nr][nc] == -1:
                check[nr][nc] = check[r][c] + 1
                if nr == r2 and nc == c2: return
                q.append((nr, nc))


n = int(input())

r1, c1, r2, c2 = map(int, input().split())

c = [[-1]*n for _ in range(n)]

c[r1][c1] = 0

bfs(n, c, r1, c1, r2, c2)

print(c[r2][c2])