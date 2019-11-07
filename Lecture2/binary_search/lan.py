def go(n):
    res = 0
    for ai in a:
        tmp = ai//n
        res += tmp
    
    return res



k, n = map(int, input().split())

a = []

for _ in range(k):
    a.append(int(input()))

left = 1
right = max(a)

res = 0

while left <= right:
    mid = (left+right)//2

    tmp = go(mid)

    if tmp < n:
        right = mid - 1
    else:
        res = mid
        left = mid + 1

print(res)
