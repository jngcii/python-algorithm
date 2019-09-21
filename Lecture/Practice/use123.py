n = int(input())

cnt = 0

def go(sum, n):
    global cnt

    if sum == n:
        cnt += 1
        return

    if sum > n: return

    for i in [1,2,3]:
        go(sum + i, n)

go(0, n)

print(cnt)