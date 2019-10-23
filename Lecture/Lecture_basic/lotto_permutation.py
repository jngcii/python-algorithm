def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]: i -= 1

    if i <= 0: return False

    j = len(a) - 1
    while a[j] <= a[i-1]: j -= 1

    a[j], a[i-1] = a[i-1], a[j]

    j = len(a) - 1
    while i < j:
        a[j], a[i] = a[i], a[j]
        i += 1
        j -= 1
    
    return True


n, *a = list(map(int, input().split()))

d = [0]*(n-6) + [1]*6

res = []

while True:
    cur = [a[i] for i in range(n) if d[i] == 1]
    print(cur)

    if not next_permutation(d): break