def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i] <= a[i-1]: i -= 1

    if i <= 0: return False

    j = len(a) - 1
    while a[j] <= a[i-1]: j -= 1

    a[j], a[i-1] = a[i-1], a[j]

    j = len(a) - 1

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    
    return True


n = int(input())

w = [list(map(int, input().split())) for _ in range(n)]

res = 100000000

a = list(range(n))

m = 0

for i in range(-1, n-1):
    m += w[a[i]][a[i+1]]

res = min(res, m)

while next_permutation(a):
    m = 0

    for i in range(-1, n-1):
        m += w[a[i]][a[i+1]]

    res = min(res, m)

print(res)