n = int(input())
num = list(range(n))
a = [list(map(int, input().split())) for _ in range(n)]

def next_permutation(x):
    i = len(x) - 1

    while i > 0 and x[i-1] >= x[i]: i -= 1

    if i <= 0: return False

    j = len(x) - 1

    while x[i-1] >= x[j]: j -= 1

    x[i-1], x[j] = x[j], x[i-1]


    while j > i:
        x[j],x[i] = x[i],x[j]
        j -= 1
        i += 1

    return True

num.sort()
res = 11000000

while True:
    ok = True
    s = 0
    for i in range(0, n):
        if a[num[i-1]][num[i]] == 0:
            ok = False
            break
        s += a[num[i-1]][num[i]]

    if ok and s < res: res = s

    if not next_permutation(num): break
    if num[0] != 0: break

print(res)