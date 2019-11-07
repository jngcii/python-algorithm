def go(n):
    res = 0

    for i in range(len(a)):
        if a[i] > n:
            tmp = a[i]-n
            res += tmp

    return res


n, m = map(int, input().split())
a = list(map(int, input().split()))

left = 0
right = max(a)
res = 0

while left <= right:
    mid = (left+right)//2

    tmp = go(mid)
    
    if tmp < m:
        right = mid - 1
    else:
        res = mid
        left = mid + 1

print(res)