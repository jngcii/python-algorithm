def next_permutation(a):
    
    i = len(a) -1

    while i > 0 and a[i-1] >= a[i]: i -= 1
    
    if i == 0: return False

    j = len(a) - 1

    while j > i-1 and a[j] < a[i]: j -= 1

    a[j], a[i-1] = a[i-1], a[j]

    j = len(a) - 1

    while i < j:
        a[j], a[i] = a[i], a[j]
        i += 1
        j -= 1

    return True

