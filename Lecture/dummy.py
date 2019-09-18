import sys

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())    #지도 크기
m = int(input())    #사과 갯수
d = [[-1]*n for _ in range(n)] #d[i][j]에 머리가 언제 도착했는지를 기록 지나간적 없으면 -1
apple = [[False]*n for _ in range(n)]
al = [list(map(int, input().split())) for _ in range(m)]

for a in al:
    apple[a[0]-1][a[1]-1] = True

x = 0
y = 0
direction = 0
length = 1
d[y][x] = 0

l = int(input())    # 뱀의 방향 변환 횟수
now = 0

for k in range(l+1):
    t = n**2 + 1
    ch = "L"
    if k<l:
        t, ch = input().split()
        t = int(t)

    while now < t: #다음 방향키를 누를때까지 계속 전진
        now += 1

        # 머리의 위치를 바라보고있는 방향으로 한칸 이동시키기
        y += dy[direction]
        x += dx[direction]

        # 머리 위치가 맵을 벗어나면 현재 시간 프린트하고 끄기
        if x<0 or x>=n or y<0 or y>=n:
            print(now)
            sys.exit(0)

        # 현재 머리위치에 사과가 있으면 길이 하나 늘려주기
        if apple[y][x]:
            apple[y][x] = False
            length += 1
        
        # 현재 머리위치가 지나간 적이 없는 곳이고, 현지 경과 시간에서 그곳을 지나간 시간의 차이보다 몸 길이가 길면 시간 프린트하고 끄기
        if d[y][x] != -1 and now - d[y][x] <= length:
            print(now)
            sys.exit(0)

        # 현재 머리가 지나간 위치에 얼마나 경과했는지 기록
        d[y][x] = now

    if ch == "L": direction = (direction+3)%4
    else: direction = (direction+1)%4