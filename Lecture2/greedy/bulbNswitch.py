n = int(input())

a1 = [0]*n
a2 = [0]*n
b = [0]*n

cnt1 = 1
cnt2 = 0

ai = list(input())
bi = list(input())

for i in range(n):
    a1[i] = int(ai[i])
    a2[i] = int(ai[i])

for i in range(n):
    b[i] = int(bi[i])

a1[0] = 1-a1[0]
a1[1] = 1-a1[1]

for i in range(1, n-1):
    if a1[i-1] != b[i-1]:
        a1[i-1] = 1-a1[i-1]
        a1[i] = 1-a1[i]
        a1[i+1] = 1-a1[i+1]
        cnt1 += 1
        
    if a2[i-1] != b[i-1]:
        a2[i-1] = 1-a2[i-1]
        a2[i] = 1-a2[i]
        a2[i+1] = 1-a2[i+1]
        cnt2 += 1

if a1[-2]!=b[-2]:
    a1[-2]=1-a1[-2]
    a1[-1]=1-a1[-1]
    cnt1+=1
    if a1[-1] != b[-1]: cnt1=-1

if a2[-2]!=b[-2]:
    a2[-2]=1-a2[-2]
    a2[-1]=1-a2[-1]
    cnt2+=1
    if a2[-1] != b[-1]: cnt2=-1

if cnt1 == -1 and cnt2 == -1: print(-1)
elif cnt1 == -1 and cnt2 >-1: print(cnt2)
elif cnt2 == -1 and cnt1 >-1: print(cnt1)