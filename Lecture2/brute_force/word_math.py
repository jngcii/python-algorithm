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


def cal(a, letters, numbers):
    d = dict()
    for i in range(len(letters)):
        d[letters[i]] = numbers[i]

    r = 0
    for ai in a:
        r1 = 0
        for aii in ai:
            r1 = r1 * 10 + d[aii]

        r += r1
    
    return r


n = int(input())

a = []
for _ in range(n):
    a.append(input())


letters = []

for ai in a:
    for aii in ai:
        if aii not in letters: letters.append(aii)

numbers = list(range(10-len(letters), 10))

res = cal(a, letters, numbers)

while next_permutation(numbers):
    res = max(res, cal(a, letters, numbers))

print(res)