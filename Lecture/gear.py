g = [list(map(int, input().split())) for _ in range(4)]
k = int(input())
m = [list(map(int, inpu().split())) for _ in range(k)]

for i in range(len(m)):
    m[i][0] -= 1

    d = [0]*4               # 먼저 각 한 번의 명령에서 4개의 톱니바퀴가 어느방향으로 돌지

    d[m[i][0]] = m[i][1]    # 각 명령의 정해진 톱니가 어느 방향으로 돌아야 하는지

    j = m[i][0]

    #돌려진 톱니 왼쪽
    left = j - 1
    while left >= 0:
        if g[left][2] != g[left+1][6]:
            d[left] = -d[left+1]
        else: break
    
    #돌려진 톱니 오른쪽
    right = j + 1
    while right <= 4:
        if g[right][6] != g[right-1][2]:
            d[right] = -d[right-1]
        else: break
    
    for idx in range(len(d)):
        if d[idx] == 0: continue
        if d[idx] == 1:
            p = d.pop()
            d = [p] + d
        elif d[idx] == -1:
            p = d.pop(0)
            d.append(p)
    
res = 0

for i in range(4):
    for gi in g:
        if gi == 1:
            res += 2**i

print(res)


    