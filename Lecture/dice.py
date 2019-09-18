dx = [0,0,-1,1]
dy = [-1,1,0,0]
n,m,x,y,l = map(int, input().split( ))
a = [list(map(int, input().split( ))) for  _ in range(n)]
dice = [0] * 7 #첫 값을 그대로 두고 1번 인덱스부터 6번인덱스까지
move = list(map(int, input().split( )))
for k in move:
    k -= 1 #입력값이 1~4이고 dx, dy의 인덱스는 0~3이라서 1 빼준다.
    nx, ny = x+dx[k], y+dy[k] #현재 위치인 x, y에서 움직인 값을 계산한다.
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue #만약 움직인 값이 가로 세로 값을 넘어가면 현재위치를 바꾸지않고 그대로 다음 움직임을 실행
    if k == 0:
        tmp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = tmp
    elif k == 1:
        tmp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] =tmp
    elif k == 2:
        tmp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = tmp
    else:
        tmp = dice[1]
        dice[1] = dicep[2]
        dice[2] = dicep[6]
        dice[6] = dicep[5]
        dice[7] = tmp

    x, y = nx, ny

    if a[x][y] == 0:
        a[x][y] == dice[6]
    else:
        dice[6] = a[x][y]
        a[x][y] = 0
    
    print(dice[1])