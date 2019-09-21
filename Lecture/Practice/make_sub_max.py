def next_permutation(a):
    i = len(a) - 1

    while i > 0 and a[i] <= a[i-1]: i -= 1

    if i <= 0 : return False

    j = len(a) - 1

    while a[i-1] >= a[j]: j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1

    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


n = int(input())

a = list(map(int, input().split()))

res = -1000


a.sort()

while True:
    s = 0

    for i in range(1, n):
        s += abs(a[i] - a[0])

    res = max(res, s)

    if not next_permutation(a): break

print(res)