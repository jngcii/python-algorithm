def go(mid, c):
    cnt = 1

    tmp = a[0]

    for i in range(len(a)):
        if a[i]-tmp >= mid:
            cnt += 1
            tmp = a[i]

    return cnt >= c


n, c = map(int, input().split())

a = []

for _ in range(n):
    a.append(int(input()))

a.sort()

left = 1
right = a[-1] - a[0]

res = 0

while left <= right:
    mid = (left+right)//2

    tmp = go(mid, c)

    if tmp:
        if mid > res:
            res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)