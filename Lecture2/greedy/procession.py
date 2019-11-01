def switch(a, i, j):
    for ii in range(i, i+3):
        for jj in range(j, j+3):
            a[ii][jj] = 1-a[ii][jj]


n, m = map(int, input().split())

a = [[0]*m for _ in range(n)]
b = [[0]*m for _ in range(n)]

cnt = 0

for i in range(n):
    ai = list(input())
    for j in range(len(ai)):
        a[i][j] = int(ai[j])

for i in range(n):
    bi = list(input())
    for j in range(len(bi)):
        b[i][j] = int(bi[j])

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            switch(a, i, j)
            cnt += 1

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]: cnt = -1
    if cnt == -1: break

print(cnt)