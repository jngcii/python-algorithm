n = int(input())

coins=[]

for _ in range(n):
    coins.append(list(input()))

heads=[0]*n
tails=[0]*n

while True:

    for i in range(n):
        heads[i] = coins[i].count('H')


    for i in range(n):
        c = 0
        for j in range(n):
            if coins[j][i] == 'H': c += 1
        tails[i] = c
    
    p = 0
    type = (0,0)

    for i in range(n):
        if heads[i] > n-heads[i]:
            if heads[i] > p:
                p=heads[i]
                type=(0,i)

    for i in range(n):
        if tails[i] > n-tails[i]:
            if tails[i] > p:
                p=tails[i]
                type=(1,i)

    if p == 0: break

    if type[0] == 0:
        for i in range(n):
            if coins[type[1]][i] == "H": coins[type[1]][i] = "T"
            else: coins[type[1]][i] = "H"
    else:
        for i in range(n):
            if coins[i][type[1]] == "H": coins[i][type[1]] = "T"
            else: coins[i][type[1]] = "H"



print(sum(heads))
