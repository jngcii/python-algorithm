from collections import deque
import sys

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

a = []

for _ in range(n):
    a.append(list(input()))

c1y = -1
c1x = -1
c2y = -1
c2x = -1


for i in range(n):
    for j in range(m):
        if a[i][j] == "o":
            if c1y == -1:
                c1y = i
                c1x = j
            else:
                c2y = i
                c2x = j


q = deque()
q.append((c1y, c1x, c2y, c2x, 0))

while q:
    p1y, p1x, p2y, p2x, cnt = q.popleft()

    if cnt >= 11: continue

    for k in range(4):
        n1y = p1y + dy[k]
        n1x = p1x + dx[k]
        n2y = p2y + dy[k]
        n2x = p2x + dx[k]

        if (0> n1y or n1y >= n or 0> n1x or n1x >= m) and (0> n2y or n2y >= n or 0> n2x or n2x >= m):
            continue
        elif (0> n1y or n1y >= n or 0> n1x or n1x >= m) or (0> n2y or n2y >= n or 0> n2x or n2x >= m):
            print(cnt+1)
            sys.exit(0)
        else:
            if a[n1y][n1x] == '#':
                n1y = p1y
                n1x = p1x
            if a[n2y][n2x] == '#':
                n2y = p2y
                n2x = p2x
            q.append((n1y, n1x, n2y, n2x, cnt+1))

print(-1)