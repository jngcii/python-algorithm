def next_permutation(a):
    i = len(a) - 1
    while i>0 and a[i] <= a[i-1]: i -= 1

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


def calc(a, check):
    c1 = [i for i in range(len(check)) if check[i]==0]
    c2 = [i for i in range(len(check)) if check[i]==1]
    
    r1 = 0
    r2 = 0

    for ci in c1:
        for cj in c1:
            if cj != ci:
                r1 += a[ci][cj]

    for ci in c2:
        for cj in c2:
            if cj != ci:
                r2 += a[ci][cj]

    return abs(r1-r2)



n = int(input())

a = [0]*n

for i in range(n):
    a[i] = list(map(int, input().split()))

check = [0]*(n//2) + [1]*(n//2)

res = calc(a, check)

while next_permutation(check):
    res = min(res, calc(a, check))

print(res)