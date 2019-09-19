def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]: i -= 1

    if i <= 0: return False

    j = len(a) - 1
    
    while a[j] <= a[i-1]: j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1

    while j > i:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    
    return True
    

n = int(input())

a = list(range(1, n+1))

c = []

while True:
    c.append(''.join(map(str, a)))
    if not next_permutation(a): break

print(c)