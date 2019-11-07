def go(n):
    nn = str(n)
    length = 1
    res = 0

    while len(nn) > length:
        length += 1
    
    m = 10**(length-1)

    i = length

    while i > 1:
        i -= 1
        res += (9*i*(10**(i-1)))

    res += (n-m+1)*length

    return res


n, k = map(int, input().split())

left = 1
right = n
res = 0

while left <= right:
    mid = (left+right)//2

    loc = go(mid)
    
    if loc < k:
        left = mid + 1
    else:
        res = mid
        right = mid - 1

print(res)

print(int(str(res)[k-go(res)-1]))